from fastapi import FastAPI, status, Cookie, Response, Header
from datetime import datetime, UTC
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

fake_db = [
    {
        "title": "Criando uma aplicação com FastAPI",
        "date": datetime.now(UTC),
        "published": True,
    },
    {
        "title": "Criando uma aplicação com Django",
        "date": datetime.now(UTC),
        "publshed": True,
    },
    {
        "title": "Criando uma aplicação com Flask",
        "date": datetime.now(UTC),
        "published": True,
    },
    {
        "title": "Criando uma aplicação com Pyramid",
        "date": datetime.now(UTC),
        "published": False,
    },
]


class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False


@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    return post


@app.get("/posts/")
def read_posts(
    response: Response,
    published: bool,
    skip: int,
    limit: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
):
    response.set_cookie(key="user", value="email@email.com")

    posts = []
    for post in fake_db:
        if len(posts) == limit:
            break
        if post["published"] == published:
            posts.append(post)

    return posts


@app.get("/posts/{framework}")
def read_framework_posts(framework: str):
    return {
        "posts": [
            {
                "title": f"Criando uma aplicação com {framework}",
                "date": datetime.now(UTC),
            },
            {
                "title": f"Internacionalizando uma app {framework}",
                "date": datetime.now(UTC),
            },
        ]
    }
