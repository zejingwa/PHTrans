# PHTrans.py
The package computes persistent homology transform (PHT) of a point cloud. It plots persistence diagrams for visualization.
## Installation
Install the package using `pip`:

```bash
pip install PHTrans
```
## Persistent homology transform
[This paper](https://arxiv.org/pdf/1310.1030) defines persistent homology transform. In brief, the inputs of the transform contain a simplicial complex $$K$$ in $$R^n$$ and a unit vector in $$R^n$$, while its output is persistent homology of $$\{K_n\}$$ whose filtration is determined by the unit vector.
## Function
Our main function below visualizes persistent homology transform for an input data set 
```bash
def PHT(dataset,  number_of_trials = 5, max_edge_length = 15):
```
The function verifies that the first argument `dataset` is a 2D array. 
```bash
if type(dataset) != np.ndarray:
    raise TypeError("The first argument must be a matrix.")
```
Given a dataset of data type 2D array, we first convert it to a simplicial complex by the package `Gudhi`. The input argument `max_edge_length` is a `float` that determines the complex. 

Then we generate random unit vectors, the number of which is the `int` argument `number_of_trials`.

Finally, the function returns plots of persistent diagrams that visualizes PHT, the number of which is equal to `number_of_trials`. Each random unit vector corresponds to each plot. See the section Example at the end.
## How to run
Import the package as below:
```bash
from PHTrans import PHT
```
After you extract a 2D array $$X$$ from a data set, decide values for `number_of_trials` and `max_edge_length`. The command line is as follows:
```bash
PHT(X, number_of_trials, max_edge_length)
```
Or if you want to take the values at default:
```bash
PHT(X)
```
## Example
In the [test file](https://github.com/zejingwa/PHTrans/blob/main/PHTrans/test1.1.py), we generate a random set of 70 points in 3D by
```bash
X = np.random.uniform(-10,10, (70,3))
```
It generates 5 + 2 = 7 diagrams. See [images](https://github.com/zejingwa/PHTrans) in the folder.


