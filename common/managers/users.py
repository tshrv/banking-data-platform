from loguru import logger

from common.models.types import AsyncSession
from common.models.user import User, UserDB


class UserManager:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create_user(self, user: User) -> UserDB:
        """Create a user and return created object"""
        user_db = UserDB(**user.model_dump())
        self._session.add(user_db)
        await self._session.flush()
        logger.info(f'New user "{user_db.name}" created')
        return user_db
