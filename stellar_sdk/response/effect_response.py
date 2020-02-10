from datetime import datetime

from pydantic import BaseModel, Field

from .common import Link


class Links(BaseModel):
    operation: Link
    succeeds: Link
    precedes: Link


class EffectResponse(BaseModel):
    id: str
    paging_token: str
    account: str
    type: str
    type_i: int
    created_at: datetime
    links: Links = Field(None, alias="_links")