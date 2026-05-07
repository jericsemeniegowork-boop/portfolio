# 01. Requirement Analysis

## Feature

Purchase Request and Approval Management System

## Objective

Validate that users can create, submit, approve, reject, view, and track purchase requests according to business requirements.

## Sample Requirements

| ID | Requirement |
|---|---|
| REQ-001 | A requester can create a purchase request with required item details. |
| REQ-002 | A requester cannot submit a request if required fields are missing. |
| REQ-003 | A request with valid details can be submitted for approval. |
| REQ-004 | An approver can approve or reject a pending request. |
| REQ-005 | A rejected request must require a rejection reason. |
| REQ-006 | An approved request must become read-only for the requester. |
| REQ-007 | The request list must show the correct latest status. |
| REQ-008 | Request history must record create, submit, approve, reject, and update actions. |
| REQ-009 | Unauthorized users must not access approval actions. |
| REQ-010 | Regression testing must confirm that related workflows still work after changes. |

## Testable Areas Identified

- Required field validation
- Valid request creation
- Submit for approval
- Approver decision flow
- Rejection reason validation
- Status update behavior
- Read-only behavior after approval
- Role-based access control
- Request list and details consistency
- History/audit trail behavior
- Regression impact around create, submit, approve, reject, and search

## Clarification Questions

1. Which user roles can create a purchase request?
2. Can a requester approve their own request?
3. Which fields are mandatory before submission?
4. What are the allowed request statuses?
5. Should rejected requests be editable and resubmittable?
6. Should approved requests be completely read-only?
7. What actions should appear in request history?
8. Are there department-based or amount-based approval rules?
9. What should happen if the approver is inactive?
10. What are the expected entry and exit criteria for release?

## Assumptions

- Requester and approver are separate roles.
- Approved requests should not be editable by the requester.
- Rejection requires a reason.
- Request status should be consistent across list, detail, and history views.
- Audit trail/history is required for important actions.

## Risks and Dependencies

| Risk / Dependency | Impact |
|---|---|
| Incorrect approval role setup | Unauthorized approval or blocked approval |
| Missing validation rules | Invalid request data may be submitted |
| Incorrect status transition | Request workflow may become unreliable |
| Approved request remains editable | Audit and approval integrity risk |
| Request list not synced with details | User confusion and reporting issues |
| Incomplete audit trail | Weak traceability and release risk |
