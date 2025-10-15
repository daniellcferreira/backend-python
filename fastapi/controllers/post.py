from fastapi import status, APIRouter, Depends
from schemas.post import PostIn, PostUpdateIn
from views.post import PostOut
from models.post import posts
from database import database
from security import login_required
from services.post import PostService

router = APIRouter(prefix="/posts", dependencies=[Depends(login_required)])

service = PostService()


@router.get("/", response_model=list[PostOut])
async def read_posts(
    published: bool,
    skip: int = 0,
    limit: int = 0,
):
    return await service.read_all(published=published, skip=skip, limit=limit)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    command = posts.insert().values(
        title=post.title,
        content=post.content,
        published=post.published,
        published_at=post.published_at,
    )
    last_id = await database.execute(command)
    return {**post.model_dump(), "id": last_id}


@router.get("/{id}", response_model=PostOut)
async def read_post(id: int):
    return await service.read(id)


@router.patch("/{id}", response_model=PostOut)
async def update_post(id: int, post: PostUpdateIn):
    return await service.update(id=id, post=post)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_post(id: int):
    return await service.delete(id)
