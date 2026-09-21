# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in week 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next week costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**

The test questions are mainly questions that are made from looking at additional information added in the replies that the original question didn't ask. I want to see if the model can chunk good and look at the replies.
---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**

This goes back to our grounding requirement. We want to be able to get evidence from the source documents rather than general knowledge. It shows how strong the RAG model and could potentially prevent hallucinations.
---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.


**Why this target:**
<!-- What did your distances look like when you set the cutoff in Milestone 4?
     Was there a clean gap, or did the two groups overlap? -->
Again, the model should be grounded to the source documents. It shouldn't use general knowledge to answer questions. If it does, then the RAG model is not working.
---

## 4. Something about your chunks


At least 4 of 5 sampled chunks should contain complete replies or complete related thoughts, without cutting a sentence in half or separating a reply’s useful detail from its explanation.

**Why this target:**

The advice-thread documents are short, but their useful information is spread across several replies. Keeping replies or related thoughts together should make each retrieved chunk easier for the model to understand and cite accurately.

---

## 5. Your choice


For at least 4 of 5 in-corpus questions, the answer should include a specific detail from a reply and accurately mention disagreement or differences in advice when the thread contains them.

**Why this target:**

The advice-thread corpus contains several replies with different opinions or extra details, so an answer should consider every perspective.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     WEEK 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in week 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
