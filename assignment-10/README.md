# Assignment 10 — Final Project I

> **The work for this assignment lives in a different repository again.**
> The final project uses its own starter repository, not the weekly homework
> fork. The code and the pull request are in
> [ba-00001/python-intro-final-project](https://github.com/ba-00001/python-intro-final-project),
> a fork of `Code-the-Dream-School/python-intro-final-project`, on the branch
> `week-10-final-project`. This folder is a signpost.

**Go to:** [python-intro-final-project/README.md](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md)

## Submission links

| Field | Link |
| --- | --- |
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-final-project/pull/1 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Mindset Response** | [Information Literacy](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md#mindset-response--information-literacy-week-10) |

## The project

**Country Explorer** — a CLI over live World Bank country data.

| Phase | What it covers |
| --- | --- |
| Phase 1 — Core program | `fetch_data()` with `try`/`except` and a status check; JSON parsed into a list of dicts; all fetching and parsing in dedicated functions |
| Phase 2 — CLI tool | Menu loop with three interactions — name search, region filter sorted by population, and a two-country comparison |

## Files (branch `week-10-final-project`)

| File | What it does |
| --- | --- |
| [main.py](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/main.py) | Entry point — fetching, parsing, and the CLI |
| [requirements.txt](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/requirements.txt) | `requests` and its dependencies |
| [README.md](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | Project title, API used, install and run, CLI interactions |

## Why not REST Countries?

The course recommends `restcountries.com`. It was deprecated during the course
and now answers HTTP `200` with an error body rather than data; v5 requires an
API key. The World Bank API is keyless and carries the same fields.

That substitution became the most useful thing in the project: an endpoint
returning **200 with no data in it** is the clearest possible argument for why
checking `status_code` alone isn't enough, which is why `fetch_data()` validates
the response *shape* as well.

## Commit history

The rubric asks for incremental progress rather than one commit. Week 10 is
three: getting the API working, parsing the data, then adding the CLI.

## Working on it locally

```bash
cd ../python-intro-final-project
git checkout week-10-final-project
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python main.py
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
| 9 | External Libraries & APIs | [week-9/assignment-9](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/README.md) | [python-intro-homework#8](https://github.com/ba-00001/python-intro-homework/pull/8) |
| 10 | Final Project I | this page → [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
| 11 | Final Project II | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
