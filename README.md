# Assurity Test

This is my attempt to solve the Assurity coding challenge to test the api response of one of its endpoints. This uses a bare minimum set of tools to get the test up and running. It is very readable and easy to modify.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes. The solution  has 3 test cases, mainly:

1. test_name - tests if Name = "Carbon credits"
2. test_relist - tests if CanRelist = true
3. test_promotions - tests is the Promotions element with Name = "Gallery" has a Description that contains the text "2x larger image"

A method get_categories() is being called by each of the test cases to retrieve the category details.

### Prerequisites

Python 2.7
requests (python library - command: pip install requests)  
json (python library - command: pip install json)  
pytest (python library - command: pip install pytest)  
a copy of the test_assurity.py file (git clone https://github.com/jcsia87/assurity.git)

## Running the tests

Simple run the command below in your terminal

```
py.test test_assurity.py
```

pytest implements the following standard test discovery:

* test_ prefixed test functions or methods outside of class
* test_ prefixed test functions or methods inside Test prefixed test classes (without an __init__ method)

A successful test will output a log similar to the one below

```
==================================================================== test session starts =====================================================================
platform linux2 -- Python 2.7.5, pytest-3.7.2, py-1.5.4, pluggy-0.7.1
rootdir: /home/jefferson/Desktop, inifile:
plugins: tavern-0.17.2
collected 3 items                                                                                                                                            

test_assurity.py ...                                                                                                                                   [100%]

================================================================== 3 passed in 7.87 seconds ==================================================================
```

## Built With

* [Python](https://www.python.org/) - The programming language used
* [pytest](https://docs.pytest.org/en/latest/getting-started.html) - Test Runner
