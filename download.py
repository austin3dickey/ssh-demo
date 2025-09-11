import pathlib
from urllib.request import urlretrieve

URL_TEMPLATE = (
    "https://ursa-labs-taxi-data.s3.us-east-2.amazonaws.com/{year}/{month}/data.parquet"
)
DATA_DIR = pathlib.Path("data")


def download_data():
    """Downloads all the nyctaxi files into ./data/

    Will not overwrite any files that exist.
    """
    DATA_DIR.mkdir(exist_ok=True)

    for year in range(2009, 2020):
        local_dir = DATA_DIR / str(year)
        local_dir.mkdir(exist_ok=True)

        for month in range(1, 13):
            monthstr = str(month).zfill(2)
            local_path = local_dir / f"{year}-{monthstr}.parquet"
            print(f"Downloading {local_path}")

            try:
                if local_path.exists():
                    raise RuntimeError("it exists already")
                urlretrieve(
                    url=URL_TEMPLATE.format(year=year, month=monthstr),
                    filename=local_path,
                )
            except Exception as e:
                print(f"Could not download {local_path} due to: {e}")


if __name__ == "__main__":
    download_data()
