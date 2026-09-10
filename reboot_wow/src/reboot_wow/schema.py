from pydantic import BaseModel


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

class WowsResponse(BaseModel):
    """What GET /wows answers"""
    # TODO: count (int) and wows (a LIST of Wow)
    count: int
    wows: list[Wow]

if __name__ == "__main__":
    wow = Wow(movie="Cars", year=2006, character="Lightning", full_line="Wow!")
    print(wow)
    print(wow.movie, wow.year)   # fields are read with a dot, not with ["..."]