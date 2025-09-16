# Duolingo_bug
This repo demonstrates how streak-tracking logic can fail due to:
- Day-boundary / timezone mismatches
- Missing idempotency on client retries

## Highlights
- Bug repro: streak loss when practicing near midnight in UTC.
- Fix: normalize to user's timezone + enforce idempotency.
- Simple Python demo, runnable with `uvicorn` or standalone.

Why it matters: streak features drive user engagement. Correctness builds trust and retention.
