
NO LONGER SUPPORTED
===================

Check out [The Schwimmbad](https://github.com/adrn/schwimmbad) instead.

---------

mpipool
=======

A Python MPI Pool

Minimal workin example
----------------------

See code in `examples/mpipool-demo.py`:

```python
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
```

Execute the script using `mpiexec` or your computer/cluster's MPI execute script, e.g., here we
will use 8 cores: `mpiexec -n 8 python mpipool-demo.py`
