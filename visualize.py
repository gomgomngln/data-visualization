import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")
corr = df.select_dtypes("number").corr()

#MATPLOTLIB
# 1. Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["total_bill"], bins=20, color="steelblue", edgecolor="black")
plt.title("Distribusi Total Bill (Matplotlib)", fontsize=14)
plt.xlabel("Total Bill ($)", fontsize=12)
plt.ylabel("Frekuensi", fontsize=12)
plt.savefig("mpl_histogram.png", dpi=150, bbox_inches="tight")
plt.show()

# 2. Bar chart
plt.figure(figsize=(8, 5))
avg = df.groupby("day", observed=True)["total_bill"].mean()
plt.bar(avg.index, avg.values, color=["#4c72b0", "#55a868", "#c44e52", "#8172b3"])
plt.title("Rata-rata Total Bill per Hari (Matplotlib)", fontsize=14)
plt.xlabel("Hari", fontsize=12)
plt.ylabel("Rata-rata Total Bill ($)", fontsize=12)
plt.show()

# 3. Box plot
plt.figure(figsize=(8, 5))
groups = [g["tip"].values for _, g in df.groupby("day", observed=True)]
plt.boxplot(groups, tick_labels=avg.index)
plt.title("Tip per Hari (Matplotlib)", fontsize=14)
plt.xlabel("Hari", fontsize=12)
plt.ylabel("Tip ($)", fontsize=12)
plt.show()

# 4. Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df["total_bill"], df["tip"], alpha=0.6, color="darkorange")
plt.title("Total Bill vs Tip (Matplotlib)", fontsize=14)
plt.xlabel("Total Bill ($)", fontsize=12)
plt.ylabel("Tip ($)", fontsize=12)
plt.show()

# 5. Heatmap korelasi
plt.figure(figsize=(6, 5))
plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns)
for i in range(len(corr)):
    for j in range(len(corr)):
        plt.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center")
plt.title("Korelasi (Matplotlib)", fontsize=14)
plt.show()

#SEABORN
sns.set_theme(style="whitegrid", palette="Set2")

# 1. Histogram
plt.figure(figsize=(8, 5))
sns.histplot(df, x="total_bill", bins=20, kde=True)
plt.title("Distribusi Total Bill (Seaborn)", fontsize=14)
plt.xlabel("Total Bill ($)", fontsize=12)
plt.ylabel("Frekuensi", fontsize=12)
plt.savefig("sns_histogram.png", dpi=150, bbox_inches="tight")
plt.show()

# 2. Bar chart
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="day", y="total_bill", errorbar=None)
plt.title("Rata-rata Total Bill per Hari (Seaborn)", fontsize=14)
plt.xlabel("Hari", fontsize=12)
plt.ylabel("Rata-rata Total Bill ($)", fontsize=12)
plt.show()

# 3. Box plot
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="day", y="tip")
plt.title("Tip per Hari (Seaborn)", fontsize=14)
plt.xlabel("Hari", fontsize=12)
plt.ylabel("Tip ($)", fontsize=12)
plt.show()

# 4. Scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="time")
plt.title("Total Bill vs Tip (Seaborn)", fontsize=14)
plt.xlabel("Total Bill ($)", fontsize=12)
plt.ylabel("Tip ($)", fontsize=12)
plt.show()

# 5. Heatmap korelasi
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Korelasi (Seaborn)", fontsize=14)
plt.show()