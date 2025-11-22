# Chapter 11 - Testing Your Code

## Preparation

```sh
chapter_11$ python -m venv chapter11-env
source chapter11-env/bin/activate
(chapter11-env) chapter_11$ pip list

(chapter11-env) chapter_11$ pip install --upgrade pip

(chapter11-env) chapter_11$ pip list

(chapter11-env) chapter_11$ pip install pytest

(chapter11-env) chapter_11$ pip list

(chapter11-env) chapter_11$ pip freeze > requirements.txt
```

Install packages from the `requirements.txt`

```sh
chapter_11$ python -m venv chapter11-env2
chapter_11$ source chapter11-env2/bin/activate

(chapter11-env2) chapter_11$ pip install --upgrade pip
(chapter11-env2) chapter_11$ pip install -r requirements.txt
(chapter11-env2) chapter_11$ pip list
```

## Run the test

### Passing test

```sh
(chapter11-env) chapter_11$ pytest
======================================================= test session starts ========================================================
platform linux -- Python 3.13.8, pytest-9.0.1, pluggy-1.6.0
rootdir: /home/nim/Desktop/python_work/chapter_11
collected 1 item                                                                                                                   

test_name_function.py .                                                                                                      [100%]

======================================================== 1 passed in 0.03s =========================================================
```

### Failing test

```sh
(chapter11-env) chapter_11$ pytest
======================================================= test session starts ========================================================
platform linux -- Python 3.13.8, pytest-9.0.1, pluggy-1.6.0
rootdir: /home/nim/Desktop/python_work/chapter_11
collected 1 item                                                                                                                   

test_name_function.py .                                                                                                      [100%]

======================================================== 1 passed in 0.03s =========================================================
```