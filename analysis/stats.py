import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import os

def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)

    df['price'] = df['price'].astype(str).str.replace('Â', '', regex=False)
    df['price'] = df['price'].str.replace('£', '', regex=False)


    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df.dropna(subset=['price'])
    df['price'] = df['price'].astype(float)
    return df

def describe_prices(df: pd.DataFrame) -> pd.Series:
    return df['price'].describe()

def price_clustering(df: pd.DataFrame, n_clusters=3):
    X = df[['price']]
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    df['price_cluster'] = model.fit_predict(X)
    return df

def summary_by_cluster(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('price_cluster')['price'].describe()

def plot_price_histogram(df: pd.DataFrame, filename="data/histogram_price.png"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.figure(figsize=(8, 6))
    plt.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
    plt.title("Histogramme des prix")
    plt.xlabel("Prix (£)")
    plt.ylabel("Nombre de produits")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def plot_price_boxplot(df: pd.DataFrame, filename="data/boxplot_price.png"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.figure(figsize=(6, 8))
    plt.boxplot(df['price'], vert=True)
    plt.title("Boxplot des prix")
    plt.ylabel("Prix (£)")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def plot_price_clusters(df: pd.DataFrame, filename="data/clustering_price.png"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if 'price_cluster' not in df.columns:
        raise ValueError("Run price_clustering() before plotting clusters.")
    plt.figure(figsize=(10, 6))
    plt.scatter(df.index, df['price'], c=df['price_cluster'], cmap='viridis', alpha=0.6)
    plt.title("Scatter plot des prix par cluster")
    plt.xlabel("Index")
    plt.ylabel("Prix (£)")
    plt.colorbar(label='Cluster')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def plot_cluster_distribution(df: pd.DataFrame, filename="data/cluster_boxplot.png"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    if 'price_cluster' not in df.columns:
        raise ValueError("Run price_clustering() before plotting cluster distribution.")
    plt.figure(figsize=(8, 6))
    df.boxplot(column='price', by='price_cluster', grid=False)
    plt.title("Distribution des prix par cluster")
    plt.suptitle("")
    plt.xlabel("Cluster")
    plt.ylabel("Prix (£)")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
