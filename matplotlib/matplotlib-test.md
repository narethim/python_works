# Instruction on using `matplotlib` library

Open `Anaconda cmd` terminal on window or a terminal cmd on Linux

```sh
(base) $ conda env list

# Create environment 'envmatplotlib'
(base) $ conda create -n envmatplotlib python=3.13
(base) $ conda activate envmatplotlib

# Verify python version
(envmatplotlib) $ python -V
Python 3.13.7

(envmatplotlib) $ conda list 
(envmatplotlib) $ conda list | wc -l
35

(envmatplotlib) $ conda env list

# Install additional libraries

(envmatplotlib) $ conda install pandas
(envmatplotlib) $ conda list | wc -l
52

(envmatplotlib) $ conda install numpy
(envmatplotlib) $ conda list | wc -l
52
```

## Go to work area

```sh
# On Linux

cd ~/Desktop/python_work

# On Window

E:
cd Test\python_work

$ python
>>> import pandas as pd
>>> pd.__version__
'2.3.3'
>>> exit()
```

## References

* Matplotlib Fundamentals playlist [Matplotlib Fundamentals](https://www.youtube.com/watch?v=wV3C06ya08E&list=PLp0BA-8NZ4bj0HKsK2ZpDkvHCkayxyp0s) - Dan Kornas
