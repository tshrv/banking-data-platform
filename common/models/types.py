from pydantic import StringConstraints
from sqlmodel.ext.asyncio.session import AsyncSession as _AsyncSession
from typing_extensions import Annotated

AsyncSession = _AsyncSession


MobileNumber = Annotated[
    str, StringConstraints(strip_whitespace=True, pattern=r"^\d{10}$")
]

PermanentAccountNumber = Annotated[
    str,
    StringConstraints(strip_whitespace=True, pattern=r"^[a-zA-Z]{5}\d{4}[a-zA-Z]{1}$"),
]
