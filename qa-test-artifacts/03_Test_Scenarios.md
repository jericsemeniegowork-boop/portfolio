# 03. Test Scenarios

## Purchase Request Creation

| Scenario ID | Scenario |
|---|---|
| TS-001 | Verify requester can open the Create Purchase Request page. |
| TS-002 | Verify requester can save a draft with valid required fields. |
| TS-003 | Verify system blocks submission when required fields are missing. |
| TS-004 | Verify system validates invalid amount values. |
| TS-005 | Verify system accepts valid boundary amount values. |
| TS-006 | Verify requester can edit a draft request before submission. |
| TS-007 | Verify requester can submit a valid request for approval. |

## Approval Workflow

| Scenario ID | Scenario |
|---|---|
| TS-008 | Verify approver can view pending requests assigned to them. |
| TS-009 | Verify approver can approve a pending request. |
| TS-010 | Verify approver can reject a pending request with a reason. |
| TS-011 | Verify system blocks rejection without a reason. |
| TS-012 | Verify requester cannot approve their own request. |
| TS-013 | Verify unauthorized user cannot access approval action. |

## Status and Audit Trail

| Scenario ID | Scenario |
|---|---|
| TS-014 | Verify request list displays latest request status. |
| TS-015 | Verify request detail page displays latest request status. |
| TS-016 | Verify request history records create, submit, approve, and reject actions. |
| TS-017 | Verify rejected request shows rejection reason. |
| TS-018 | Verify approved request becomes read-only. |

## Regression and Release Validation

| Scenario ID | Scenario |
|---|---|
| TS-019 | Verify existing draft creation still works after approval-related fix. |
| TS-020 | Verify request submission still works after status-related fix. |
| TS-021 | Verify approval and rejection still work after UI validation fix. |
| TS-022 | Verify request list, detail page, and history remain consistent after deployment. |
