"""
Does an answer count as correct?

`run_eval.py::load_scorer` imports this file if it exists and looks for one
function:

    judge(question, expects, answer, results) -> bool

Uses an LLM to judge whether the answer or resulting chunks contains the expected phrase. Returns True
if it does, False if not.
"""

import os
from dotenv import load_dotenv
import anthropic

def judge(question: str, expects: str, answer: str, results) -> bool:
    """
    True when the answer contains the phrase a correct answer has to contain.

    `results` — the retrieved chunks — is in the signature and unused here on
    purpose. It is what you reach for if you want to separate the two questions
    every RAG eval has to answer: was the right thing retrieved, and did the
    model use it? `retrieval_hit` below is that second scorer, and criterion 1
    in criteria.md is scored with it rather than with this function.
    """
    load_dotenv()
    client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
    prompt = f"Question: {question}\nExpected answer: {expects}\nModel answer: {answer}\n\nDoes the model answer contain the expected answer? Answer 'yes' or 'no' with no preamble or explanation. Just answer 'yes' or 'no'."
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    text = response.content[0].text
    # check if response has yes or no
    if response and text.lower() == "yes":
        return True
    return False


def retrieval_hit(expects: str, results) -> bool:
    """
    True when the expected phrase is in at least one RETRIEVED CHUNK.

    This is the criterion-1 scorer, and it is a different measurement from
    `judge`. A question where this is True and `judge` is False is a generation
    failure; one where both are False is a retrieval failure. Splitting them is
    what makes the week 2 diagnosis a lookup rather than a guess.
    """
    # check through the retrieved chunks to see if any of them contain the expected phrase
    if not expects:
        return False
    load_dotenv()
    client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

    for r in results:
        response = client.messages.create(
            model="claude-sonnet-5",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": f"Expected answer: {expects}\nRetrieved chunk: {r.text}\n\nDoes the retrieved chunk contain the expected answer? Answer 'yes' or 'no' with no preamble or explanation. Just answer 'yes' or 'no'."}
            ]
        )
        text = response.content[0].text
        if response and text.strip().lower() == "yes":
            return True
        
    return False