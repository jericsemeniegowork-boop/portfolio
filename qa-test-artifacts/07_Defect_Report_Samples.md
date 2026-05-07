# 07. Defect Report Samples

## BUG-001: Approved Request Remains Editable

| Field | Details |
|---|---|
| Title | [Purchase Request] Approved request remains editable for requester |
| Environment | QA / Chrome / Windows |
| Severity | High |
| Priority | High |
| Status | New |
| Module | Approval Workflow / Read-only Behavior |

### Preconditions

- Request `PR-1003` exists.
- Request status is `Approved`.
- User is logged in as the original requester.

### Steps to Reproduce

1. Login as requester.
2. Open approved request `PR-1003`.
3. Attempt to edit the Amount field.
4. Attempt to click Save.

### Expected Result

Approved request should be read-only. Protected fields should be disabled and Save should not be available.

### Actual Result

Requester can edit the Amount field and Save button remains available.

### Impact

This may affect approval integrity, audit accuracy, and downstream reporting.

---

## BUG-002: Rejection Allowed Without Reason

| Field | Details |
|---|---|
| Title | [Approval Workflow] Approver can reject request without rejection reason |
| Environment | QA / Chrome / Windows |
| Severity | Medium |
| Priority | High |
| Status | New |
| Module | Approval Workflow |

### Preconditions

- Request is in `Pending Approval` status.
- User is logged in as valid approver.

### Steps to Reproduce

1. Login as approver.
2. Open a pending request.
3. Click Reject.
4. Leave rejection reason blank.
5. Confirm rejection.

### Expected Result

System should block rejection and display a required reason validation message.

### Actual Result

System allows rejection without a reason.

### Impact

Business users cannot understand why the request was rejected, and audit trail becomes incomplete.

---

## BUG-003: Request List Status Does Not Match Detail Page

| Field | Details |
|---|---|
| Title | [Request List] Request list shows old status after approval |
| Environment | QA / Edge / Windows |
| Severity | Medium |
| Priority | Medium |
| Status | New |
| Module | Request List / Status Display |

### Preconditions

- Request was approved by approver.

### Steps to Reproduce

1. Login as approver.
2. Approve a pending request.
3. Go to Request List.
4. Search the request ID.
5. Open the request details.

### Expected Result

Request List and Request Detail page should both show `Approved`.

### Actual Result

Request Detail page shows `Approved`, but Request List still shows `Pending Approval`.

### Impact

Users may think the request is still waiting for approval.
