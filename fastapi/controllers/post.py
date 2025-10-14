from fastapi import status, Response, APIRouter
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    # fake_db.append(post.model_dump())
    return post


@router.get("/", response_model=list[PostOut])
def read_posts(
    response: Response,
    published: bool,
    skip: int,
    limit: int = 0,
):

    return []
