This repository includes lecture/lab materials for COM3523/6523 Software Reengineering at the University of Sheffield.

# Refactoring

## Setup

```bash
pip install -r requirements.txt
```

## Task1: Check the existing tests and add more if necessary

Before refactoring, you need to check the existing tests in `tests/test_main.py` and ensure that they are working as expected.
```bash
python -m unittest tests/test_main.py
```

Also, by looking at the tests in `tests/test_main.py`, you can see how the code in `main.py` is expected to behave.

If you run the following code, you can check the test coverage of `main.py`:
```bash
coverage run -m unittest tests/test_main.py && coverage html && open htmlcov/main_py.html
```

If you find that the test coverage is not sufficient, you need to add more tests to improve the coverage.


## Task2: Apply appropriate refactoring techniques to the code

If you look at the code in `main.py`, you can see that it is not ideal.
Apply appropriate refactoring techniques to improve the code quality.

The following list of refactoring techniques might be useful:
- Extract Function
- Inline Function
- Extract Variable
- Inline Variable
- Rename Variable
- Decompose Conditional
- Parametrise Function
- Move Function
- Move Field

## Mini Report

After completing the above task, push the changes to the repository and include a short report to summarise what you have done for the task. 

Your discussions/reflections are also recommended. For example, you can discuss the following points:
- What refactoring techniques did you apply?
- What was the reason for applying these techniques?
- How do you know that observable behaviour has not changed after refactoring?
- What are the (potential) benefits and drawbacks of applying these techniques?
- Overall, how do you feel about the refactoring process? Worth it? Why (or why not)?

On the report's front page, please record below who participated in this week's exercise submissions:

- NAME (brief description of the role)
- NAME (brief description of the role)
...

**Important**: Please add the report as `mini-report.pdf` in the root directory.