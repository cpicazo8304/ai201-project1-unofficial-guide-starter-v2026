# Run log — before_revised

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 3 · relevance cutoff: 0.5
- Runs per question: 3, caching off
- When: 2026-09-20 22:09

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Is a bike worth it for a 20-minute walk commute, including the downsides? | fail | fail | fail |
| Are office hours usually empty? | fail | pass | pass |
| What are the different considerations when changing majors? | pass | pass | pass |
| Which meal plan tier makes sense for students with and without a kitchen? | pass | pass | pass |
| What should students applying to graduate programs know before choosing pass/fail? | pass | pass | pass |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.5. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.899 | refused |
| How do I change the oil in a diesel engine? | 0.905 | refused |
| Who won the 1994 World Cup? | 0.898 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.819 | refused |
| How do I write a for loop in Rust? | 0.861 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### Is a bike worth it for a 20-minute walk commute, including the downsides? — run 1

- Best distance: 0.0864 (passed the gate)
- Sources retrieved: thread_bike_commute.txt#reply_1, thread_bike_commute.txt#reply_3, thread_bike_commute.txt#reply_4

```
Yes, a bike is worth it as it cuts an 18-minute walk down to about 6 minutes, but a downside is that covered bike parking fills up by 9 am at all three buildings that offer it. 

Source: thread_bike_commute.txt#reply_1
```

### Is a bike worth it for a 20-minute walk commute, including the downsides? — run 2

- Best distance: 0.0864 (passed the gate)
- Sources retrieved: thread_bike_commute.txt#reply_1, thread_bike_commute.txt#reply_3, thread_bike_commute.txt#reply_4

```
Based on the provided documents, a bike can cut a commute significantly (an 18-minute walk to about 6 minutes), but a major downside is that covered bike parking fills up by 9 AM at all three buildings. 

Source: `thread_bike_commute.txt#reply_1`
```

### Is a bike worth it for a 20-minute walk commute, including the downsides? — run 3

- Best distance: 0.0864 (passed the gate)
- Sources retrieved: thread_bike_commute.txt#reply_1, thread_bike_commute.txt#reply_3, thread_bike_commute.txt#reply_4

```
Yes, a bike is worth it as it cuts an 18-minute walk down to about 6 minutes, but a downside is that covered bike parking fills up by 9 am at all three buildings that have it (thread_bike_commute.txt#reply_1). Additionally, another user notes that keeping a cheap bike (costing about $120) eliminates the worry of what happens to it (thread_bike_commute.txt#reply_3).
```

### Are office hours usually empty? — run 1

- Best distance: 0.3481 (passed the gate)
- Sources retrieved: thread_office_hours_etiquette.txt#reply_2, thread_professor_email.txt#reply_2, thread_professor_email.txt#reply_3

```
Yes, office hours are usually empty. 

Sources: 
- `thread_office_hours_etiquette.txt#reply_2`
- `thread_professor_email.txt#reply_2`
- `thread_professor_email.txt#reply_3`
```

### Are office hours usually empty? — run 2

- Best distance: 0.3481 (passed the gate)
- Sources retrieved: thread_office_hours_etiquette.txt#reply_2, thread_professor_email.txt#reply_2, thread_professor_email.txt#reply_3

```
Yes, office hours are usually empty. 

Sources: 
- `thread_office_hours_etiquette.txt#reply_2`
- `thread_professor_email.txt#reply_2`
- `thread_professor_email.txt#reply_3`
```

### Are office hours usually empty? — run 3

- Best distance: 0.3481 (passed the gate)
- Sources retrieved: thread_office_hours_etiquette.txt#reply_2, thread_professor_email.txt#reply_2, thread_professor_email.txt#reply_3

```
Yes, office hours are usually empty. 

Sources: 
- `thread_office_hours_etiquette.txt#reply_2`
- `thread_professor_email.txt#reply_2`
- `thread_professor_email.txt#reply_3`
```

### What are the different considerations when changing majors? — run 1

- Best distance: 0.4092 (passed the gate)
- Sources retrieved: thread_changing_major.txt#reply_1, thread_changing_major.txt#reply_2, thread_changing_major.txt#reply_3

```
Based on the provided documents, the considerations when changing majors include:
- Whether the credits you have already taken map onto the requirements of the new major (thread_changing_major.txt#reply_1).
- The direction of the move, as moving within sciences is usually fine, while moving into a science from outside in the third year often results in an extra semester (thread_changing_major.txt#reply_2).
- Consulting the department adviser for the major you want to find out about any exceptions (thread_changing_major.txt#reply_3).
```

### What are the different considerations when changing majors? — run 2

- Best distance: 0.4092 (passed the gate)
- Sources retrieved: thread_changing_major.txt#reply_1, thread_changing_major.txt#reply_2, thread_changing_major.txt#reply_3

```
Based on the provided documents, the considerations when changing majors include:
* Whether your credits map onto the new requirements (thread_changing_major.txt#reply_1).
* The direction of the move, as moving within sciences is usually fine, but moving into a science from outside in your third year often requires an extra semester (thread_changing_major.txt#reply_2).
* Consulting the department adviser for the major you want to find out about exceptions (thread_changing_major.txt#reply_3).
```

### What are the different considerations when changing majors? — run 3

- Best distance: 0.4092 (passed the gate)
- Sources retrieved: thread_changing_major.txt#reply_1, thread_changing_major.txt#reply_2, thread_changing_major.txt#reply_3

```
Based on the provided documents, the considerations when changing majors include:
- Whether the credits you have already taken map onto the requirements of the new major (`thread_changing_major.txt#reply_1`).
- The direction of the move, as moving within sciences is usually fine, while moving into a science from outside in the third year often requires an extra semester (`thread_changing_major.txt#reply_2`). 
- Administrative steps, which involve filling out a form and talking to the department adviser for the desired major regarding exceptions (`thread_changing_major.txt#reply_3` and `thread_changing_major.txt#reply_1`).
```

### Which meal plan tier makes sense for students with and without a kitchen? — run 1

- Best distance: 0.3004 (passed the gate)
- Sources retrieved: thread_meal_plan_tier.txt#reply_1, thread_meal_plan_tier.txt#reply_2, thread_meal_plan_tier.txt#reply_3

```
Based on the documents, if your building has kitchenettes (like Fenwick), people go down a tier and cook two or three nights, while everywhere else you should get the middle tier. The highest tier only makes sense if you eat three meals a day in the halls every single day. 

Source: thread_meal_plan_tier.txt (replies 1 and 2)
```

### Which meal plan tier makes sense for students with and without a kitchen? — run 2

- Best distance: 0.3004 (passed the gate)
- Sources retrieved: thread_meal_plan_tier.txt#reply_1, thread_meal_plan_tier.txt#reply_2, thread_meal_plan_tier.txt#reply_3

```
For students whose building has a kitchen (such as Fenwick), people go down a tier and cook two or three nights, while everywhere else should get the middle tier (thread_meal_plan_tier.txt#reply_1). The highest tier only makes sense if you eat three meals a day in the halls every single day (thread_meal_plan_tier.txt#reply_2).
```

### Which meal plan tier makes sense for students with and without a kitchen? — run 3

- Best distance: 0.3004 (passed the gate)
- Sources retrieved: thread_meal_plan_tier.txt#reply_1, thread_meal_plan_tier.txt#reply_2, thread_meal_plan_tier.txt#reply_3

```
Based on the documents, if your building has kitchenettes (like Fenwick), people go down a tier and cook two or three nights, while everywhere else you should get the middle tier. The highest tier only makes sense if you eat three meals a day in the halls every single day. 

Source: `thread_meal_plan_tier.txt`
```

### What should students applying to graduate programs know before choosing pass/fail? — run 1

- Best distance: 0.2181 (passed the gate)
- Sources retrieved: thread_pass_fail.txt#reply_1, thread_pass_fail.txt#reply_3, thread_pass_fail.txt#reply_4

```
Students applying to graduate programs should be careful because some graduate programs require a letter grade for prerequisites, and a "P" grade may not satisfy that requirement (thread_pass_fail.txt#reply_3).
```

### What should students applying to graduate programs know before choosing pass/fail? — run 2

- Best distance: 0.2181 (passed the gate)
- Sources retrieved: thread_pass_fail.txt#reply_1, thread_pass_fail.txt#reply_3, thread_pass_fail.txt#reply_4

```
Students applying to graduate programs should be careful with the pass/fail option, as some programs require a letter grade for prerequisites and a "P" grade will not satisfy this requirement (thread_pass_fail.txt#reply_3).
```

### What should students applying to graduate programs know before choosing pass/fail? — run 3

- Best distance: 0.2181 (passed the gate)
- Sources retrieved: thread_pass_fail.txt#reply_1, thread_pass_fail.txt#reply_3, thread_pass_fail.txt#reply_4

```
Students applying to graduate programs should be careful with the pass/fail option, as some programs require a letter grade for prerequisites and a "P" grade will not satisfy it (thread_pass_fail.txt#reply_3).
```
