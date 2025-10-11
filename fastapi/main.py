from fastapi import FastAPI  # Importa o framework FastAPI

app = FastAPI()  # Cria uma instância da aplicação

@app.get("/")  # Define uma rota GET no endpoint raiz "/"
def read_root():
  return {"message": "Hello World"}  # Retorna uma resposta JSON
