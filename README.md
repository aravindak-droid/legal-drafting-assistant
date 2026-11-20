# Legal Drafting Assistant

[![Built with askThili](https://ask.thili.ai/api/v1/public/projects/jfxg2gyzwz/badge.svg)](https://ask.thili.ai/b/jfxg2gyzwz)

This project creates a Legal Drafting Assistant designed for paralegals. It leverages an n-gram model to suggest the next word in legal sentences and integrates a fine-tuned GPT-2 model to classify these sentences into specific clause types, streamlining the drafting process.

## What you are building

**Goal.** You will build a Legal Drafting Assistant that uses an n-gram model to predict next words for drafting simple legal sentences and a fine-tuned GPT-2 model to instantly classify these sentences into clause types.

**Done when.** Your assistant can generate legal sentences using n-gram prediction from a prepared corpus and then classify the generated text into clause types using the fine-tuned GPT-2 model, all accessible via a command-line interface.

## Milestones

Tick these off as you go, and commit after each one.

- [ ] **1. Prepare a small legal text corpus for n-gram training.**  
      Hint: Use techniques from 'Build a Next-Word Predictor from Scratch' to process your corpus.
- [ ] **2. Implement the n-gram next-word predictor.**  
      Hint: Apply the n-gram model logic from 'Build a Next-Word Predictor from Scratch' to predict words.
- [ ] **3. Load the pre-trained GPT-2 model and fine-tuned adapter for legal clause tagging.**  
      Hint: Load the models as described in 'Fine-Tune GPT-2 to Tag Legal Contract Clauses'.
- [ ] **4. Create a CLI interface to generate text and then classify the generated text.**  
      Hint: Design a user-friendly command-line interface to interact with both models.
- [ ] **5. Evaluate classification accuracy on example clauses.**  
      Hint: Compare your model's predictions to a set of known clause types, similar to evaluation in 'Fine-Tune GPT-2 to Tag Legal Contract Clauses'.

## Run it

You need Python 3.12 and git.

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then choose a model; see the comments inside
python -m app.cli hello
pytest
```

Your work goes in `app/core.py` (one stub per milestone) and `tests/test_core.py`. The first tests pass already; they
check the plumbing.

## Settings and secrets

Model settings live in `.env`, which is ignored by git. **Never commit `.env` or paste a key into code.** If a key ever
reaches GitHub, treat it as leaked and make a new one.

## Stretch ideas

- Implement smoothing techniques for the n-gram model to handle unseen word combinations more gracefully.
- Add functionality to save and load generated sentences, allowing paralegals to review and edit their drafts.
- Explore integrating more advanced text generation techniques beyond simple n-gram prediction.
