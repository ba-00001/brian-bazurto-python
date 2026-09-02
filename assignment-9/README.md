# Assignment 9 — External Libraries & APIs

> **The work for this assignment lives in another repository.**
> From Week 2 the course moves to a fork of the shared homework repository, so
> the code and the pull request are in
> [ba-00001/python-intro-homework](https://github.com/ba-00001/python-intro-homework),
> not here. This folder is a signpost.

**Go to:** [week-9/assignment-9/README.md](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/README.md)

## Submission links

| Field | Link |
| --- | --- |
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-homework/pull/8 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Mindset Response** | [Accessibility](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/README.md#mindset-response--accessibility) |

## ⚠️ API substitution

The assignment specifies `restcountries.com/v3.1`. **That API was deprecated
during the course** — it now returns HTTP `200` with a deprecation notice
instead of country data, and its v5 replacement requires an API key, so it is
no longer a keyless public API.

Warmup 3 and the mini-project use the **World Bank API** instead: keyless, no
registration, and it carries all four required fields. Warmups 1 and 2 still
use Agify exactly as specified. The full rationale is in the assignment README.

## Files (all in the other repository, branch `assignment-9`)

| File | What it does |
| --- | --- |
| [warmup1.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/warmup1.py) | `requests.get()` on Agify; prints status code and full JSON |
| [warmup2.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/warmup2.py) | Fields by key, plus `.get()` with a fallback for the absent `birthday` |
| [warmup3.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/warmup3.py) | Loops a JSON list of countries in one region, first 10 only |
| [warmup4.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/warmup4.py) | `except requests.exceptions.RequestException` plus a non-200 status check |
| [mini_project.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/mini_project.py) | Country Explorer CLI — menu loop, name search, region filter, two endpoints joined |
| [requirements.txt](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/requirements.txt) | `requests` and its dependencies |

**A bug worth recording.** The first version joined the two endpoints on
`row["country"]["id"]` and every population came out `0`. Both endpoints have a
field called `id`, but they hold different identifiers — ISO3 in one, a World
Bank code in the other. Joining on the wrong one matched nothing and failed
*silently*, because `.get(key, 0)` did exactly what it was told. A default value
stops a crash and can hide that the lookup never worked.

## Working on it locally

```bash
cd ../python-intro-homework
git checkout assignment-9
cd week-9/assignment-9
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
| 8 | Errors & Debugging | [week-8/assignment-8](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/README.md) | [python-intro-homework#7](https://github.com/ba-00001/python-intro-homework/pull/7) |
| 9 | External Libraries & APIs | this page → [week-9/assignment-9](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/README.md) | [python-intro-homework#8](https://github.com/ba-00001/python-intro-homework/pull/8) |
| 10 | Final Project I | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
| 11 | Final Project II | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
