# mpipool-demo.py

# Standard library
import sys
import numpy as np
from mpipool import MPIPool

def worker(task):
    x,y = task
    return 5*x + y**2

def main():

    # Initialize the MPI pool
    pool = MPIPool()

    # Make sure only we run map() on the master process
    if not pool.is_master():
        pool.wait()
        sys.exit(0)

    # create some random input data
    x = np.random.uniform(size=10000)
    y = np.random.uniform(size=10000)
    tasks = np.vstack((x,y)).T

    vals = pool.map(worker, tasks)

    pool.close()

if __name__ == "__main__":
    main()
