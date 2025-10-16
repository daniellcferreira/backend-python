from database import database
from databases.interfaces import Record
from fastapi import HTTPException, status
from models.post import posts
from schemas.post import PostIn, PostUpdateIn


class PostService:
    async def read_all(
        self, published: bool | None = None, skip: int = 0, limit: int = 0
    ) -> list[Record]:
        query = posts.select()
        if published is not None:
            query = query.where(posts.c.published == published)
        if limit > 0:
            query = query.limit(limit)
        query = query.offset(skip)
        return await database.fetch_all(query)

    async def create(self, post: PostIn) -> int:
        command = posts.insert().values(
            title=post.title,
            content=post.content,
            published=post.published,
            published_at=post.published_at,
        )
        return await database.execute(command)

    async def read(self, id: int) -> Record:
        return await self.__get_by_id(id)

    async def update(self, id: int, post: PostUpdateIn) -> Record:
        exists = await self.count(id)
        if not exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Post with id {id} not found",
            )

        data = post.model_dump(exclude_unset=True)
        command = posts.update().where(posts.c.id == id).values(**data)
        await database.execute(command)
        return await self.__get_by_id(id)

    async def delete(self, id: int) -> None:
        command = posts.delete().where(posts.c.id == id)
        await database.execute(command)

    async def count(self, id: int) -> int:
        query = "SELECT COUNT(id) AS total FROM posts WHERE id = :id"
        result = await database.fetch_one(query, {"id": id})
        return result["total"] if result else 0

    async def __get_by_id(self, id: int) -> Record:
        query = posts.select().where(posts.c.id == id)
        post = await database.fetch_one(query)
        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Post with id {id} not found",
            )
        return post
