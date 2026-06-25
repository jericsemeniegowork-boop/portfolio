# Requirement Analysis

## Case Study
Purchase Request and Approval Management System

## Testable Requirements
- Requester can create a purchase request.
- Required fields must block submission when missing.
- Requester can submit a valid request for approval.
- Approver can approve or reject a pending request.
- Rejection must require a reason.
- Approved requests must become read-only.
- Request list and detail page must show the same status.
- Request history must record important actions.
- Unauthorized users must not access approval actions.

## Clarification Questions
1. Can a requester approve their own request?
2. Which fields are required before submission?
3. Should rejected requests be editable and resubmittable?
4. What actions should appear in history/audit trail?
5. What are the release exit criteria?

## Main Risks
- Approved request remains editable.
- Status mismatch between list and detail page.
- Rejection without reason.
- Missing audit/history record.
- Unauthorized approval action.
