import matplotlib.pyplot as plt
#använt tidigare i v4

# stapeldiagram intäkt per kategori, v4 uppgift 18
#Dokumentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html + google
def plot_revenue_by_category(revenue):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(revenue.index, revenue.values / 1_000_000)
    ax.set_title("Intäkt per kategori")
    ax.set_xlabel("Kategori")
    ax.set_ylabel("Intäkt (miljoner kr)")
    ax.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    return fig

#Linjediagram intäkt per månad, ändra till månad och tusen kr. y axel börjar från 0. V4 uppgift 18-20.
#Dokumentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
def plot_revenue_by_month(revenue):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(revenue.index.astype(str), revenue.values / 1_000, marker="o")
    ax.set_title("Intäkt per månad")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Intäkt (tusen kr)")
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig
