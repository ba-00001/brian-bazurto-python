# Assignment 11 — Final Project II

> **The work for this assignment lives in a different repository again.**
> Week 11 extends the Week 10 project on the same branch, in
> [ba-00001/python-intro-final-project](https://github.com/ba-00001/python-intro-final-project).
> This folder is a signpost.

**Go to:** [python-intro-final-project/README.md](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md)

## Submission links

| Field | Link |
| --- | --- |
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-final-project/pull/1 |
| **URL2** — Video demo (2–4 min) | `VIDEO_URL_HERE` |
| **Extension track** | **Option B — Data Cleaning & CSV Export** |
| **Mindset Response** | [Self-Motivation](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md#mindset-response--self-motivation-week-11) |

## The extension

**Option B** — clean the API data and export it to a structured CSV with
`csv.DictWriter`, added as menu option 4 in the existing CLI.

| File | What it does |
| --- | --- |
| [export.py](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/export.py) | All extension logic — the cleaning framework and the CSV writer |
| [countries_clean_2026-09-02.csv](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/countries_clean_2026-09-02.csv) | Sample export — 217 countries |
| [main.py](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/main.py) | Wires the export in as menu option 4 |

Kept in its own module rather than added to `main.py`, because cleaning and
exporting is a separate job from fetching and browsing.

## Data cleaning decisions

The export applies a **per-field** decision framework — the answer to "what
does missing mean here" deliberately differs by field:

| Field | Missing / invalid | Decision |
| --- | --- | --- |
| `name` | empty or absent | **DROP the record** |
| `region` | empty or `Aggregates` | **DROP the record** |
| `population` | `0`, `None`, non-numeric, negative | **DROP the record** |
| `capital` | `""` or the sentinel `"N/A"` | **KEEP**, write `""` |
| `income_level` | `""` or absent | **KEEP**, write `Not classified` |

The three DROP fields are what the export exists to carry — a row with no name
can't be identified, no region can't be grouped, no population can't be ranked.
`capital` and `income_level` are descriptive: their absence is a real fact about
the country, not a broken row.

The full write-up, including type coercion and why `0` is treated as missing, is
in the [project README](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md#data-cleaning-decisions).

## Standard library beyond `csv`

`os.path` (`os.path.join` for the output path) and `datetime` (a dated output
filename, so re-running the export doesn't overwrite the previous file).

## Working on it locally

```bash
cd ../python-intro-final-project
git checkout week-10-final-project
source .venv/bin/activate
python main.py     # choose option 4 to export
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
| 10 | Final Project I | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
| 11 | Final Project II | this page → [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
