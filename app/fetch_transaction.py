from typing import Any

from loguru import logger

from app import __version__
from app.config import settings
from app.schemas.api import fetchtransaction
from app.schemas.json.fetchtransaction import (
    FetchTransactionInputSchema,
    FetchTransactionOutputSchema,
)


class FetchTransactionService:
    def __init__():
        pass

    def execute(request_data: FetchTransactionInputSchema):
        response_data = dict(errors=None, version=__version__, transactions=[])
        response_data["transactions"] = [
            dict(
                org_stan="123456",
                approval_no="app12378",
                org_txn_id="txn567823",
                org_txn_date="13-07-20",
            )
        ]
        return response_data
