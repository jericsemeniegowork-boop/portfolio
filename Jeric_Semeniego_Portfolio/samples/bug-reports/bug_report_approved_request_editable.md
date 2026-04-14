# Bug Report — Approved Request Remains Editable After Final Approval

## Summary
An already approved purchase request can still be edited and saved by the requester after final approval.

## Module
Approval Workflow / Request Details

## Severity
High

## Priority
High

## Environment
Representative QA sample environment

## Preconditions
- Requester account is active
- Approver account is active
- Purchase request can be created and submitted

## Steps to Reproduce
1. Log in as requester.
2. Create a purchase request with valid data.
3. Submit the request for approval.
4. Log in as approver and approve the request.
5. Return to the requester account.
6. Open the approved request.
7. Edit fields such as amount or remarks.
8. Click Save.

## Expected Result
The approved request should be read-only. Protected fields should not allow edits, and save actions should be blocked.

## Actual Result
The requester can still edit protected fields and save the changes even after the request is approved.

## Business Impact
- Approved records can be changed after final approval.
- Audit accuracy is weakened.
- Compliance and release confidence are reduced.
- Business users may rely on incorrect final data.

## Suggested Validation Checks
- Verify field state after approval for requester and approver roles.
- Confirm audit trail logs any attempted changes.
- Confirm API and database status remain aligned with UI behavior.
