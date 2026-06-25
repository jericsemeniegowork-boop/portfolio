# Defect Report Samples

## BUG-001: Approved Request Remains Editable

**Module:** Purchase Request / Approval  
**Severity:** High  
**Priority:** High

### Steps to Reproduce
1. Login as requester.
2. Open an approved request.
3. Try to edit the Amount field.
4. Click Save.

### Expected Result
Approved request should be read-only and protected fields should be disabled.

### Actual Result
Requester can still edit protected fields.

### Impact
Can affect approval integrity, audit accuracy, and reporting.

---

## BUG-002: Rejection Allowed Without Reason

**Module:** Approval Workflow  
**Severity:** Medium  
**Priority:** High

### Steps to Reproduce
1. Login as approver.
2. Open pending request.
3. Click Reject.
4. Leave reason blank.
5. Confirm rejection.

### Expected Result
System blocks rejection and requires a reason.

### Actual Result
Request is rejected without reason.

### Impact
Business users cannot see why the request was rejected.
