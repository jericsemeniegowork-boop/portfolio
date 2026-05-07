# 09. UAT Checklist

## Purpose

Support business users in validating whether the Purchase Request workflow meets real business needs.

## UAT Scenarios

### Scenario 1: Requester Creates and Submits Request

- [ ] Requester can login.
- [ ] Requester can open Create Request page.
- [ ] Requester can enter valid item details.
- [ ] Requester can save draft.
- [ ] Requester can submit request for approval.
- [ ] Request status becomes Pending Approval.

### Scenario 2: Approver Approves Request

- [ ] Approver can login.
- [ ] Approver can view pending request.
- [ ] Approver can review request details.
- [ ] Approver can approve request.
- [ ] Request status becomes Approved.
- [ ] Request history records approval.

### Scenario 3: Approver Rejects Request

- [ ] Approver can reject request with reason.
- [ ] Rejected request status is displayed.
- [ ] Rejection reason is visible.
- [ ] Request history records rejection.

### Scenario 4: Business Rule Validation

- [ ] Requester cannot approve own request.
- [ ] Rejection requires a reason.
- [ ] Approved request is read-only.
- [ ] Request list and detail page status match.

## UAT Result Template

| Scenario | Result | Notes |
|---|---|---|
| Requester creates and submits request | Pass / Fail / Blocked |  |
| Approver approves request | Pass / Fail / Blocked |  |
| Approver rejects request | Pass / Fail / Blocked |  |
| Role restriction validation | Pass / Fail / Blocked |  |
| Read-only validation | Pass / Fail / Blocked |  |
