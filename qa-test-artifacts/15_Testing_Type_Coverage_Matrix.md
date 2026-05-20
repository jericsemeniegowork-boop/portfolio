# Testing Type Coverage Matrix Across Portfolio Case Studies

I created this artifact to map common QA testing types across three representative case studies: Purchase Request workflow, fictional online western game patch testing, and Banking account balance validation.

| Testing Type | Purchase Request Case | Fictional Game Patch Case | Banking Case |
|---|---|---|---|
| Functional | Create, submit, approve, reject, status update, read-only behavior | Treasure reward claim, Wildlife Research samples, Open-World Mission launch, stable entry, mount recall | Login, MFA, account overview, balance display, logout |
| UI / Visual | Required labels, disabled fields, confirmations, status chips | Reward screen, map marker, stable menu, public name labels, voice chat setting | Balance cards, masked account display, error messages, negative balance display |
| Security / Access Control | Requester cannot approve own request; unauthorized user blocked | Server rejects duplicate reward claims and invalid chest interactions | Unauthorized URL blocked; MFA/session/logout/token behavior |
| Privacy | Request details only visible to permitted roles | Custom crew and mount names not publicly visible after patch | Account number masking and no sensitive data in URLs/logs/errors |
| Internationalization | Currency/date questions if global | Regional/session behavior if supported | Country access rules, currency, date, decimal format, IP/risk behavior |
| Localization | Translated validation/status text if multilingual | Reward, mission, and settings strings in supported languages | Supported languages, long strings, RTL if supported, translated errors |
| Accessibility | Keyboard flow, focus order, contrast, clear errors | Menu prompts, captions/subtitles, readable reward summaries | Screen reader labels, keyboard-only flow, contrast, non-color-only errors |
| Performance | Save, submit, approve, list refresh response | Stable load, session load, long session stability, crash checks | Login/account overview load, mobile 3G/4G, memory, battery observation |
| Cross-App / Compatibility | Browser/device support | PC/console/controller/keyboard behavior | Web/mobile sync, browsers, mobile OS/device coverage |
| Negative / Boundary | Missing fields, invalid amount, reject without reason | Reconnect during reward claim, session change, area reload, multiple maps | Wrong password, locked account, negative balance, unavailable service |
| Regression | Re-run main workflow after fixes | Re-run latest patch fixes and reward integrity checks | Re-run balance, masking, logout, cross-channel checks |
| Automation | Login, create draft, submit, approve, status checks | Economy idempotency, reward multiplier, stable/mount smoke, launch smoke | API masking, authorization, account overview response, UI smoke |

## Portfolio Summary

The goal is not to claim complete product knowledge. The goal is to show structured QA thinking: ask requirement questions, identify high-risk areas, define expected behavior, execute test cases, validate evidence, report defects, and recommend release readiness.
