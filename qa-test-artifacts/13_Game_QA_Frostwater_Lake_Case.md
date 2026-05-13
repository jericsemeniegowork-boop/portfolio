# Extra Game QA Case Study: Frostwater Lake Reward Integrity Investigation

## Purpose
This is a non-confidential QA portfolio sample for a live-service game economy incident. It covers patch testing, manual test cases, incident escalation, and abuse-risk validation for a suspected treasure reward duplication issue.

## Incident Summary
- **Incident ID:** INC-ECO-FROST-001
- **Severity:** Critical / P0
- **Component:** Online Economy / Treasure Maps / Reward Transactions
- **Risk:** Duplicate cash, gold, XP, or treasure reward transaction from a single map instance.

## Core Test Cases

| ID | Title | Priority | Coverage |
|---|---|---:|---|
| TC-FROST-001 | Verify treasure reward is granted once | Critical | Reward and inventory integrity |
| TC-FROST-002 | Verify reconnect does not duplicate reward | Critical | Network persistence |
| TC-FROST-003 | Verify session change does not restore claimed reward | Critical | Session state |
| TC-FROST-004 | Verify area reload does not reset claimed chest state | High | World streaming regression |
| TC-FROST-005 | Verify multiple treasure maps do not corrupt inventory state | High | Inventory regression |
| TC-ABUSE-001 | Verify repeated reward claim attempts are rejected and logged | Critical | Anti-abuse and server authority |

## Evidence Required
- Video recording
- Build version
- Platform
- Player ID
- Session ID
- Treasure map instance ID
- Chest instance ID
- Wallet before/after
- Inventory before/after
- Economy transaction logs
- Security telemetry

## Escalation Summary
P0 investigation opened for a suspected reward integrity issue. Risk includes duplicate cash/gold/XP grants from a single treasure map state. Request review from Economy Backend, Gameplay Systems, Online Services, Anti-Cheat, and Live Ops.

## Fix Acceptance Criteria
- Valid reward claim grants exactly one reward.
- Treasure map is consumed or marked completed.
- Reconnect, session change, and area reload do not duplicate the reward.
- Repeated or invalid claim requests are rejected server-side.
- Suspicious attempts are logged for review.
- Normal treasure map flows still work after the fix.


# Added Patch Regression Context: Latest / Recent FTO-Style Coverage

## Official Patch Context Used for This Sample

- Frontier Trails Online Patch v1.8.0 is used as the latest fictional patch-note reference for this portfolio sample.
- Current Frontier Trails Online live-service context is represented by the Seasonal Wildlife Research bonus rotation.
- In a real QA role, the exact build number, environment, and release notes must be confirmed before testing.

## Patch Areas Added to Regression Scope

| Patch Area | Test Type | Validation Focus |
|---|---|---|
| Custom crew names hidden publicly | Privacy / UI / Regression | Public players do not see custom crew names. |
| Custom mount names hidden publicly | Privacy / UI / Regression | Public players see mount breed, not custom mount name. |
| Wildlife Research samples count toward Daily Challenges | Functional / Regression / Economy | Sample progress updates correctly and pays once. |
| Open-World Missions launch fix | Functional / Smoke / Regression | Missions launch, objectives appear, rewards resolve. |
| Stable entry improvement | Regression / Performance / Stability | Stable menu loads without infinite loading. |
| Mount and wagon summon improvement | Functional / Regression | Correct owned mount or wagon responds after travel/session changes. |
| Voice chat defaults to Off | Privacy / Settings / Regression | Fresh or default sessions do not expose voice chat unexpectedly. |
| PC crash / launch / HDR / FSR changes | Compatibility / Performance / Stability | Launch, graphics settings, crash logs, and supported PC configuration checks pass. |
| Wildlife Research bonus rotation | Economy / UI / Regression | Bonus text and reward multipliers display and pay correctly once. |

## Testing Types Applied

| Testing Type | Example in this case |
|---|---|
| Functional | Validate reward claim, Wildlife Research sample counting, mission launch, stable entry, mount recall. |
| UI / Visual | Validate reward summary, map marker, stable menu, public name labels, voice chat setting. |
| Security / Anti-Abuse | Reject duplicate reward requests and invalid reward claims server-side. |
| Privacy | Confirm public custom crew and mount names are hidden. |
| Internationalization | Confirm region/account behavior if supported by requirements. |
| Localization | Validate updated strings in supported languages. |
| Accessibility | Check readable prompts, focus, subtitles/captions, and non-color-only state indicators. |
| Performance / Stability | Validate session load, stable load, long sessions, crash fixes, PC graphics behavior. |
| Cross-Platform | Validate behavior across PC and consoles where supported. |
| Negative / Boundary | Disconnect during reward claim, session change, area unload/reload, multiple maps. |
| Regression | Re-run recent patch fixes plus treasure reward integrity checks. |
| Automation | Prioritize economy idempotency, patch smoke checks, and high-risk regression checks. |

## Added Patch Test Cases

### TC-FTO-PATCH-001: Wildlife Research sample and bonus reward verification

**Priority:** High  
**Type:** Functional / Regression / Economy

| Step | Action | Expected Result |
|---:|---|---|
| 1 | Log in with a Wildlife Researcher-enabled QA account. | Player enters online session and Daily Challenge list is available. |
| 2 | Perform a valid sample flow using QA data. | Sample is collected or sold according to the test requirement. |
| 3 | Open Daily Challenge progress. | Wildlife Research sample challenge updates correctly. |
| 4 | Check reward or bonus display if bonus period is active. | Expected bonus text and payout are shown once and match server logs. |

### TC-FTO-PATCH-002: Stable entry and mount recall regression

**Priority:** Critical  
**Type:** Regression / Performance / Stability

| Step | Action | Expected Result |
|---:|---|---|
| 1 | Enter online session mounted on an owned mount. | Player and mount spawn correctly. |
| 2 | Enter stable on while mounted. | Stable menu loads within expected threshold. |
| 3 | Exit stable, fast travel, then call mount. | Correct owned mount responds and can be mounted. |
| 4 | Repeat across multiple sessions/platforms. | No recurring stable lock, missing mount, or summon failure occurs. |

### TC-FTO-PATCH-003: Public custom name privacy regression

**Priority:** High  
**Type:** Privacy / UI / Regression

| Step | Action | Expected Result |
|---:|---|---|
| 1 | Create a custom crew name in QA. | Custom name is saved only where allowed by design. |
| 2 | Observe from another account in the same session. | Public display does not show custom crew name. |
| 3 | Assign a custom mount name and observe from another account. | Public display shows mount breed, not custom mount name. |
| 4 | Check supported platforms. | Public name behavior is consistent. |
