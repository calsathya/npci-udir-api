from typing import Any, List, Optional

from pydantic import BaseModel


class FetchTransactionInputSchema(BaseModel):
    txn_id: Optional[str]
    ref_url: Optional[str]
    type: Optional[int]
    sub_type: Optional[str]
    mobile_no: Optional[str]
    ifsc_code: Optional[str]
    card_no: Optional[str]


class FetchTransactionOutputSchema(BaseModel):
    org_stan: Optional[str]
    approval_no: Optional[str]
    org_txn_id: Optional[str]
    org_txn_date: Optional[str]
