# Test Summary Report

## Scope Tested
- Create request
- Required field validation
- Submit for approval
- Approve / reject request
- Status display
- Read-only behavior
- Regression checklist

## Metrics

| Metric | Count |
|---|---:|
| Total Test Cases | 8 |
| Passed | 5 |
| Failed | 2 |
| Blocked | 1 |

## Defects

| Defect ID | Title | Severity |
|---|---|---|
| BUG-001 | Approved request remains editable | High |
| BUG-002 | Rejection allowed without reason | Medium |

## Recommendation
Not ready for release until BUG-001 is fixed and retested. After the fix, run regression around approval, status, read-only behavior, and request history.
