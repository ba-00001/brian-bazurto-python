# Assignment 1 — Video Reflection Script

**Target length:** 3–5 minutes (this script runs ~4:30 spoken at a normal pace).
**Setup:** screen share of the repository and the terminal, webcam in the corner
for the intro and the closing. Run the program once, live, before recording so
the terminal is warm and you know your own answers.

**Before you hit record**

- Open two tabs: the repo on the `assignment-1` branch, and pull request #1.
- Open `assignment-1.py` in the editor, scrolled to the top.
- Have a terminal open in the repo folder, cleared.
- Decide your five profile answers ahead of time so you are not thinking on camera:
  hometown, hobby, fun fact, birth year, and the two numbers for Section 3.

---

## 0:00 – 0:25 · Intro (webcam)

> Hey, I'm Brian Bazurto, and this is my reflection for Assignment 1 of Python
> Intro 26.3 with Code the Dream. This week was Python basics — variables,
> types, `input()`, type conversion, and f-strings — and the assignment was a
> Profile Card Builder in five sections. I'm going to walk you through the repo,
> then the code, then run it, and finish with the mindset question on asking for
> help.

*(Switch to screen share.)*

---

## 0:25 – 1:00 · The repository (screen: GitHub)

> Here's the repo — `ba-00001/brian-bazurto-python`. Week 1 asks for the work in
> a personal repo, so that's what this is. I'm on the `assignment-1` branch, not
> `main`, and the pull request from that branch into `main` is pull request
> number one — that's the URL1 link on my submission.

*(Click the `assignment-1` folder.)*

> `assignment-1.py` sits at the repository root, because the instructions say to
> create it there through GitHub's web editor. This `assignment-1/` folder next
> to it is my submission README — the links, the file list, the sample output,
> the requirements checklist, and the mindset response, all in one page so my
> reviewer isn't hunting for anything.

---

## 1:00 – 1:20 · Section 1 — variables and types (screen: editor)

*(Scroll to Section 1.)*

> Section 1 is one variable of each of the four basic types: `name` is a string,
> `age` is an int, `height` is a float, and `is_student` is a bool. I print the
> value next to `type()` for each one, and that's the part I actually wanted to
> see, because it makes it obvious that `27` and `"27"` are not the same thing to
> Python. That distinction is the whole rest of the assignment.

---

## 1:20 – 1:55 · Section 2 — input and math

*(Scroll to Section 2, highlight the `int(birth_year)` line.)*

> Section 2 is where that bites. I ask for a birth year with `input()`, and
> `input()` always hands back a string — even when the person typed digits. So
> `birth_year` is the text `"1998"`, not the number. If I subtract it straight
> from `current_year` I get:
>
> `TypeError: unsupported operand type(s) for -: 'int' and 'str'`
>
> I hit that error for real, and the fix is `int()` around it, which converts the
> text to a number so the subtraction is legal. Then I print with an f-string —
> the `f` before the quote lets me drop variables straight into the text inside
> curly braces instead of gluing strings together with plus signs.

*(Point at `current_year = 2026` at the top of the file.)*

> One thing I did on purpose: `current_year` is defined once at the top, because
> two sections calculate an age. If I'd hardcoded the year in both places I'd
> eventually update one and forget the other.

---

## 1:55 – 2:20 · Section 3 — float conversion

> Section 3 is the same idea with `float()` instead of `int()`, because these two
> should accept decimals. Reading it inside out: `input()` asks and returns text,
> `float()` converts it. Then I multiply them — and because they're real numbers
> now, `*` actually multiplies. If they were still strings this would either fail
> or do something strange. Small thing I noticed: type in a whole number like 4
> and it prints back as `4.0`, because `float()` made it a decimal.

---

## 2:20 – 2:45 · Section 4 — the receipt

> Section 4 has no `input()` at all — everything comes from variables, and the
> total is calculated from `price` and `quantity` rather than typed in, so
> changing the price up here updates the receipt without me touching the print
> lines.

*(Highlight `${price:.2f}`.)*

> The formatting detail I care about is `:.2f`. It forces exactly two decimal
> places, so a price of `30.0` prints as `$30.00` instead of `$30.0`, which would
> look broken for money.

---

## 2:45 – 3:25 · Section 5 — run it live (screen: terminal)

> Section 5 pulls all of it together. Let me just run it.

```bash
python3 assignment-1.py
```

*(Answer the prompts as you go — narrate lightly, don't read every prompt aloud.)*

> Five questions — name, hometown, hobby, fun fact, birth year. The assignment
> says to work the age out rather than ask for it, so I take the birth year and
> subtract. And there's the card.

*(Let the finished profile card sit on screen for a couple of seconds.)*

> The labels are padded to the same width so the values all start in the same
> column — that's just f-strings and spacing, but it's the difference between
> output that looks deliberate and output that looks like a pile of prints.

---

## 3:25 – 4:10 · Mindset — asking for help (webcam or screen)

> The mindset question was about when to ask for help. My rule of thumb is around
> thirty minutes, but the clock isn't really what I'm watching — what I'm
> watching is whether I've learned anything new in that time. If I'm still coming
> up with ideas and testing them, I'll keep going, because that's the part where
> I'm actually learning to debug. What tells me to stop is catching myself
> reading the same error for the fourth time.
>
> The one I wish I'd asked about sooner was the Week 2 setup. The instructions
> said to fork the class repo, and that didn't register, because Assignment 1
> went in a repo I made myself, so I assumed everything did. I spent a while
> looking for a `week-2/` folder in a repository that was never going to have
> one. It wasn't hard. It was just wrong, and I never said it out loud, so nobody
> could correct me. Asking "does Assignment 2 go in the class repo or the one I
> made?" would have taken a minute.
>
> And on what to put in a question — the one people leave out is what you already
> tried and what it did. Without that, whoever's helping starts from the top and
> suggests three things you ruled out an hour ago. Writing it up in that order
> actually solved my `TypeError` before I sent anything: I wrote down the goal on
> one line, the error on the next, and just saw it. `input()` had given me text.

---

## 4:10 – 4:30 · Close (webcam)

> So that's Assignment 1. The thing I'm taking forward is that most of my bugs
> this week weren't logic — they were type bugs, text pretending to be a number.
> Thanks for watching, and everything's linked in the submission README.

---

## Delivery notes

- Say the `TypeError` message out loud, slowly. Graders listen for whether you
  understand it or just pasted the fix.
- Don't read the code line by line. Say what it does and why you chose it.
- If you fumble a sentence, pause two seconds and say it again — easy to cut.
- Under 3:00 reads as thin; over 5:00 gets cut off. Time your first take.

---

## Video URL

Upload to YouTube (unlisted) or Loom, then paste the link here and in the two
other places it is needed.

**Video URL:** `VIDEO_URL_HERE`

| Also paste it into | Where |
| --- | --- |
| Submission README `URL2` row | [assignment-1/README.md](README.md) |
| Pull request description | [brian-bazurto-python#1](https://github.com/ba-00001/brian-bazurto-python/pull/1) |
| Course index video table | [main README](https://github.com/ba-00001/brian-bazurto-python/blob/main/README.md#video-reflections) |
