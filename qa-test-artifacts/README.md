# Manual QA Test Artifacts | Purchase Request and Approval Workflow

This repository contains representative, non-confidential Manual QA artifacts for a **Purchase Request and Approval workflow**.

The goal is to show a complete manual QA process:

```text
Requirement Analysis
→ Test Planning
→ Test Case Design
→ Test Data Preparation
→ Environment Check
→ Test Execution
→ Defect Management
→ Retesting
→ Regression Testing
→ Test Reporting
→ Release Validation
```

## Case Study

**Feature:** Purchase Request and Approval Management System

**Main workflow:**

1. Requester creates a purchase request.
2. Requester submits the request for approval.
3. Approver approves or rejects the request.
4. System updates the request status.
5. Approved requests become read-only.
6. Request history records important actions.
7. Regression testing confirms existing workflows still work after changes.

## Files Included

| File | Purpose |
|---|---|
| `01_Requirement_Analysis.md` | Requirements, risks, dependencies, assumptions, and clarifications |
| `02_Test_Plan.md` | Scope, test types, entry/exit criteria, environment, and tools |
| `03_Test_Scenarios.md` | High-level manual test scenarios |
| `04_Manual_Test_Cases.csv` | Detailed manual test cases with steps and expected results |
| `05_Requirement_Traceability_Matrix.csv` | Requirements mapped to scenarios and test cases |
| `06_Test_Data.csv` | Valid, invalid, boundary, and role-based test data |
| `07_Defect_Report_Samples.md` | Sample defects with steps, expected vs actual, severity, and impact |
| `08_Regression_Checklist.md` | Regression checklist for impacted workflows |
| `09_UAT_Checklist.md` | UAT checklist and business validation guide |
| `10_Test_Execution_Report.csv` | Sample test execution status tracking |
| `11_Test_Summary_Report.md` | Test metrics, defect summary, risks, and recommendation |
| `12_Release_Validation_Checklist.md` | Pre-release and post-release validation checklist |
| `templates/` | Reusable templates for bug reports, test cases, and test summaries |

## QA Focus Areas

- Requirement Analysis
- Manual Functional Testing
- Negative Testing
- Boundary Testing
- Regression Testing
- UAT Support
- Defect Documentation
- Retesting
- Release Validation
- Test Summary Reporting

## Note

All data, users, scenarios, and defects are representative samples only. No confidential client or company information is included.


## Testing Types Demonstrated

- Functional testing: validates create, submit, approve, reject, status, read-only behavior, and required field rules.
- Smoke testing: confirms the core workflow is stable enough for deeper testing.
- Sanity testing: verifies focused fixes such as approved request read-only behavior.
- Exploratory testing: checks unexpected user actions such as repeated submit, browser back, unusual values, and inconsistent status views.
- End-to-end testing: validates requester-to-approver workflow from request creation to final status/history check.
- Acceptance/UAT testing: confirms whether the workflow meets business user expectations.
- Regression testing: reruns impacted workflows after fixes or changes to ensure existing behavior still works.
- Performance observation: notes slow page behavior, delayed actions, or timeout symptoms during manual testing.
- Automation-ready awareness: includes supporting Postman, SQL, Browser DevTools, and simple Selenium/Python sample checks without positioning this as an automation-heavy project.
