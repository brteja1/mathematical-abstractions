# Human comprehension trial — not yet performed

Choose one anonymous packet per case, read its TASK.md and relevant artifacts,
then answer questions.md. Record elapsed time, confidence and file/line evidence
in responses.csv. Leave accuracy to a reviewer using the contract. Do not read
the arm key, aggregate report or the other packet before submitting answers.
Use opposite packet orders across readers. A reader who sees both variants
learns from the first; disclose that effect. Labels conceal paths and metadata,
but content such as catalog references may still suggest the arm.

These packets are prepared materials, not measured human readability results.
The suite author's quality scores are editorial judgments, not a blind trial.

## Anonymous packets

| Case | Packet A | Packet B | Questions |
| --- | --- | --- | --- |
| Calendar | [spec](case-10/A/spec.md), [code](case-10/A/calendar_api.py), [tests](case-10/A/test_calendar.py) | [spec](case-10/B/spec.md), [code](case-10/B/calendar_api.py), [tests](case-10/B/test_calendar.py) | [A](case-10/A/questions.md), [B](case-10/B/questions.md) |
| Scheduler | [test plan](case-11/A/test-plan.md), [tests](case-11/A/test_scheduler.py) | [test plan](case-11/B/test-plan.md), [tests](case-11/B/test_scheduler.py) | [A](case-11/A/questions.md), [B](case-11/B/questions.md) |
| Quota | [spec](case-12/A/spec.md) | [spec](case-12/B/spec.md) | [A](case-12/A/questions.md), [B](case-12/B/questions.md) |
