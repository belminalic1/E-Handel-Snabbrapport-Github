import pandas as pd

def load_data(path):
    #läser in csv filen från sökväg (data)
    df = pd.read_csv(path)
    # gör om till datum så jag i senare skede kan gruppera efter månad
    df["date"] = pd.to_datetime(df["date"])
    return df

#import pandas as pd använts i genomgång + arbetsblad
#v4, upppgift 7 och uppgift 11, samma som pd.to_numberic
#https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html