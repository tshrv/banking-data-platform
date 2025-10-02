from datetime import date
from uuid import UUID, uuid4

from pydantic import StringConstraints
from sqlmodel import Field, UniqueConstraint
from typing_extensions import Annotated

from .base import BaseModel
from .types import MobileNumber, PermanentAccountNumber


class User(BaseModel):
    name: Annotated[str, StringConstraints(strip_whitespace=True)] = Field(
        nullable=False,
        min_length=2,
    )
    date_of_birth: date = Field(nullable=False)
    mobile_number: MobileNumber = Field(
        nullable=False,
        unique=True,
        index=True,
        min_length=10,
        max_length=10,
    )
    pan: PermanentAccountNumber = Field(
        nullable=False,
        unique=True,
        index=True,
        min_length=10,
        max_length=10,
    )
    address: Annotated[str, StringConstraints(strip_whitespace=True)] = Field(
        nullable=False, min_length=5, max_length=255
    )


class UserDB(User, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)

    __table_args__ = (
        UniqueConstraint("mobile_number"),
        UniqueConstraint("pan"),
    )
