# 11. Test Summary Report

## Project

Purchase Request and Approval Management System

## Build / Environment

| Item | Details |
|---|---|
| Environment | QA / Staging |
| Browser | Chrome, Edge |
| Test Type | Manual Functional, Negative, Regression, UAT Support |
| Test Cycle | Sample Cycle 1 |

## Scope Tested

- Create purchase request
- Required field validation
- Submit for approval
- Approve request
- Reject request
- Role-based access
- Request status display
- Request history/audit trail
- Approved request read-only behavior
- Regression checklist
- Smoke validation

## Execution Summary

| Metric | Count |
|---|---:|
| Total Test Cases | 25 |
| Passed | 18 |
| Failed | 5 |
| Blocked | 2 |
| Not Run | 0 |

## Defect Summary

| Severity | Count |
|---|---:|
| Critical | 0 |
| High | 1 |
| Medium | 2 |
| Low | 0 |

## Open Defects

| Defect ID | Title | Severity | Priority | Status |
|---|---|---|---|---|
| BUG-001 | Approved request remains editable for requester | High | High | New |
| BUG-002 | Approver can reject request without reason | Medium | High | New |
| BUG-003 | Request list shows old status after approval | Medium | Medium | New |

## Risks

- Approved requests can still be edited, which may affect approval integrity.
- Rejection without reason may cause incomplete audit trail.
- Status mismatch may confuse users and affect reporting accuracy.
- Regression and smoke checks are partially blocked by high-impact defect.

## Recommendation

**Not ready for release** until `BUG-001` is fixed and retested.

After fix:

1. Retest BUG-001.
2. Run regression around approval, rejection, request list, detail page, and audit history.
3. Complete blocked smoke test.
4. Update final test summary and release recommendation.
