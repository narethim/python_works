# Instruction on using `pandas` library

Open `Anaconda cmd` terminal on window or a terminal cmd on Linux

```sh
(base) $ conda env list

# Create environment 'envpandas'
(base) $ conda create -n envpandas python=3.13
(base) $ conda activate envpandas

# Verify python version
(envpandas) $ python -V
Python 3.13.9

(envpandas) $ conda list 
(envpandas) $ conda list | wc -l
35

(envpandas) $ conda env list

# Install additional libraries

(envpandas) $ conda install pandas
(envpandas) $ conda list | wc -l
52

(envpandas) $ conda install numpy
(envpandas) $ conda list | wc -l
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

* A Gentle Introduction to Pandas Data Analysis (on Kaggle)
https://www.youtube.com/watch?v=_Eb0utIRdkw

* Pandas Fundamentals playlist [Pandas Fundamentals](https://www.youtube.com/watch?v=8gGNXQgCmIE&list=PLp0BA-8NZ4bgNDMxQojvn6eg71jaaRaYZ) - Dan Kornas
