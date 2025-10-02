from typing import Annotated

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from common.clients.db import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]
