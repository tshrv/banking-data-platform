from setuptools import find_packages, setup

setup(
    name="common",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "loguru>=0.7.3",
        "pydantic>=2.11.9",
        "pydantic-settings>=2.7.1",
        "pydantic[email]",
        "pydantic>=2.11.9",
        "pydantic-settings>=2.7.1",
        "pydantic[email]",
        "python-decouple>=3.8",
        "sqlmodel[asyncio]>=0.0.22",
    ],
)
