# Purchase Request & Approval System — Repository and Workflow Scenarios

## Workflow Scenarios
1. Requester creates a valid draft and receives a request ID.
2. Requester submits a complete draft for approval.
3. Correct approver receives the pending request.
4. Approver rejects a request and a rejection reason is required.
5. Approver approves a valid request and the audit trail is updated.
6. Approved request becomes read-only for requester edits.
7. Unauthorized users cannot approve pending requests.
8. Session timeout during draft editing does not corrupt data.

## Repository Scenarios
1. Search by exact request ID returns the correct record.
2. Filter by status shows only matching records.
3. Sort by created date works in ascending and descending order.
4. Detail view status matches repository list status.
5. Export respects active filters and includes expected columns.
6. Repository refresh shows the latest workflow state after approval or rejection.

## Cross-Validation Scenarios
1. UI status matches API status for the same request.
2. UI status matches database status for the same request.
3. Approval history appears in the audit trail and database history table.
4. Duplicate submit actions do not create duplicate workflow entries.
