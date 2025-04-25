import os

# identificação
CLIENTE_ID = os.getenv('ID')
CLIENTE_SECRET = os.getenv('CHAVE')

# autenticação
AUTHORIZATION_URL = "https://olddragon.com.br/authorize"
TOKEN_URL = "https://olddragon.com.br/token"
REDIRECT_URI = "https://postman-echo.com/oauth/post"

# escopo autorizado
SCOPE = "openid email content.read offline_access"

# api base
API_BASE_URL = "https://olddragon.com.br/"

# cabeçalho de identifcação
USER_AGENT = "OD2 (alessandro.guarita@gmail.com)"

# caminho local para armazenar o token
TOKEN_FILE = "token.json"
