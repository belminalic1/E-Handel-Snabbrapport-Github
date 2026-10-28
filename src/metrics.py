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

#summera intäkt efter kategori, störst först
def revenue_by_category(df):
    return df.groupby("category")["revenue"].sum().sort_values(ascending=False)

#topp 3 kategorier efter intäkt, störst först
def top_categories(df, n=3):
    return revenue_by_category(df).head(n)

#Intäkt per stad, störst först
def revenue_by_city(df):
    return df.groupby("city")["revenue"].sum().sort_values(ascending=False)

