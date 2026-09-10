import os
import pandas as pd

CSV_PATH = "data/wows.csv"
COLUMNS = ["movie", "year", "character", "full_line"]

def save_wow(wow):
    os.makedirs("data", exist_ok=True)      # create data/ if it does not exist
    df = pd.DataFrame([wow])[COLUMNS]      # TODO 1: one dict -> a DataFrame of 1 row,
                                            #         keeping only our 4 columns
    file_exists = os.path.exists(CSV_PATH)  # True from the 2nd run on
    df.to_csv(CSV_PATH, mode="a", header=not file_exists, index=False)   # TODO 2
    return CSV_PATH

def read_wows(movie=None):
    if not os.path.exists(CSV_PATH):
        return []
    df = pd.read_csv(CSV_PATH)
    # TODO 1: if movie is not None, keep only the rows where the "movie" column equals movie
    if movie is not None:
        df = df[df["movie"] == movie]
    # TODO 2: return the DataFrame as a list of dictionaries -> df.to_dict(orient="records")
    return df.to_dict(orient="records")

if __name__ == "__main__":
    from src.reboot_wow.fetch import get_wow

    wow = get_wow()
    print("saved to ->", save_wow(wow))