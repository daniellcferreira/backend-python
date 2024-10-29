from flask import Flask, url_for, request

app = Flask(__name__)

@app.route("/exemplo/<usuario>/<int:idade>")
def hello_world(usuario, idade):
    print(idade)
    print(type(idade))
    print(type(usuario))
    return f"<p>Hello, usuário: {usuario}!</p>"


@app.route("/exemplo2")
def bem_vindo():
    return "<p>Bem vindo!</p>"


# redirecionamento de comportamento

@app.route("/projects/")
def projects():
    return "The project page"

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return "This is a GET"
    else:
        return "This is a POST"

# url building

with app.test_request_context():
    print(url_for("bem_vindo"))
    print(url_for("projects"))
    print(url_for("about", next="/"))
    print(url_for("hello_world", usuario="Daniel", idade=30))


# APIs com JSON

@app.route("/exemplo3")
def saudacao():
    return {"messege": "Olá mundo!"}