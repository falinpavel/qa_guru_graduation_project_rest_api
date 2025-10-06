import pytest
from dotenv import load_dotenv

from config import Settings


@pytest.fixture(scope="session")
def settings() -> Settings:
    load_dotenv()
    return Settings()
