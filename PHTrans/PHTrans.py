import numpy as np
import gudhi as gd
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
def PHT(dataset,  number_of_trials = 5, max_edge_length = 15):
# Make sure your first argument is a matrix
    if type(dataset) != np.ndarray:
        raise TypeError("The first argument must be a matrix.")
# Create a Rips complex from the dataset
    rips_complex = gd.RipsComplex(points=dataset, max_edge_length=max_edge_length
)
    simplex_tree = rips_complex.create_simplex_tree(max_dimension=3)

# Generate random nonzero column vectors and normalize
    Vector = np.random.uniform(-1,1,(number_of_trials, dataset.shape[1]))
    Vector = normalize(Vector, norm='l2', axis=1)
    for i in range(number_of_trials):
        # Set up filtration function:
        for j in range(dataset.shape[0]):
            simplex_tree.assign_filtration([j], np.dot(dataset[j,:],Vector[i,:]))
        simplex_tree.make_filtration_non_decreasing()
        # generate persistent info
        persistence = simplex_tree.persistence()
        ax = gd.plot_persistence_diagram(persistence)
        ax.set_title("Persistence diagram for vector " + str(i+1))
    plt.show()

