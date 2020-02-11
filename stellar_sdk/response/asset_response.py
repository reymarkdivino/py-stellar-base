from pydantic import BaseModel, Field

from .common import Link
from ..response.account_response import AccountFlags


class Links(BaseModel):
    toml: Link


class AssetResponse(BaseModel):
    asset_type: str
    asset_code: str
    asset_issuer: str
    paging_token: str
    amount: str
    num_accounts: int
    flags: AccountFlags
    links: Links = Field(None, alias="_links")
