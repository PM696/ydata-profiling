from pathlib import Path

import pandas as pd

from ydata_profiling import ProfileReport
from ydata_profiling.utils.cache import cache_file

if __name__ == "__main__":
    file_name = cache_file(
        "nza_01_DBC.csv", "https://www.opendisdata.nl/download/csv/01_DBC.csv"
    )

    df = pd.read_csv(file_name, low_memory=False)
    df["JAAR"] = pd.to_datetime(df["JAAR"], format="%Y")

    logo_string = "data:image/png;base64,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"

    profile = ProfileReport(
        df,
        title="DBC-Zorgproducten per jaar, specialisme, diagnose",
        html={"style": {"logo": logo_string}},
    )
    profile.to_file(output_file=Path("./nza_report.html"))
