from pydantic import BaseModel

from .common import Price


class TradesAggregationResponse(BaseModel):
    """Represents trade data aggregation over a period of time.
    """
    base_volume: str
    counter_volume: str
    avg: str
    high: str
    high_r: Price
    low: str
    low_r: Price
    open: str
    open_r: Price
    close: str
    close_r: Price
    timestamp: int
    trade_count: int
