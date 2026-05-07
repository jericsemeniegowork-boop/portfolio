# 02. Test Plan

## Project

Purchase Request and Approval Management System

## Test Objective

Verify that the Purchase Request workflow works according to requirements and is ready for release.

## In Scope

- Create purchase request
- Required field validation
- Submit request for approval
- Approve request
- Reject request
- Rejection reason validation
- Status update validation
- Role-based access
- Read-only behavior after approval
- Request list and detail page consistency
- Request history/audit trail
- Retesting fixed defects
- Regression testing for impacted workflows
- Test reporting and release validation

## Out of Scope

- Payment processing
- Vendor management integration
- Email/SMS notification delivery
- Performance/load testing
- External accounting system integration
- Production data testing

## Test Types

| Test Type | Purpose |
|---|---|
| Functional Testing | Validate feature behavior against requirements |
| Negative Testing | Validate invalid inputs and blocked actions |
| Boundary Testing | Validate amount and field limits |
| Role-based Testing | Confirm access rules for requester and approver |
| Regression Testing | Confirm existing workflows still work after changes |
| UAT Support | Validate business workflow from user perspective |
| Smoke Testing | Confirm environment/build is ready for deeper testing |

## Entry Criteria

- Functional requirements are available.
- Test environment is accessible.
- Test users are created.
- Test data is prepared.
- Build version is deployed to QA/staging.
- Major environment blockers are cleared.

## Exit Criteria

- Planned critical test cases are executed.
- Critical and high defects are fixed or accepted by stakeholders.
- Retesting is completed for fixed defects.
- Regression testing is completed for impacted areas.
- Test summary report is prepared.
- Release recommendation is provided.

## Test Environment

| Item | Details |
|---|---|
| Environment | QA / Staging |
| Browser | Chrome, Edge |
| Device | Windows desktop/laptop |
| Test Management | Excel / Google Sheets style documentation |
| Defect Tracking | Jira / ServiceNow-style workflow |
| Evidence | Screenshots, notes, test result logs |
