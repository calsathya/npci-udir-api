import json
from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger

from app import __version__, schemas
from app.config import settings

from .fetch_transaction import FetchTransactionService
from .schemas.api import fetchtransaction
from .schemas.api.health import Health

api_router = APIRouter()


@api_router.get("/health", response_model=Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = schemas.api.health.Health(
        name=settings.PROJECT_NAME, api_version=__version__
    )

    return health.dict()


@api_router.post(
    "/fetch-transaction", response_model=fetchtransaction.Response, status_code=200
)
async def fetch_transaction(input_data: fetchtransaction.Request) -> Any:
    """
    Fetch Transaction
    """

    #    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))
    ft_request_data = input_data.transaction_request

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Fetching transaction for input: {ft_request_data}")
    results = FetchTransactionService.execute(ft_request_data)
    if results["errors"] is not None:
        logger.warning(f"Fetch transaction error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Fetch transaction results: {results.get('transactions')}")

    return results
