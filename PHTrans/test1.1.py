import numpy as np
from sklearn.preprocessing import normalize
from PHTrans import PHT
X = np.random.uniform(-10,10, (70,3))
PHT(X)
PHT(X, 2, 10)

