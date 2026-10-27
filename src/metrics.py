#Summan av intäkten för alla ordar
def total_revenue(df):
    return df["revenue"].sum()

#Summan av sålda units för alla ordar
def total_units(df):
    return df["units"].sum()

#funktion för AOV, genomsnittligt ordervärder = Den totala intäkten/antal ordrar
#varje rad i csv data, len (df) ger antal ordrar
def aov(df):
    return total_revenue(df) / len(df)