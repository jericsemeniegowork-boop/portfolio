# QA Tools Utilized in Test Cases

This artifact explains how I utilized manual testing tools and automation testing tools inside the sample portfolio test cases. The goal is to show applied QA workflow, not just list tool names.

## Manual Testing Tools Utilized

| Tool Category | Tools | How I Utilized It in Test Cases | Sample Output |
|---|---|---|---|
| Test Management | TestRail, Zephyr, Excel/Google Sheets | Created test cases, grouped them by module, assigned priority, recorded expected result, actual result, execution status, and retest result. | Test run record, pass/fail count, execution summary |
| Bug Tracking | Jira, Bugzilla, Mantis, ServiceNow-style tickets | Logged defects from failed test cases with reproduction steps, severity, priority, environment, screenshots/video, and retest notes. | Defect report, escalation ticket, retest evidence |
| API Exploration | Postman | Manually triggered API requests to compare backend responses with UI behavior before automation. | API response notes, status code validation, auth check evidence |
| Cross-Browser / Device Checks | BrowserStack | Checked UI behavior across desktop and mobile browsers, device sizes, and operating systems. | Cross-browser screenshots, compatibility checklist |

## Automation Testing Tools Utilized

| Tool Category | Tools | How I Utilized It in Test Cases | Best Candidate Tests |
|---|---|---|---|
| Web Automation | Selenium, Cypress, Playwright | Identified stable UI flows that should be automated after manual validation. | Login smoke, submit request, account overview, read-only validation |
| Mobile Automation | Appium | Planned mobile regression coverage for banking app flows after requirements are stable. | Mobile login, balance display, session timeout, cross-app sync |
| Low-Code / No-Code Automation | BugBug.io, Testim-style tools | Used as an option for quick recorded smoke flows, with manual review to avoid weak assertions and flaky steps. | Login, dashboard open, balance page open |
| Performance Testing | Apache JMeter, LoadRunner | Planned baseline load and response-time checks for high-risk customer flows. | Login, account overview, balance refresh, transaction history |

## Tool Utilization by Sample Test Case

| Sample Test Case | Tools Utilized | How I Applied the Tool | Output / Evidence |
|---|---|---|---|
| TC-PR-001: Create purchase request with valid data | TestRail/Zephyr, Excel/Sheets | Documented steps, test data, expected result, actual result, and pass/fail status. | Executed test case record and test summary count |
| TC-PR-006: Approved request becomes read-only | Jira-style bug tracker, Selenium/Playwright candidate | Logged defect if approved request remained editable; marked as regression automation candidate after fix. | Bug report with severity, screenshots, and retest status |
| TC-GAME-ECO-001: Fictional reward is granted once only | Bug tracker, logs/telemetry, test harness candidate | Validated reward transaction count, inventory state, reconnect behavior, and duplicate prevention. | Incident ticket, log evidence, escalation notes |
| TC-GAME-PATCH-002: Patch regression for stable/mount behavior | Checklist, video evidence, bug tracker | Repeated stable entry, exit, and mount recall steps after patch changes. | Regression checklist and video evidence if failed |
| TC-BANK-001: Account balance displays correctly | TestRail/Zephyr, Postman, BrowserStack | Verified UI balance, compared API response, and checked consistency across desktop and mobile browsers. | Manual execution result, API response notes, cross-device screenshots |
| TC-BANK-SEC-001: Unauthorized account data is not exposed | Postman, bug tracker, security checklist | Checked that API responses only return data for the authenticated customer and do not expose other account details. | API evidence and security defect if failed |
| TC-BANK-A11Y-001: Account page supports accessibility expectations | Accessibility checklist, BrowserStack/device testing | Checked keyboard navigation, labels, focus order, contrast concerns, and screen-reader-friendly structure where available. | Accessibility notes and defects for failed items |
| TC-BANK-PERF-001: Account overview response under load | JMeter/LoadRunner | Planned response-time and load baseline for login/account overview under expected traffic. | Performance summary with response time, errors, and bottlenecks |

## Automation Priority

| Priority | Automate | Keep Manual / Specialist-Led |
|---|---|---|
| High | Login smoke, critical happy paths, API authorization checks, account/reward transaction consistency | Requirement clarification, suspected abuse investigation, business-rule interpretation |
| Medium | Cross-browser checks, basic accessibility scans, repeated form validation | Screen reader review, localization judgment, visual polish |
| Low | Stable minor checks only if valuable | One-off UI changes and unclear requirements |

## Professional Positioning

Manual QA remains the foundation: understand requirements, ask the right questions, design useful tests, execute carefully, and document defects clearly. Automation is strongest when used for stable, repeatable, high-risk checks that need to run often.
