# Assignment 7 — Text Data & Modules

[← Course index (all 11 assignments)](../README.md)

> **The work for this assignment lives in another repository.**
> From Week 2 the course moves to a fork of the shared homework repository, so
> the code and the pull request are in
> [ba-00001/python-intro-homework](https://github.com/ba-00001/python-intro-homework),
> not here. This folder is a signpost.

**Go to:** [week-7/assignment-7/README.md](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/README.md)

## Submission links

| Field | Link |
| --- | --- |
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-homework/pull/6 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Video script** | [VIDEO-SCRIPT.md](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/VIDEO-SCRIPT.md) |
| **Mindset Response** | [Debugging](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/README.md#mindset-response--debugging) |

## Files (all in the other repository, branch `assignment-7`)

| File | What it does |
| --- | --- |
| [warmup1.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/warmup1.py) | Reads `notes.txt` in a `with` block, numbering lines with `enumerate` |
| [warmup2.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/warmup2.py) | `csv.DictReader` over `students.csv`, fields accessed by header name |
| [warmup3.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/warmup3.py) | `os.getcwd()`, `os.path.exists()` guard, `os.path.join()` |
| [warmup4.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/warmup4.py) | `datetime.now()` and `.strftime()` |
| [mini_project.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/mini_project.py) | Expense Report Generator — guard, `DictReader`, `float()`, filter, total, file write |
| [food_report.txt](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/food_report.txt) | The generated output — 5 Food expenses, $185.65 total |

Written as `build_report(category)` rather than hardcoding `"Food"`, so the
optional any-category extension is covered by the same code.

## Working on it locally

```bash
cd ../python-intro-homework
git checkout assignment-7
cd week-7/assignment-7
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
| 7 | Text Data & Modules | this page → [week-7/assignment-7](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/README.md) | [python-intro-homework#6](https://github.com/ba-00001/python-intro-homework/pull/6) |
| 8 | Errors & Debugging | [week-8/assignment-8](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/README.md) | [python-intro-homework#7](https://github.com/ba-00001/python-intro-homework/pull/7) |
| 9 | External Libraries & APIs | [week-9/assignment-9](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/README.md) | [python-intro-homework#8](https://github.com/ba-00001/python-intro-homework/pull/8) |
| 10 | Final Project I | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
| 11 | Final Project II | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
