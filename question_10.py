from sklearn.neighbors import KNeighborsClassifier
import numpy as np

if __name__ == "__main__":
    neigh = KNeighborsClassifier(n_neighbors=3)
    X = [[1], [2], [3], [6], [6], [7], [10], [11]]
    y = [1, 1, 2, 2, 2, 1, 1, 1]

    X_train, X_test = np.array_split(X, 2)
    y_train, y_test = np.array_split(y, 2)

    neigh.fit(X_train, y_train)

    print("Predicted: "+str(neigh.predict(X_test)))
    print("Actual" + str(y_test))

