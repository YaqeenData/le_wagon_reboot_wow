from pydantic import BaseModel
from pydantic import Field


class Wow(BaseModel):
    movie: str
    year: int
    # TODO: add character (str) and full_line (str)
    character: str
    full_line: str


class IngestResponse(BaseModel):
    """What POST /ingest answers"""
    success: bool
    saved_to: str
    wow: Wow          # <-- a schema can be used as a type!
    success: bool = Field(..., description="Did the pipeline run without error")

class WowsResponse(BaseModel):
    """What GET /wows answers"""
    # TODO: count (int) and wows (a LIST of Wow)
    count: int
    wows: list[Wow]
    
class StatsResponse(BaseModel):
    """What GET /stats answers"""
    # TODO: implement stats response
    year_counts: dict[str, int]  # a dictionary with years as keys and counts as values

class IngestRequest(BaseModel):
    """What POST /ingest expects"""
    movie: str | None = None  # optional movie name to filter the ingested wow
    year: int | None = None  # optional year to filter the ingested wow


if __name__ == "__main__":
    wow = Wow(movie="Cars", year=2006, character="Lightning", full_line="Wow!")
    print(wow)
    print(wow.movie, wow.year)   # fields are read with a dot, not with ["..."]