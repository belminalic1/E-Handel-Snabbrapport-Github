import pandas as pd

def load_data(path):
    #läser in csv filen från sökväg (data)
    df = pd.read_csv(path)
    # gör om till datum så jag i senare skede kan gruppera efter månad
    df["date"] = pd.to_datetime(df["date"])
    return df