from fastapi import FastAPI

from controllers import post

app = FastAPI()
app.include_router(post.router)
