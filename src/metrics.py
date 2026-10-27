#Summan av intäkten för alla ordar
def total_revenue(df):
    return df["revenue"].sum()

#Summan av sålda units för alla ordar
def total_units(df):
    return df["units"].sum()