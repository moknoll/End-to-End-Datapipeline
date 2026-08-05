import pandas as pd

def clean_transfer_value(value):

    if pd.isna(value):
        return None

    if isinstance(value, (int, float)):
        return value

    value = str(value).strip()

    if value in ("-", "", "?"):
        return None

    value = (
        value
        .replace("€", "")
        .replace(",", ".")
    )

    try:
        if "Mio." in value:
            return float(
                value.replace("Mio.", "").strip()
            ) * 1_000_000

        if "Tsd." in value:
            return float(
                value.replace("Tsd.", "").strip()
            ) * 1_000

        return float(value)

    except ValueError:
        return None

def clean_height(height: str | None) -> int | None:
    if pd.isna(height):
        return None
    if height is None: 
        return None 
    if height == "-": 
        return None
    height = height.replace("m", "")
    height = height.replace(",", ".")
    return int(float(height) * 100)

def clean_date(date: str |None)-> str |None: 
    if date is None:
        return None
    if date == "-": 
        return None 
    date = pd.to_datetime(date, format="%d.%m.%Y")
    return date

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # create a copy of dataframe
    df = df.copy()

    # clean Unnamed data 
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # transform to snake_case
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # clean numerical Series 
    df["market_value"] = df["market_value"].apply(clean_transfer_value)
    df["signing_fee"] = df["signing_fee"].apply(clean_transfer_value)
    df["height"] = df["height"].apply(clean_height)
    df["dob"] = pd.to_datetime(df["dob"], format="%d.%m.%Y")
    df["contract"] = df["contract"].apply(clean_date)
    df["age"] = df["age"].astype(int)

    df.replace(["-", ""], None, inplace=True)
    
    # delete duplicates 
    df.drop_duplicates(inplace=True)
    return df
