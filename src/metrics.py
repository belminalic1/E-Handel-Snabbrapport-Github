#Summan av intäkten för alla ordar, v4 uppgift 9
def total_revenue(df):
    return df["revenue"].sum()

#Summan av sålda units för alla ordar, v4 uppgift 9
def total_units(df):
    return df["units"].sum()

#funktion för AOV, genomsnittligt ordervärder = Den totala intäkten/antal ordrar, v4 uppgift 10
#varje rad i csv data, len (df) ger antal ordrar
def aov(df):
    return total_revenue(df) / len(df)

#summera intäkt efter kategori, störst först, v4 uppgift 8, 12 och 17
def revenue_by_category(df):
    return df.groupby("category")["revenue"].sum().sort_values(ascending=False)

#topp 3 kategorier efter intäkt, störst först, v4 7 och 8
def top_categories(df, n=3):
    return revenue_by_category(df).head(n)

#Intäkt per stad, störst först, v4 8, 12 och 17
def revenue_by_city(df):
    return df.groupby("city")["revenue"].sum().sort_values(ascending=False)

# Summera intäkt per månad, göra om datum till månad för att ta reda på försäljning över tid månadsvis, v4 uppgift 12 och 17
def revenue_by_month(df):
    return df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
