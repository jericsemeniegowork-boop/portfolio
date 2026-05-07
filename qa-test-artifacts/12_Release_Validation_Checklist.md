# 12. Release Validation Checklist

## Pre-release Checklist

- [ ] Requirements reviewed.
- [ ] Test cases prepared.
- [ ] Test data available.
- [ ] QA/staging environment ready.
- [ ] Critical test cases executed.
- [ ] High-impact defects fixed or accepted.
- [ ] Retesting completed for fixed bugs.
- [ ] Regression testing completed.
- [ ] UAT feedback reviewed.
- [ ] Known issues documented.
- [ ] Test summary report prepared.
- [ ] Release recommendation shared.

## Post-release Smoke Checklist

- [ ] Application is accessible.
- [ ] Requester can login.
- [ ] Approver can login.
- [ ] Purchase Request module opens.
- [ ] Requester can create a draft.
- [ ] Requester can submit request.
- [ ] Approver can approve request.
- [ ] Request status updates correctly.
- [ ] Approved request is read-only.
- [ ] Request history is visible.
- [ ] No critical UI or workflow blockers observed.

## Release Recommendation Format

```text
Release Status: Ready / Not Ready / Ready with Known Issues

Summary:
[Short summary of testing result]

Open Risks:
[List remaining risks]

Recommendation:
[Release recommendation based on test evidence]
```
