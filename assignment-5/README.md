# Assignment 5 — Iteration & Algorithms

[← Course index (all 11 assignments)](../README.md)

> **The work for this assignment lives in another repository.**
> From Week 2 the course moves to a fork of the shared homework repository, so
> the code and the pull request are in
> [ba-00001/python-intro-homework](https://github.com/ba-00001/python-intro-homework),
> not here. This folder is a signpost.

**Go to:** [week-5/assignment-5/README.md](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/README.md)

## Submission links

| Field | Link |
| --- | --- |
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-homework/pull/4 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Video script** | [VIDEO-SCRIPT.md](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/VIDEO-SCRIPT.md) |
| **Mindset Response** | [Comfort with the Unknown](#mindset-response--comfort-with-the-unknown) |

## Files (all in the other repository, branch `assignment-5`)

| File | What it does |
| --- | --- |
| [warmup1.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/warmup1.py) | Sums 1 to 100 with a `for` loop over `range()` |
| [warmup2.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/warmup2.py) | `while` loop re-asks until a positive integer arrives, using `try`/`except` |
| [warmup3.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/warmup3.py) | Linear search by hand — no `.index()`, no membership operator |
| [warmup4.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/warmup4.py) | FizzBuzz 1–30, combined case checked first |
| [mini_project.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/mini_project.py) | Number Cruncher — menu loop with hand-written min, max, search, and bubble sort |

The `numbers` list is copied verbatim from `week-5/data/numbers.py`; the file in
`data/` is untouched.

## Working on it locally

```bash
cd ../python-intro-homework
git checkout assignment-5
cd week-5/assignment-5
```

## Mindset Response — Comfort with the Unknown

> *"An entrepreneur is someone who jumps off a cliff and builds a plane on the
> way down."* — Reid Hoffman

### 1. So far in class, have you had any "aha" moments? What have you enjoyed the most? What has been the hardest?

The clearest one was small. `input()` always gives you text back, even when the
person typed a number. I got `TypeError: unsupported operand type(s) for -:
'int' and 'str'` and sat there annoyed, because I *had* typed a number. When it
landed, a lot of other things landed with it. Types are a real thing and not a
technicality, and the error was an accurate description of what I'd asked for
rather than Python being difficult about it.

The other one was the `swapped` flag in bubble sort. I got the swapping straight
away and the stopping part not at all, until it clicked that the algorithm works
out for itself when it's finished. A whole pass with no swaps is what sorted
means. Nothing is counting the passes. That's the first bit of code that struck
me as clever rather than just working.

Enjoyed most: the mini-projects, and particularly the menu loop in the Number
Cruncher. Watching a program keep going, take an instruction, do it and come
back for the next one was the first thing I'd written that behaved like an
actual program instead of something that prints and quits.

Hardest, by a distance, was not the Python. It was Git and GitHub. I lost real
time to not understanding that Assignment 2 moves into a fork of the class repo
rather than the personal one from Week 1, and went hunting for folders in a
repository that never had them. The language has been fine. It's everything
around the language I've struggled with.

### 2. What were you excited/worried about before class started?

Excited about finally getting some foundation under things I'd been building by
copying. I've put projects together out of examples before and they hold up
right until they don't, and I wanted to stop being stranded at that point.

Worried about time more than anything. Not whether I'd understand the material,
but whether I'd reliably find the hours for it. That turned out to be the right
thing to worry about — I fell behind in Weeks 2 and 3 and handed both in late.
Not because they were hard. Because catching up takes longer than keeping up,
which is obvious now and apparently needed learning the hard way.

I was also a bit worried about being the slowest person in the cohort. I've
mostly stopped keeping score on that. It never once helped.

### 3. How do you feel about what's still to come in this class and in your journey ahead?

Alright, with the caveat that the later weeks build on the earlier ones and I've
already shown I can slip. Functions and scope is next, and I can see from my own
code — the same block copied three times in the Number Cruncher — that I'm about
to be handed the fix for something I could already tell was wrong. That's a good
way to learn something.

What's changed most is how not knowing something feels. Early on, hitting
something I didn't understand felt like proof I shouldn't be here. Now it mostly
just feels like the job. The thing I don't get today is the same shape as the
thing I didn't get a couple of weeks ago and do now.

Further out I'm not planning much on purpose. Finish this properly, get one of
my own projects actually done rather than abandoned, and see what that opens up.
Building the plane on the way down is a slightly dramatic way to put it, but it
isn't far off, and I'd rather be doing that than still stood on the edge working
out whether to.

## All assignments

| # | Topic | Submission README | Pull request |
| --- | --- | --- | --- |
| 1 | Python Basics | [assignment-1/](../assignment-1/README.md) | [brian-bazurto-python#1](https://github.com/ba-00001/brian-bazurto-python/pull/1) |
| 2 | CLI & Professional Environment | [week-2/assignment-2](https://github.com/ba-00001/python-intro-homework/blob/assignment-2/week-2/assignment-2/README.md) | [python-intro-homework#1](https://github.com/ba-00001/python-intro-homework/pull/1) |
| 3 | Control Flow | [week-3/assignment-3](https://github.com/ba-00001/python-intro-homework/blob/assignment-3/week-3/assignment-3/README.md) | [python-intro-homework#2](https://github.com/ba-00001/python-intro-homework/pull/2) |
| 4 | Core Data Structures | [week-4/assignment-4](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/README.md) | [python-intro-homework#3](https://github.com/ba-00001/python-intro-homework/pull/3) |
| 5 | Iteration & Algorithms | this page → [week-5/assignment-5](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/README.md) | [python-intro-homework#4](https://github.com/ba-00001/python-intro-homework/pull/4) |
| 6 | Functions & Scope | [week-6/assignment-6](https://github.com/ba-00001/python-intro-homework/blob/assignment-6/week-6/assignment-6/README.md) | [python-intro-homework#5](https://github.com/ba-00001/python-intro-homework/pull/5) |
| 7 | Text Data & Modules | [week-7/assignment-7](https://github.com/ba-00001/python-intro-homework/blob/assignment-7/week-7/assignment-7/README.md) | [python-intro-homework#6](https://github.com/ba-00001/python-intro-homework/pull/6) |
| 8 | Errors & Debugging | [week-8/assignment-8](https://github.com/ba-00001/python-intro-homework/blob/assignment-8/week-8/assignment-8/README.md) | [python-intro-homework#7](https://github.com/ba-00001/python-intro-homework/pull/7) |
| 9 | External Libraries & APIs | [week-9/assignment-9](https://github.com/ba-00001/python-intro-homework/blob/assignment-9/week-9/assignment-9/README.md) | [python-intro-homework#8](https://github.com/ba-00001/python-intro-homework/pull/8) |
| 10 | Final Project I | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
| 11 | Final Project II | [python-intro-final-project](https://github.com/ba-00001/python-intro-final-project/blob/week-10-final-project/README.md) | [python-intro-final-project#1](https://github.com/ba-00001/python-intro-final-project/pull/1) |
