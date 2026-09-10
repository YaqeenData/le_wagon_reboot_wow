import requests
from fastapi import status, HTTPException

URL = "https://owen-wilson-wow-api.onrender.com/wows/random"


def get_wow(movie: str | None = None, year: int | None = None) -> dict:
    params = {}

    if movie is not None:
        params["movie"] = movie

    if year is not None:
        params["year"] = year

    response = requests.get(URL, params=params)

    data = response.json()
    
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No wow found for the given movie and year.",
        )

    return data[0]


if __name__ == "__main__":
    print(get_wow())