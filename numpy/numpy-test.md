# Instruction on using `numpy` library

Open `Anaconda cmd` terminal on window or a terminal cmd on Linux

```sh
(base) $ conda env list

# Create environment 'envnumpy'
(base) $ conda create -n envnumpy python=3.13
(base) $ conda activate envnumpy

# Verify python version
(envnumpy) $ python -V
Python 3.13.9

(envnumpy) $ conda list 
(envnumpy) $ conda list | wc -l
35

(envnumpy) $ conda env list

# Install additional libraries

(envnumpy) $ conda install pandas
(envnumpy) $ conda list | wc -l
52

(envnumpy) $ conda install numpy
(envnumpy) $ conda list | wc -l
52

# Install 'Jupyter Notebook'
(envmatplotlib) $ conda install notebook

(envmatplotlib) $ jupyter notebook

# Install 'JupyterLab'
(envmatplotlib) $ conda install jupyterlab

(envmatplotlib) $ jupyter lab
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

* Numpy Fundamentals playlist [Numpy Fundamentals](https://www.youtube.com/watch?v=6Ry1tWJG0l0&list=PLp0BA-8NZ4biK_2tRCEFTIe7HOMMKFIMD) - Dan Kornas
