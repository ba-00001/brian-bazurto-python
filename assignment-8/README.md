# Assignment 8 — Errors & Debugging

[← Course index (all 11 assignments)](../README.md)

> **The work for this assignment lives in another repository.**
> From Week 2 the course moves to a fork of the shared homework repository, so
> the code and the pull request are in
> [ba-00001/python-intro-homework](https://github.com/ba-00001/python-intro-homework),
> not here. This folder is a signpost.

**Go to:** [week-8/assignment-8/README.md](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/README.md)

## Submission links

| Field | Link |
| --- | --- |
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-homework/pull/7 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Video script** | [VIDEO-SCRIPT.md](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/VIDEO-SCRIPT.md) |
| **Mindset Response** | [Problem Solving](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/README.md#mindset-response--problem-solving) |

## Files (all in the other repository, branch `assignment-8`)

| File | What it does |
| --- | --- |
| [warmup1.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/warmup1.py) | Loop re-asking until `float()` succeeds, catching `ValueError` |
| [warmup2.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/warmup2.py) | `ZeroDivisionError` and `ValueError` handled separately, success in `else` |
| [warmup3.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/warmup3.py) | `FileNotFoundError` caught, with the traceback quoted in a comment |
| [warmup4.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/warmup4.py) | Imports `requests` from the venv, prints its version |
| [requirements.txt](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/requirements.txt) | Real `pip freeze` — `requests` plus its four dependencies |
| [mini_project.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/mini_project.py) | Defensive CSV Reader — per-row `try`/`except`, extra-column guard, summary report |

The mini-project puts the `try` **inside** the row loop, not around it: one bad
row costs one row instead of abandoning the remaining eleven. Extra columns are
a guard rather than an `except`, because `DictReader` files surplus fields under
the `None` key without raising anything.

## Working on it locally

```bash
cd ../python-intro-homework
git checkout assignment-8
cd week-8/assignment-8
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## All assignments

| # | Topic | Submission README | Pull request |
| --- | --- | --- | --- |
| 1 | Python Basics | [assignment-1/](../assignment-1/README.md) | [brian-bazurto-python#1](https://github.com/ba-00001/brian-bazurto-python/pull/1) |
| 2 | CLI & Professional Environment | [week-2/assignment-2](https://github.com/ba-00001/python-intro-homework/blob/assignment-2/week-2/assignment-2/README.md) | [python-intro-homework#1](https://github.com/ba-00001/python-intro-homework/pull/1) |
| 3 | Control Flow | [week-3/assignment-3](https://github.com/ba-00001/python-intro-homework/blob/assignment-3/week-3/assignment-3/README.md) | [python-intro-homework#2](https://github.com/ba-00001/python-intro-homework/pull/2) |
| 4 | Core Data Structures | [week-4/assignment-4](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/README.md) | [python-intro-homework#3](https://github.com/ba-00001/python-intro-homework/pull/3) |
| 5 | Iteration & Algorithms | [week-5/assignment-5](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/README.md) | [python-intro-homework#4](https://github.com/ba-00001/python-intro-homework/pull/4) |
| 6 | Functions & Scope | [week-6/assignment-6](https://github.com/ba-00001/python-intro-homework/blob/assignment-6/week-6/assignment-6/README.md) | [python-intro-homework#5](https://github.com/ba-00001/python-intro-homework/pull/5) |
| 7 | Text Data & Modules | [week-7/assignment-7](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/README.md) | [python-intro-homework#6](https://github.com/ba-00001/python-intro-homework/pull/6) |
| 8 | Errors & Debugging | this page → [week-8/assignment-8](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/README.md) | [python-intro-homework#7](https://github.com/ba-00001/python-intro-homework/pull/7) |
| 9 | External Libraries & APIs | [week-9/assignment-9](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/README.md) | [python-intro-homework#8](https://github.com/ba-00001/python-intro-homework/pull/8) |
| 10 | Final Project I | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
| 11 | Final Project II | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
