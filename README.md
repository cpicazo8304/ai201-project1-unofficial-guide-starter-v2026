# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none, because the grader can't
> read it.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Week 1

## What This Does

I picked the advice threads corpus that answers questions from different perspectives and replies that go against each other. 

## Chunking Strategy

**Chunk size:** 300 characters
**Overlap:** 60 characters

I chose 300 characters because the threads contain several replies that sometimes disagree. Keeping replies in small chunks should help retrieval distinuish between different perspectives instead of combining conflicting advice. I used enough overlap to preserve context when a reply crosses a chunk boundary.

## Sample Chunks
```
======================================================================
Chunk 1  |  source: thread_bike_commute.txt#reply_1#0  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Is a bike worth it for a 20 minute walk commute?

Yeah. Cuts an 18 minute walk to about 6. The thing nobody mentions is storage — covered bike parking exists at three buildings and is full by 9am at all three.
```
```
======================================================================
Chunk 2  |  source: thread_first_gen.txt#reply_2#1  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Anything specific for first-generation students?

The thing I'd say: the unwritten rules are the hard part, not the coursework. Ask about the unwritten rules explicitly. People are happy to explain them and nobody volunteers them.
```
```
======================================================================
Chunk 3  |  source: thread_laptop_specs.txt#reply_3#2  |  produced by: chunker.py::split_documents
======================================================================
THREAD: How much laptop do I actually need for CS courses?

I did two years on an 8GB machine and it was fine until the last project, at which point it very much wasn't. 16 is the answer.
```
```
======================================================================
Chunk 4  |  source: thread_parking.txt#reply_2#1  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Worth getting a parking permit?

Street parking on Verrill is legal and free and unmarked, which is why half the upper years do it.
```
```
======================================================================
Chunk 5  |  source: thread_sleep_schedule.txt#reply_2#1  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Everyone says fix your sleep. Does it actually matter?

The library being open until 2am is a trap. It's a resource, not a schedule.
```

## Sample Answer

**Question:**
```
How wrong is the laundry machine availability app?
```
**Answer:**
```
The laundry machine availability app is wrong about half the time because it reports a machine as free for a few minutes after it finishes before someone actually unloads it (thread_laundry_timing.txt#reply_3).

Sources retrieved: thread_laundry_timing.txt#reply_1, thread_laundry_timing.txt#reply_2, thread_laundry_timing.txt#reply_3
```


**My relevance cutoff:**

I chose the relevance cutoff of 0.5. In terms of the out of corpus questions and the actual in-context questions, there was a big gap (0.4ish and 0.8/0.9ish). However, in terms of the actual chunks I was getting, only the ones 0.4 or lower were good for the question. The rest just matched the wording rather than the semantic context.

| Question | In corpus? | Best distance |
|---|---|---|
| How wrong is the laundry machine availability app? | Yes | 0.3258 |
| Are office hours usually empty? | Yes | 0.348 |
| When do room changes happen? | Yes | 0.4211 |
| Do printing quotas roll over to the next semester? | Yes | 0.3023 |
| What should students applying to graduate programs know before choosing pass/fail? | Yes | 0.218 |
| What is the capital of Mongolia? | No | 0.8990 |
| How do I change the oil in a diesel engine? | No | 0.9047 |
| Who won the 1994 World Cup? | No | 0.8982 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8189 |
| How do I write a for loop in Rust? | No | 0.861 |

## How I Used AI


**1.** I used VS Code CoPilot to fill in the table in Milestone 4 so I wouldn't have to go back and forth copying and pasting. It was able to do the table correctly. At first, it added default distances, but I changed the prompt to not include the distance column since I would be doing that.

**2.** I asked Claude to check over my code for the splitting chunks function. I created the idea, but Claude checked if I was good. I wanted confirmation before moving on. It gave a couple of suggestions, but I didn't include all of them.

---

# Week 2

## Run Log — Before

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 3/5 | 4/5 | 4/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Complete replies in chunks. | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Includes information from two sides (if possible) | 3 of 5 | 2/5 | 2/5 | 2/5 | MISSED |

**Criterion 1** — scored by `scorer.py::retrieval_hit`, which checks whether the
`expects` phrase appears in any retrieved chunk. From the before log:


| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Is a bike worth it for a 20-minute walk commute, including the downsides? | fail | fail | fail |
| Are office hours usually empty? | fail | pass | pass |
| What are the different considerations when changing majors? | pass | pass | pass |
| Which meal plan tier makes sense for students with and without a kitchen? | pass | pass | pass |
| What should students applying to graduate programs know before choosing pass/fail? | pass | pass | pass |

**Criterion 2** — read off the answers in the before log, produced by
`generate.py::answer_from_chunks`. Every one of the fifteen names a file:

```
Based on the provided documents, the considerations when changing majors include:
- Whether the credits you have already taken map onto the requirements of the new major (thread_changing_major.txt#reply_1).
- The direction of the move, as moving within sciences is usually fine, while moving into a science from outside in the third year often results in an extra semester (thread_changing_major.txt#reply_2).
- Consulting the department adviser for the major you want to find out about any exceptions (thread_changing_major.txt#reply_3).
```

**Criterion 3** — `run_eval.py::check_out_of_scope`, straight from the before log:

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.899 | refused |
| How do I change the oil in a diesel engine? | 0.905 | refused |
| Who won the 1994 World Cup? | 0.898 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.819 | refused |
| How do I write a for loop in Rust? | 0.861 | refused |


**Criterion 4** — the five chunks in the Sample Chunks section above, from
`chunker.py::split_documents`. 5 of 5 open with "THREAD: {question} \n\n {reply}".
Here is an example of  `thread_bike_commute.txt#reply_3`:

```
THREAD: Is a bike worth it for a 20 minute walk commute?


Both true. I keep a cheap bike for September to November and walk the rest of the year. Total cost was about $120 for the bike and I don't care what happens to it.
```

**Criterion 5** - answers must include contrasting information. Here is an example in the meal-plan question that includes different perspectives:

```
For students whose building has a kitchen (such as Fenwick), people go down a tier and cook two or three nights, while everywhere else should get the middle tier (thread_meal_plan_tier.txt#reply_1). The highest tier only makes sense if you eat three meals a day in the halls every single day (thread_meal_plan_tier.txt#reply_2).
```

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MISSED | The first two questions were missing information that should have been contained in the answer. |
| 2 | Every answer names a source | MET | The source is included in every answer (no matter if fully right or not). |
| 3 | Gate stops out-of-corpus questions | MET | All of the out-of-corpus questions were refused by gate. |
| 4 | Complete replies in chunks. | MET | Every chunk includes the question plus reply. |
| 5 | Includes information from two sides (if possible) | MISSED | The question on bike commute didn't include the contrasting information of snow affecting bike commute (negative reply). |

**Criterion 5 revision:** I changed three of the questions tested to better target criterion 5. I changed the laundry question with a bike commute question, the room-change question with a major-change comparison, and the printing question with a meal-plan comparison.

## Diagnoses

**Criterion 1**: The answer for the bike commute question expected information on ice and road slat affecting bike commute, but none of the answers included this. One of the replies in the bike commute thread includes this information. So, either the cutoff is too low or the top-k removes meaningful chunks. For the office hours question, doesn't seem to be missing anything. 

**Criterion 5:** The bike commute question doesn't have the contrasting information on the perspective of having a bike during the winter months (snow and road salts can affect the bike). This has the same problem as criterion 1, so the problem lies with top-k or the cutoff.

## The Improvement

**What I changed:** Changed top-k from 3 to 5.

**Why I picked it:**

Given the diagnoses, I mention that certain replies/information were not included even though replies in the threads include the information. So, I wanted to see if it was because the top-k was too narrow and didn't took away meaningful chunks. I could move the relevance cutoff up higher, but this is less likely because higher distances points to chunks less relevant to the query.

### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Complete replies in chunks. | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Includes information from two sides (if possible) | 3 of 5 | 3/5 | 3/5 | 3/5 | MET |

Before, the bike commute question had this answer:

```
Yes, a bike is worth it as it cuts an 18-minute walk down to about 6 minutes, but a downside is that covered bike parking fills up by 9 am at all three buildings that offer it. 

Source: thread_bike_commute.txt#reply_1
```

After the top-k change, the bike commute question had this answer:

```
Yes, a bike can cut an 18-minute walk down to about 6 minutes, but there are several downsides to consider (thread_bike_commute.txt#reply_1). Storage can be an issue because covered bike parking is full by 9 AM (thread_bike_commute.txt#reply_1), salt used on paths between November and March destroys drivetrains in a single season (thread_bike_commute.txt#reply_2), and bikes run the risk of being taken, though free campus registration can help recover them (thread_bike_commute.txt#reply_4). 

Sources: thread_bike_commute.txt#reply_1, thread_bike_commute.txt#reply_2, and thread_bike_commute.txt#reply_4
```

**Did it help?**

The change did help by including more information of all the perspectives to a question. It led to a more structured answer that grabbed all important information in the corpus (with sources attached).

## What's Still Broken

Nothing is broken!

## What I'd Do Differently

I wouldn't change my criterion but I would have definitely created better questions with better expectations. I honestly think that doing the criterion first then the questions would have helped since it would the questions help test out the criterion.