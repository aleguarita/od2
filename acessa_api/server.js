const express = require("express");
const passport = require("passport");
const OAuth2Strategy = require("passport-oauth2");
const session = require("express-session");
const axios = require("axios");
require("dotenv").config();

passport.use(
  "oauth2",
  new OAuth2Strategy(
    {
      authorizationURL: "https://olddragon.com.br/authorize",
      tokenURL: "https://olddragon.com.br/token",
      clientID: process.env.ID,
      clientSecret: process.env.CHAVE,
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

// app.get("/callback", (req, res, next) => {
//   passport.authenticate("oauth2", (err, user, info) => {
//     if (err) {
//       console.error("Authentication Error:", err);
//       return res.send("Authentication Error: " + err.message);
//     }
//     if (!user) {
//       console.error("Authentication Failed:", info);
//       return res.redirect("/");
//     }
//     req.logIn(user, async (err) => {
//       if (err) {
//         console.error("Login Error:", err);
//         return next(err);
//       }

//       // Agora vamos usar os tokens
//       try {
//         const response = await axios.get(
//           "https://olddragon.com.br/campanhas.json",
//           {
//             headers: {
//               Authorization: `Bearer ${req.user.accessToken}`,
//             },
//           }
//         );
//         res.send(
//           `<html><head><title>OldDragon OAuth2 Node.js</title><link rel='stylesheet' href='https://unpkg.com/simpledotcss@2.1.0/simple.min.css'></head><body>` +
//             `<h2>Access Token</h2><pre>${req.user.accessToken}</pre>"` +
//             `<h2>/campanhas.json</h2><pre>${JSON.stringify(
//               response.data
//             )}</pre>`
//         );
//       } catch (error) {
//         console.error("Error fetching campanhas:", error);
//         if (error.response && error.response.status === 401) {
//           // Handle token expiration, e.g., try to refresh the token
//           // If refresh token is also expired, redirect to login
//         }
//         res.status(500).send("Error fetching campanhas");
//       }
//     });
//   })(req, res, next);
// });

app.get("/callback", (req, res, next) => {
  passport.authenticate("oauth2", async (err, user, info) => {
    if (err) return res.send("Authentication Error: " + err.message);
    if (!user) return res.redirect("/");

    req.logIn(user, async (err) => {
      if (err) return next(err);

      const endpoints = [
        "classes",
        "monstros",
        "habilidades",
        "magias",
        "talentos",
        "pericias",
      ];

      const fs = require("fs");
      const path = require("path");
      const downloadResults = [];

      for (const endpoint of endpoints) {
        try {
          const url = `https://olddragon.com.br/api/${endpoint}`;
          const response = await axios.get(url, {
            headers: {
              Authorization: `Bearer ${req.user.accessToken}`,
            },
          });

          const filename = path.join(__dirname, `${endpoint}.json`);
          fs.writeFileSync(filename, JSON.stringify(response.data, null, 2));
          downloadResults.push(`${endpoint}.json salvo com sucesso.`);
        } catch (error) {
          console.error(`Erro ao baixar ${endpoint}:`, error.message);
          downloadResults.push(`Erro ao baixar ${endpoint}`);
        }
      }

      res.send(
        `<h2>Download completo</h2><ul>${downloadResults
          .map((msg) => `<li>${msg}</li>`)
          .join("")}</ul>`
      );
    });
  })(req, res, next);
});


app.listen(3000, () => {
  console.log("Server is running...");
});