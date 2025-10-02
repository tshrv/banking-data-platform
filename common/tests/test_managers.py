import pytest
from pydantic import ValidationError
from sqlmodel.ext.asyncio.session import AsyncSession

from common.managers.users import UserManager
from common.models.user import User


@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.parametrize(
    "name, date_of_birth, mobile_number, pan, address",
    [
        (
            "John Doe",
            "1996-03-01",
            "7898589658",
            "FOEKG2761H",
            "A10 Avenue City",
        )
    ],
)
async def test_user_manager_success(
    session: AsyncSession,
    name: str,
    date_of_birth: str,
    mobile_number: str,
    pan: str,
    address: str,
):
    """Create user record and verify it exists"""
    user = await UserManager(session).create_user(
        User(
            name=name,
            date_of_birth=date_of_birth,
            mobile_number=mobile_number,
            pan=pan,
            address=address,
        )
    )
    assert user.id is not None


@pytest.mark.asyncio(loop_scope="session")
@pytest.mark.parametrize(
    "name, date_of_birth, mobile_number, pan, address",
    [
        (
            "",
            "1996-03-01",
            "7898589658",
            "FOEKG2761H",
            "A10 Avenue City",
        ),
        (
            "John",
            "1996-03-1",
            "7898589658",
            "FOEKG2761H",
            "A10 Avenue City",
        ),
        (
            "John",
            "1996-03-11",
            "789858965a",
            "FOEKG2761H",
            "A10 Avenue City",
        ),
        (
            "John",
            "1996-03-11",
            "7898589658",
            "FOEKG27611",
            "A10 Avenue City",
        ),
        (
            "John",
            "1996-03-11",
            "7898589658",
            "FOEKG2761H",
            "",
        ),
    ],
)
async def test_user_manager_validation_error(
    session: AsyncSession,
    name: str,
    date_of_birth: str,
    mobile_number: str,
    pan: str,
    address: str,
):
    """Ensure that invalid data raises ValidationError"""
    with pytest.raises(ValidationError):
        await UserManager(session).create_user(
            User(
                name=name,
                date_of_birth=date_of_birth,
                mobile_number=mobile_number,
                pan=pan,
                address=address,
            )
        )
