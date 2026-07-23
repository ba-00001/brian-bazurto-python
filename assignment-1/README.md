# Assignment 1 — Python Basics

Week 1 of Python Intro 26.3. This is the submission hub for the assignment.

## Submission links

| Field | Link |
| ------- | ------ |
| **URL1** — Pull request | https://github.com/ba-00001/brian-bazurto-python/pull/1 |
| **URL2** — Video reflection | `VIDEO_URL_HERE` |
| **Mindset Response** | [Asking for Help](#mindset-response--asking-for-help) |

## Required files

| File | What it does |
| ------ | -------------- |
| [../assignment-1.py](../assignment-1.py) | All five sections of the Profile Card Builder |

`assignment-1.py` sits at the repository root because the assignment
instructions say to create the file there through GitHub's web editor. This
folder holds the submission notes that go with it.

## What each section covers

| Section | Concept |
| --------- | --------- |
| 1 | Four basic types (`str`, `int`, `float`, `bool`) printed with `type()` |
| 2 | `input()` plus `int()` conversion to compute an approximate age |
| 3 | Two `float()` inputs multiplied and printed with an f-string |
| 4 | Formatted receipt built from variables only — no `input()` |
| 5 | Mini-project — profile card assembled from five inputs, age computed from birth year |

## How to run

```bash
python3 assignment-1.py
```

Answer each prompt to see the full output.

## Sample output

```
--- Section 1: Variables and Types ---
Alex Rivera <class 'str'>
27 <class 'int'>
5.9 <class 'float'>
True <class 'bool'>

--- Section 4: Formatted Receipt ---
===========================
        RECEIPT
===========================
Item:      Python textbook
Price:     $29.99
Quantity:  2
---------------------------
Total:     $59.98
===========================
```

## Requirements checklist

- [x] Section 1 — one variable of each of the four basic types, printed with `type()`
- [x] Section 2 — name and birth year from `input()`, age computed after `int()` conversion
- [x] Section 3 — two `float()` inputs multiplied, result printed with an f-string
- [x] Section 4 — receipt built from variables, total computed, no `input()`
- [x] Section 5 — profile card from five inputs, age derived rather than asked for
- [ ] Video reflection recorded and linked above
- [x] Mindset response written

## Mindset Response — Asking for Help

> *"Smart questions are a stimulus and a gift."* — Eric S. Raymond

### 1. What's your rule of thumb for when to ask for help and when was a time when you wish you would have asked for help sooner?

My rule is about thirty minutes, but the clock isn't really what I'm watching.
What I'm watching is whether I've learned anything new in that time. If I'm
still coming up with ideas and testing them I'll keep going past an hour,
because that's the part where I'm actually learning to debug. What tells me to
stop is catching myself reading the same error for the fourth time, or running
code I haven't changed and hoping it does something different. Past that point
more time on my own isn't going to produce anything.

The one I wish I'd asked about sooner was the Week 2 setup. The instructions
said to fork the class repo. That didn't really register, because Assignment 1
went into a repo I'd made myself, so I assumed everything did. I spent a while
looking for a `week-2/` folder in a repository that was never going to have one,
and I was fairly sure by then that I'd broken something. It wasn't hard. It was
just wrong, and I never said it out loud, so nobody could correct me. Asking
"does Assignment 2 go in the class repo or the one I made?" would have taken a
minute. Instead it cost me days and is part of why Assignment 2 went in late.
Most of my worst delays have been like that. Not difficult problems, just
assumptions I didn't know I was making.

### 2. What information have you found crucial to include in your questions so that mentors or peers can help answer your questions quicker?

Five things, and I try to get all of them into the first message so there's no
back and forth:

1. What I'm trying to do, not just what's broken. "I'm trying to subtract the
   birth year from the current year" is more use than "line 12 doesn't work."
2. The actual error, pasted in full. Not retyped, not a screenshot of half of
   it. The traceback already tells you the file, the line and what kind of error
   it is.
3. The smallest bit of code that still breaks, rather than my whole file.
4. What I already tried and what it did.
5. Which file, what command I ran, what OS and Python version.

Number 4 is the one people leave out and the one I think matters most. Without
it whoever's helping starts from the top and suggests three things I ruled out
an hour ago, and now we're both wasting time. Number 2 is close behind, because
the real error text is often the whole answer sitting there in plain sight.

What surprised me is how often writing it up in that order solves it before I
send anything. That's literally what happened with the `TypeError` in my Week 2
warmup. I wrote "what I'm trying to do: subtract the birth year" on one line and
`unsupported operand type(s) for -: 'int' and 'str'` on the next and just saw
it. `input()` had given me text. I never sent the message. Apparently making
yourself state the goal separately from the symptom is already a debugging step.

## All assignments

| # | Topic | Submission README | Pull request |
| --- | ------- | ------------------- | -------------- |
| 1 | Python Basics | this page | [brian-bazurto-python#1](https://github.com/ba-00001/brian-bazurto-python/pull/1) |
| 2 | CLI & Professional Environment | [week-2/assignment-2](https://github.com/ba-00001/python-intro-homework/blob/assignment-2/week-2/assignment-2/README.md) | [python-intro-homework#1](https://github.com/ba-00001/python-intro-homework/pull/1) |
| 3 | Control Flow | [week-3/assignment-3](https://github.com/ba-00001/python-intro-homework/blob/assignment-3/week-3/assignment-3/README.md) | [python-intro-homework#2](https://github.com/ba-00001/python-intro-homework/pull/2) |
| 4 | Core Data Structures | [week-4/assignment-4](https://github.com/ba-00001/python-intro-homework/blob/assignment-4/week-4/assignment-4/README.md) | [python-intro-homework#3](https://github.com/ba-00001/python-intro-homework/pull/3) |
| 5 | Iteration & Algorithms | [week-5/assignment-5](https://github.com/ba-00001/python-intro-homework/blob/assignment-5/week-5/assignment-5/README.md) | [python-intro-homework#4](https://github.com/ba-00001/python-intro-homework/pull/4) |

Assignment 1 lives in this repository. Assignments 2 onward live in
[ba-00001/python-intro-homework](https://github.com/ba-00001/python-intro-homework),
a fork of the shared course repository, as the instructions require.
