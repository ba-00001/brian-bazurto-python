# Assignment 4 — Core Data Structures

> **The work for this assignment lives in another repository.**
> From Week 2 the course moves to a fork of the shared homework repository, so
> the code and the pull request are in
> [ba-00001/python-intro-homework](https://github.com/ba-00001/python-intro-homework),
> not here. This folder is a signpost.

**Go to:** [week-4/assignment-4/README.md](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/README.md)

## Submission links

| Field | Link |
| --- | --- |
| **URL1** — Pull request | https://github.com/ba-00001/python-intro-homework/pull/3 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Mindset Response** | [Curiosity to Learn](#mindset-response--curiosity-to-learn) |

## Files (all in the other repository, branch `assignment-4`)

| File | What it does |
| --- | --- |
| [warmup1.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/warmup1.py) | List of 8 numbers — first, last by negative index, middle-four slice, reversed. No loops. |
| [warmup2.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/warmup2.py) | Student dictionary printed with `.items()`, then a `graduated` key added |
| [warmup3.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/warmup3.py) | Two language lists as sets — union, intersection, difference |
| [mini_project.py](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/mini_project.py) | Student Roster Analyzer — top scorer, class average, unique subjects, high scorers |

The `students` list is copied verbatim from `week-4/data/roster.py`; the file in
`data/` is untouched.

## Working on it locally

```bash
cd ../python-intro-homework
git checkout assignment-4
cd week-4/assignment-4
```

## Mindset Response — Curiosity to Learn

> *"Stay hungry. Stay foolish."* — Steve Jobs

### 1. What's one thing that you were curious to learn more about recently (this doesn't need to be coding-related)? How did you learn more about it?

How people actually remember vocabulary in a new language. I'd been picking at a
language learning project and realised I'd built the whole thing on an
assumption I'd never checked — that if repetition works, then more repetition
works better. Turns out that isn't really true.

I went reading and ended up on spaced repetition and the forgetting curve. The
gist is that reviewing something right before you'd have forgotten it is far
more efficient than reviewing it constantly. Cramming feels productive because
recall is easy while it's all fresh, and that ease is exactly the problem.

Then I stopped reading about it and tried it, which is where I actually learned
anything. I ran a deck on myself for a few weeks. What surprised me is how bad
doing it properly feels. You're supposed to be reviewing at the point where you
can only just about recall something, so a lot of the time it feels like
failing. The version that feels good is the one that doesn't work.

Which lines up with the Developer Tea episode. What feels like it's working and
what's actually working aren't the same thing, and you can't tell from the
inside without testing it.

### 2. What's one best practice you've learned in your first few weeks at CTD that you don't know "the why" behind? How can you find out "the why"?

Making a branch for every assignment and merging it with a pull request. I do it
because I've been told to. I can repeat the reasons — keeps work separate, lets
people review it, gives you a way back — but I've never run into the problem
it's solving. I'm one person in my own repo. Nobody reviews my pull request
before it merges. Committing straight to `main` would get me to exactly the same
place with fewer steps. So right now it feels like performing a ritual correctly
without knowing what it's for.

Three ways I could find out. Easiest is asking a mentor what actually goes wrong
on a team without it. An actual thing that happened, not the textbook answer,
because the textbook answer is the bit I've already got.

Second is causing the problem on purpose in a throwaway repo. Two branches
editing the same lines, merge both, sit with the conflict. I suspect this only
makes sense once you've felt what it stops.

Third is carrying on until I need it. At some point I'll wreck something on a
branch and be very glad `main` was untouched, and that one moment will probably
teach me more than any explanation has.

I'd rather understand it before that happens. But I'd also rather keep doing it
while I don't understand it than drop it for feeling pointless. Not getting the
point of a rule yet isn't much of a reason to stop following it.

## All assignments

| # | Topic | Submission README | Pull request |
| --- | --- | --- | --- |
| 1 | Python Basics | [assignment-1/](../assignment-1/README.md) | [brian-bazurto-python#1](https://github.com/ba-00001/brian-bazurto-python/pull/1) |
| 2 | CLI & Professional Environment | [week-2/assignment-2](https://github.com/ba-00001/python-intro-homework/blob/assignment-2/week-2/assignment-2/README.md) | [python-intro-homework#1](https://github.com/ba-00001/python-intro-homework/pull/1) |
| 3 | Control Flow | [week-3/assignment-3](https://github.com/ba-00001/python-intro-homework/blob/assignment-3/week-3/assignment-3/README.md) | [python-intro-homework#2](https://github.com/ba-00001/python-intro-homework/pull/2) |
| 4 | Core Data Structures | this page → [week-4/assignment-4](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/README.md) | [python-intro-homework#3](https://github.com/ba-00001/python-intro-homework/pull/3) |
| 5 | Iteration & Algorithms | [week-5/assignment-5](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/README.md) | [python-intro-homework#4](https://github.com/ba-00001/python-intro-homework/pull/4) |
