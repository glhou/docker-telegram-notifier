import datetime
from typing import Annotated

from fastapi import APIRouter, Query
from pydantic import BaseModel

dashboard_router = APIRouter(prefix="/dashboard", tags=["dashboard"])


class Timespan(BaseModel):
    start_time: datetime.datetime = datetime.datetime.now(
        datetime.UTC
    ) - datetime.timedelta(days=7)
    end_time: datetime.datetime = datetime.datetime.now(datetime.UTC)


@dashboard_router.get("/stats")
def get_dashboard_stats(time: Annotated[Timespan, Query()]): ...
