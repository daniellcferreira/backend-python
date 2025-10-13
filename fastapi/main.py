from fastapi import FastAPI
from datetime import datetime, UTC

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


@app.get("/posts")
def read_posts(
    published: bool,
    skip: int = 0,
    limit: int = len(fake_db),
):
    return [
        post for post in fake_db[skip : skip + limit] if post["published"] is published
    ]


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
