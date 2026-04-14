# Purchase Request & Approval System — Test Plan

## Objective
Validate that the system supports accurate request creation, submission, approval, rejection, repository tracking, and audit visibility for a purchase request workflow.

## In Scope
- Login and session handling
- Request creation and draft editing
- Submission for approval
- Approve / reject actions
- Repository search, filter, sort, and export
- Audit trail and status history
- Role and access control
- Data consistency across UI, API, and database

## Out of Scope
- Performance benchmarking
- Penetration testing
- Production data migration
- Third-party vendor integrations not shown in the sample workflow

## Test Types
- Functional testing
- Negative testing
- Edge case testing
- Role-based testing
- API validation
- SQL spot checks
- Post-release / workflow integrity checks

## High-Risk Areas
- Approved request remains editable
- Wrong approver receives a request
- Mandatory fields are not enforced
- Repository status becomes stale after workflow updates
- Export output is incomplete or inaccurate
- Audit trail misses key approval actions
- UI and database status do not match
- Duplicate submissions are created by double-click or refresh

## Test Data Strategy
### Valid Data
- Standard requester and approver accounts
- Approved supplier names
- Valid cost center values
- Budget codes
- Small, medium, and large request amounts

### Invalid Data
- Blank required fields
- Invalid amount values and formats
- Unsupported file types
- Overlength remarks
- Unauthorized role actions

### Edge Data
- Minimum and maximum amount values
- Maximum text boundaries
- Same requester and approver scenario
- Session timeout while editing
- Large repository result sets

## Entry Criteria
- Test environment is available
- Accounts and test data are prepared
- Workflow roles are assigned
- Expected business flow is agreed

## Exit Criteria
- Critical and high-priority issues are documented
- Core workflow scenarios are executed
- Results are captured and reviewed
- Sample evidence is ready for portfolio presentation
