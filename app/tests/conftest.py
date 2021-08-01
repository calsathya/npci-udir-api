from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture()
def api_url() -> str:
    api_server_location = "http://localhost:8001/api/v1/"
    return api_server_location


@pytest.fixture(scope="module")
def test_fetch_transaction_data() -> dict:
    dict_payload = dict(
        transaction_request=dict(
            txn_id="123456789",
            ref_url="",
            type=10,
            sub_type="15",
            mobile_no="1234567890",
            ifsc_code="HDFC00001234",
            card_no="123456789012",
        )
    )
    return dict_payload


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
