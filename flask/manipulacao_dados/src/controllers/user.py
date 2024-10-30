from flask import Blueprint, request
from src.app import User, db
from http import HTTPStatus

app = Blueprint("user", __name__, url_prefix="/users")

def _create_user():
    data = request.json
    user = User(username=data["username"])
    db.session.add(user)
    db.session.commit()

def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return [
        {
            "id": user.id,
            "username": user.username,
        }
        for user in users
    ]

@app.route("/", methods=["GET", "POST"])
def handle_user():
    if request.method == "POST":
        _create_user()
        return {"messege": "User created"}, HTTPStatus.CREATED
    else:
        return {"users": _list_users()}

@app.route("/<int:user_id>")
def get_user(user_id):
    user = db.get_or_404(User, user_id)
    return {
        "id": user.id,
        "username": user.username,
    }

@app.route("/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    user = db.get_or_404(User, user_id)
    data = request.json

    if "username" in data:
        user.username = data["username"]
        db.session.commit()

    return {
        "id": user.id,
        "username": user.username,  
    }

@app.route("/<int:user_id>", methods=["DELETE"])
def delete(user_id):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    
    return "", HTTPStatus.NO_CONTENT