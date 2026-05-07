# 08. Regression Checklist

## Purpose

Confirm that existing Purchase Request workflows still work after a change, bug fix, or deployment.

## Checklist

### Login and Access

- [ ] Requester can login successfully.
- [ ] Approver can login successfully.
- [ ] Unauthorized user cannot access approval actions.
- [ ] User session works as expected.

### Request Creation

- [ ] Requester can open Create Request page.
- [ ] Required fields are visible.
- [ ] Draft can be saved with valid details.
- [ ] Missing required fields are blocked.
- [ ] Invalid amount values are rejected.

### Submission

- [ ] Draft request can be submitted.
- [ ] Submitted request status becomes Pending Approval.
- [ ] Duplicate submission is blocked.
- [ ] Request appears in approver queue.

### Approval / Rejection

- [ ] Approver can approve pending request.
- [ ] Approver can reject pending request with reason.
- [ ] Rejection without reason is blocked.
- [ ] Requester cannot approve own request.

### Status and History

- [ ] Request list shows correct latest status.
- [ ] Request detail page shows correct latest status.
- [ ] Request history records create action.
- [ ] Request history records submit action.
- [ ] Request history records approve/reject action.
- [ ] Rejection reason is visible when applicable.

### Read-only Behavior

- [ ] Approved request fields are disabled for requester.
- [ ] Save action is unavailable for approved request.
- [ ] Requester cannot modify approved request through UI.

### Release Validation

- [ ] Smoke test completed after deployment.
- [ ] Critical workflow passed.
- [ ] Known issues documented.
- [ ] Release recommendation provided.
