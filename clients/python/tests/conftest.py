import json
import warnings
import os
import shutil
from typing import IO, Any

import pytest

os.environ["EMAIL_DOMAIN"] = "devmail.uiform.com"
from enum import Enum
from typing import Generator

from dotenv import load_dotenv
from pydantic import BaseModel, Field

from uiform import AsyncUiForm, UiForm

# Get the directory containing the tests
TEST_DIR = os.path.dirname(os.path.abspath(__file__))


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--production", action="store_true", default=False, help="run tests against production API")
    parser.addoption("--local", action="store_true", default=False, help="run tests against local API")
    parser.addoption("--staging", action="store_true", default=False, help="run tests against staging API")


@pytest.fixture(scope="session", autouse=True)
def load_env(request: pytest.FixtureRequest) -> None:
    """Load the appropriate .env file based on the environment flag"""
    if request.config.getoption("--production"):
        env_file = "../../.env.production"
    elif request.config.getoption("--local"):
        env_file = "../../.env.local"
    elif request.config.getoption("--staging"):
        env_file = "../../.env.staging"
    else:
        raise ValueError("No environment specified. Please use --production or --local or --staging.")

    env_path = os.path.join(os.path.dirname(TEST_DIR), env_file)
    print("loading env file: ", env_path)
    if not os.path.exists(env_path):
        warnings.warn(f"Environment file not found: {env_path}", UserWarning)
    else:
        load_dotenv(env_path, override=True)
    print("EMAIL_DOMAIN", os.environ["EMAIL_DOMAIN"])


class EnvConfig(BaseModel):
    uiform_api_key: str = Field(..., description="UiForm API key")
    uiform_api_base_url: str = Field(..., description="UiForm API base URL")
    openai_api_key: str = Field(..., description="OpenAI API key")
    # claude_api_key: str = Field(..., description="Claude API key")
    # gemini_api_key: str = Field(..., description="Gemini API key")
    # xai_api_key: str = Field(..., description="XAI API key")


@pytest.fixture(scope="session")
def api_keys(load_env: None) -> EnvConfig:
    uiform_api_key = os.getenv("UIFORM_API_KEY")
    uiform_api_base_url = os.getenv("UIFORM_API_BASE_URL")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    # claude_api_key = os.getenv("CLAUDE_API_KEY")
    # gemini_api_key = os.getenv("GEMINI_API_KEY")
    # xai_api_key = os.getenv("XAI_API_KEY")

    assert uiform_api_key is not None
    assert uiform_api_base_url is not None
    assert openai_api_key is not None
    # assert claude_api_key is not None
    # assert gemini_api_key is not None
    # assert xai_api_key is not None

    return EnvConfig(
        uiform_api_key=uiform_api_key,
        uiform_api_base_url=uiform_api_base_url,
        openai_api_key=openai_api_key,
        # claude_api_key=claude_api_key,
        # gemini_api_key=gemini_api_key,
        # xai_api_key=xai_api_key
    )


@pytest.fixture(scope="session")
def base_url(request: pytest.FixtureRequest, api_keys: EnvConfig) -> str:
    return api_keys.uiform_api_base_url


@pytest.fixture(scope="session")
def uiform_api_key(api_keys: EnvConfig) -> str:
    return api_keys.uiform_api_key


@pytest.fixture(scope="function")
def sync_client(base_url: str, uiform_api_key: str, api_keys: EnvConfig) -> UiForm:
    return UiForm(
        api_key=uiform_api_key,
        base_url=base_url,
        openai_api_key=api_keys.openai_api_key,
        # claude_api_key=api_keys.claude_api_key,
        # gemini_api_key=api_keys.gemini_api_key,
        # xai_api_key=api_keys.xai_api_key,
        max_retries=3,
    )


@pytest.fixture(scope="function")
def async_client(base_url: str, uiform_api_key: str, api_keys: EnvConfig) -> AsyncUiForm:
    return AsyncUiForm(
        api_key=uiform_api_key,
        base_url=base_url,
        openai_api_key=api_keys.openai_api_key,
        # claude_api_key=api_keys.claude_api_key,
        # gemini_api_key=api_keys.gemini_api_key,
        # xai_api_key=api_keys.xai_api_key,
        max_retries=3,
    )


@pytest.fixture(scope="session")
def test_data_dir() -> str:
    """Return the path to the test data directory"""
    return os.path.join(TEST_DIR, "data")


@pytest.fixture(scope="session")
def booking_confirmation_json_schema(test_data_dir: str) -> dict[str, Any]:
    schema_path = os.path.join(test_data_dir, "freight", "booking_confirmation_schema_small.json")
    with open(schema_path) as f:
        return json.load(f)


@pytest.fixture(scope="session")
def booking_confirmation_file_path(test_data_dir: str) -> str:
    return os.path.join(test_data_dir, "freight", "booking_confirmation.jpg")


@pytest.fixture(scope="session")
def booking_confirmation_bytes(booking_confirmation_file_path: str) -> bytes:  # Not Working!
    with open(booking_confirmation_file_path, "rb") as f:
        return f.read()


@pytest.fixture(scope="session")
def booking_confirmation_io_bytes(booking_confirmation_file_path: str) -> IO[bytes]:  # Not Working!
    with open(booking_confirmation_file_path, "rb") as f:
        return f


@pytest.fixture(scope="session")
def company_json_schema() -> dict[str, Any]:
    class CompanyEnum(str, Enum):
        school = 'school'
        investor = 'investor'
        startup = 'startup'
        corporate = 'corporate'

    class CompanyRelation(str, Enum):
        founderBackground = 'founderBackground'
        investor = 'investor'
        competitor = 'competitor'
        client = 'client'
        partnership = 'partnership'

    class Company(BaseModel):
        name: str = Field(..., description="Name of the identified company", json_schema_extra={"X-FieldPrompt": "Look for the name of the company, or derive it from the logo"})
        type: CompanyEnum = Field(..., description="Type of the identified company", json_schema_extra={"X-FieldPrompt": "Guess the type depending on slide context"})
        relationship: CompanyRelation = Field(
            ...,
            description="Relationship of the identified company with the startup from the deck",
            json_schema_extra={"X-FieldPrompt": "Guess the relationship of the identified company with the startup from the deck"},
        )

    return Company.model_json_schema()
