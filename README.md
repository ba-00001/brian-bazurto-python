# Brian Bazurto — Python Assignments

Coursework for **Python Intro 26.3 — Pilot** (Code the Dream).

## Assignment index

There is one folder here per assignment. Assignment 1's folder holds the real
work; Assignments 2–11 are signposts, because from Week 2 the course requires
the work to live in a fork of a shared repository (see below).

**Submission README** is the page to link from CTD Learns — it holds the pull
request link, the video reflection link, the file list, sample output, the
mindset response, and a requirements checklist.

| # | Topic | Folder here | Submission README | Pull request |
| --- | --- | --- | --- | --- |
| 1 | Python Basics | [assignment-1/](assignment-1/README.md) | [assignment-1/README.md](assignment-1/README.md) | [brian-bazurto-python#1](https://github.com/ba-00001/brian-bazurto-python/pull/1) |
| 2 | CLI & Professional Environment | [assignment-2/](assignment-2/README.md) | [week-2/assignment-2](https://github.com/ba-00001/python-intro-homework/blob/assignment-2/week-2/assignment-2/README.md) | [python-intro-homework#1](https://github.com/ba-00001/python-intro-homework/pull/1) |
| 3 | Control Flow | [assignment-3/](assignment-3/README.md) | [week-3/assignment-3](https://github.com/ba-00001/python-intro-homework/blob/assignment-3/week-3/assignment-3/README.md) | [python-intro-homework#2](https://github.com/ba-00001/python-intro-homework/pull/2) |
| 4 | Core Data Structures | [assignment-4/](assignment-4/README.md) | [week-4/assignment-4](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/README.md) | [python-intro-homework#3](https://github.com/ba-00001/python-intro-homework/pull/3) |
| 5 | Iteration & Algorithms | [assignment-5/](assignment-5/README.md) | [week-5/assignment-5](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/README.md) | [python-intro-homework#4](https://github.com/ba-00001/python-intro-homework/pull/4) |
| 6 | Functions & Scope | [assignment-6/](assignment-6/README.md) | [week-6/assignment-6](https://github.com/ba-00001/python-intro-homework/blob/assignment-6/week-6/assignment-6/README.md) | [python-intro-homework#5](https://github.com/ba-00001/python-intro-homework/pull/5) |
| 7 | Text Data & Modules | [assignment-7/](assignment-7/README.md) | [week-7/assignment-7](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/README.md) | [python-intro-homework#6](https://github.com/ba-00001/python-intro-homework/pull/6) |
| 8 | Errors & Debugging | [assignment-8/](assignment-8/README.md) | [week-8/assignment-8](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/README.md) | [python-intro-homework#7](https://github.com/ba-00001/python-intro-homework/pull/7) |
| 9 | External Libraries & APIs | [assignment-9/](assignment-9/README.md) | [week-9/assignment-9](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/README.md) | [python-intro-homework#8](https://github.com/ba-00001/python-intro-homework/pull/8) |
| 10 | Final Project I | [assignment-10/](assignment-10/README.md) | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
| 11 | Final Project II | [assignment-11/](assignment-11/README.md) | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |

## Three repositories

Assignment 1 was submitted here, in a personal repository, as the Week 1
instructions specify. The course then moves twice:

| Scope | Repository | Branch pattern |
| --- | --- | --- |
| Assignment 1 | this repo — `ba-00001/brian-bazurto-python` | `assignment-1` |
| Assignments 2–9 | [ba-00001/python-intro-homework](https://github.com/ba-00001/python-intro-homework) — fork of `Code-the-Dream-School/python-intro-homework` | `assignment-N`, work in `week-N/assignment-N/` |
| Assignments 10–11 | [ba-00001/python-intro-final-project](https://github.com/ba-00001/python-intro-final-project) — fork of the final-project starter | `week-10-final-project` |

Weeks 10 and 11 share one branch and one pull request: Week 11 extends the
Week 10 project rather than replacing it, and the rubric asks for the combined
commit history across both weeks.

## Assignment 1 — Python Basics

`assignment-1.py` contains all five required sections of the Profile Card
Builder:

1. Variables and types
2. User input and math
3. Type conversion and f-strings
4. A formatted receipt
5. A formatted profile card

Run it with:

```bash
python3 assignment-1.py
```

Answer each prompt to see the complete output. See
[assignment-1/README.md](assignment-1/README.md) for the full write-up.

## Final project — Country Explorer

Assignments 10 and 11 build one program: a CLI over live World Bank country
data, with name search, region ranking, two-country comparison, and a cleaned
CSV export (Week 11, Option B).

The course recommended `restcountries.com`, which was **deprecated during the
course** — it now returns HTTP `200` with an error body instead of data, and its
v5 replacement requires an API key. Assignments 9–11 use the keyless World Bank
API instead. Details are in each assignment README.

## A note on video reflections

Every assignment requires a 3–5 minute video reflection (2–4 minutes for
Assignment 11). Those are recorded separately and each submission README has a
`VIDEO_URL_HERE` placeholder to fill in.
