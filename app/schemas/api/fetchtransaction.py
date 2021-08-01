from typing import Any, List, Optional

from pydantic import BaseModel

from app.schemas.json.fetchtransaction import (
    FetchTransactionInputSchema,
    FetchTransactionOutputSchema,
)


class Response(BaseModel):
    errors: Optional[Any]
    version: str
    transactions: Optional[List[FetchTransactionOutputSchema]]


class Request(BaseModel):
    transaction_request: FetchTransactionInputSchema

    class Config:
        schema_extra = {
            "example": {
                "transaction_request": {
                    "txn_id": "123456789",
                    "ref_url": "",
                    "type": 10,
                    "sub_type": "15",
                    "mobile_no": "1234567890",
                    "ifsc_code": "HDFC00001234",
                    "card_no": "123456789012",
                }
            }
        }
