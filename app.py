from flask import Flask, request

app = Flask(__name__)

@app.get("/testando/query_params")
def query_params_route():
    nome = request.args.get('nome')

    if nome:
        return {"mensagem":f"Olá {nome}! Seja bem vindo! :D"}
   
   
    return {"mensagem": "status ok"}
