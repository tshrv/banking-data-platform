from pydantic import ConfigDict
from pydantic.alias_generators import to_camel
from sqlmodel import SQLModel


class BaseModel(SQLModel):
    """Base SQL Model to be used through out the application"""

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
