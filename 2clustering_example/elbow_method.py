import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import h5py
from sklearn.cluster import KMeans, DBSCAN
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np


def visualize_elbow(vectors):
    #print(vectors)
    wcss = []
    for i in range(1,30):
        kmeans=KMeans(i)
        kmeans.fit(vectors)
        wcss.append(kmeans.inertia_)
    #print(wcss)
    plt.plot(range(1,30),wcss)
    plt.xlabel("Número de clusters (K)")
    plt.ylabel("Valor de la función de coste (J)")
    plt.show()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--vectors", required=True, help="HDF5 file containing the vectors")
    args = parser.parse_args()
    path = args.vectors

    with h5py.File(path, "r") as f:
        vectors = f["vectors"][:]

    visualize_elbow(vectors)
