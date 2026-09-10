from fastapi import FastAPI

from src.reboot_wow.fetch import get_wow
from src.reboot_wow.storage import save_wow
from src.reboot_wow.schema import Wow, IngestResponse
from src.reboot_wow.storage import save_wow, read_wows
from src.reboot_wow.schema import Wow, IngestResponse, WowsResponse

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/ingest", response_model=IngestResponse)
def ingest() -> IngestResponse:
    wow = get_wow()          # 1. get the data
    path = save_wow(wow)     # 2. save it
    # TODO: return an IngestResponse with success=True, saved_to=path, wow=Wow(**wow)
    return IngestResponse(success=True, saved_to=path, wow=Wow(**wow))

@app.get("/wows", response_model=WowsResponse)
def wows(movie: str | None = None) -> WowsResponse:
    # TODO 1: rows = read_wows(movie)
    rows = read_wows(movie)
    # TODO 2: return a WowsResponse with count=len(rows) and wows=rows
    return WowsResponse(count=len(rows), wows=rows)

