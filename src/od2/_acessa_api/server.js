const express = require("express");
const passport = require("passport");
const OAuth2Strategy = require("passport-oauth2");
const session = require("express-session");
const axios = require("axios");

const endpoints = [
    "campanhas",
    "classes",
    "equipamentos",
    "livros",
    "magias",
    "monstros",
    "personagens",
    "racas",
    "https://olddragon.com.br/livros/lb1.json",
    "https://olddragon.com.br/livros/lb2.json",
    "https://olddragon.com.br/livros/lb3.json",
]

passport.use(
  "oauth2",
  new OAuth2Strategy(
    {
      authorizationURL: "https://olddragon.com.br/authorize",
      tokenURL: "https://olddragon.com.br/token",
      clientID: process.env.CLIENT_ID,
      clientSecret: process.env.CLIENT_SECRET,
      callbackURL: `https://${process.env.PROJECT_DOMAIN}.glitch.me/callback`,
      scope: "openid email content.read offline_access",
      prompt: "consent",
      scopeSeparator: " ",
    },
    (accessToken, refreshToken, profile, cb) => {
      profile.accessToken = accessToken;
      profile.refreshToken = refreshToken;
      return cb(null, profile);
    }
  )
);

passport.serializeUser((user, done) => done(null, user));
passport.deserializeUser((obj, done) => done(null, obj));

const app = express();

app.use(
  session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: true,
  })
);

app.use(passport.initialize());
app.use(passport.session());

app.get("/", (req, res) => {
  res.send(
    `<html><head><title>OldDragon OAuth2 Node.js</title><link rel='stylesheet' href='https://unpkg.com/simpledotcss@2.1.0/simple.min.css'></head><body>` +
      `<h2>Integração com Old Dragon</h2>` +
      `<a href="/login">Login com OldDragon</a>`
  );
});

app.get("/login", passport.authenticate("oauth2"));

async function fetchAllPages(endpoint, token) {
  const allData = [];
  let url = endpoint.startsWith("http") ? endpoint : `https://olddragon.com.br/${endpoint}.json`;


  while (url) {
    const response = await axios.get(url, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (Array.isArray(response.data)) {
      allData.push(...response.data);
    } else {
      // Se não for paginado ou não for array, apenas retorna direto
      return response.data;
    }

    // Analisa o cabeçalho Link
    const linkHeader = response.headers.link;
    const nextMatch = linkHeader && linkHeader.match(/<([^>]+)>;\s*rel="next"/);
    url = nextMatch ? nextMatch[1] : null;
  }

  return allData;
}


app.get("/callback", (req, res, next) => {
  passport.authenticate("oauth2", async (err, user, info) => {
    if (err) {
      console.error("Authentication Error:", err);
      return res.send("Authentication Error: " + err.message);
    }
    if (!user) {
      console.error("Authentication Failed:", info);
      return res.redirect("/");
    }

    req.logIn(user, async (err) => {
      if (err) {
        console.error("Login Error:", err);
        return next(err);
      }

      try {
        // Mapeia cada endpoint e faz a requisição
        const results = await Promise.all(
          endpoints.map(async (endpoint) => {
            try {
              const data = await fetchAllPages(endpoint, req.user.accessToken);
              return { endpoint, data };
            } catch (error) {
              console.error(`Erro ao buscar ${endpoint}:`, error.message);
              return { endpoint, error: error.message };
            }
          })
        );


        // Gera HTML com todos os dados retornados
        const htmlSections = results
          .map((result, index) => {
            const safeId = `jsonData${index}`;
            if (result.error) {
              return `<h2>/${result.endpoint}.json</h2><p>Erro: ${result.error}</p>`;
            } else {
              const jsonString = JSON.stringify(result.data, null, 2);
              const escapedJson = jsonString.replace(/</g, "&lt;").replace(/>/g, "&gt;");

              return `
                <h2>${result.endpoint.replace("https://olddragon.com.br/", "/")}</h2>
                <button onclick="downloadJSON('${safeId}', '${result.endpoint.replace(/^https?:\/\/[^/]+\/?/, "").replace(/\.json$/, "")}.json')">Baixar JSON</button>
                <pre id="${safeId}">${escapedJson}</pre>
              `;
            }
          })
          .join("");


        res.send(
          `<html><head><title>OldDragon OAuth2 Node.js</title>
            <link rel='stylesheet' href='https://unpkg.com/simpledotcss@2.1.0/simple.min.css'>
          </head><body>
            <h2>Access Token</h2><pre>${req.user.accessToken}</pre>
            ${htmlSections}
            <script>
              function downloadJSON(preId, filename) {
                const content = document.getElementById(preId).innerText;
                const blob = new Blob([content], { type: "application/json" });
                const url = URL.createObjectURL(blob);
                const a = document.createElement("a");
                a.href = url;
                a.download = filename;
                a.click();
                URL.revokeObjectURL(url);
              }
            </script>
          </body></html>`
        );

      } catch (error) {
        console.error("Erro geral:", error);
        res.status(500).send("Erro ao buscar dados dos endpoints.");
      }
    });
  })(req, res, next);
});


app.listen(3000, () => {
  console.log("Server is running...");
});
