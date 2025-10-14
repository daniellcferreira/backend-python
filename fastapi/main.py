from fastapi import FastAPI
from controllers import post
from contextlib import asynccontextmanager
from database import database, metadata, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.post import posts  # noqa: F401

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(post.router)
