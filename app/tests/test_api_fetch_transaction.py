
from fastapi.testclient import TestClient


def test_fetch_transaction(client: TestClient, test_fetch_transaction_data: dict, api_url: str) -> None:
    # Given
    payload = test_fetch_transaction_data
    ft_api = api_url + "fetch-transaction"

    # When
    response = client.post(
        ft_api,
        json=payload,
    )

    # Then
    assert response.status_code == 200
    ft_response_data = response.json()
    assert ft_response_data["transactions"]
    assert ft_response_data["errors"] is None
