import matplotlib.pyplot as plt


# stapeldiagram intäkt per kategori
def plot_revenue_by_category(revenue):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(revenue.index, revenue.values / 1_000_000)
    ax.set_title("Intäkt per kategori")
    ax.set_xlabel("Kategori")
    ax.set_ylabel("Intäkt (miljoner kr)")
    ax.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    return fig