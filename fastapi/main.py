from fastapi import FastAPI
from datetime import datetime, UTC

app = FastAPI()


@app.get("/posts/{framework}")
def read_posts(framework: str):
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
