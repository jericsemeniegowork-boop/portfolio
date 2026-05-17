# Banking QA Case Study: Account Balance & Cross-Channel Validation

## Document Type
Manual QA / Banking Application Test Case / Requirement Gap Analysis / Automation Prioritization

## Case Study Scope
I created this non-confidential banking QA sample for a fictional online banking platform called **SecureBank**. The focus is an **Account Overview and Balance Visibility** feature across web and mobile.

The sample intentionally avoids assuming complete system behavior. It starts with questions a QA analyst should ask before finalizing test coverage.

---

## Feature Under Test

A customer logs in to a banking application and views account information, including:

- Account list
- Available balance
- Ledger/current balance
- Negative balance display
- Pending transactions
- Last updated timestamp
- Cross-device consistency between web and mobile

---

## Requirement Gaps / Questions to Ask

| Area | Questions to Ask Before Testing |
|---|---|
| Balance rules | Should the app show available balance, ledger balance, or both? How are pending transactions displayed? |
| Negative balance | Should negative balances show a minus sign, red text, warning message, overdraft label, or all of these? |
| Permissions | Can all customers see all accounts, or only accounts under their profile? What about joint accounts? |
| Privacy | Should full account numbers be masked? Which customer data is considered sensitive? |
| Security | Is MFA required before viewing balances or only during login? Are screenshots allowed on mobile? |
| Session | What is the inactivity timeout? Are concurrent sessions allowed? |
| Internationalization | Is this a global bank? Can a customer from another country log in? Are country restrictions based on account origin, IP, or customer profile? |
| Localization | Which languages and currencies are supported? How should date, amount, and decimal formats display? |
| Accessibility | What WCAG level is required? Are screen readers and keyboard navigation in scope? |
| Performance | What is the SLA for login and account overview loading? What mobile network profiles should be tested? |
| Cross-app sync | How quickly should changes on mobile appear on desktop, and vice versa? |
| Automation | Which flows are stable enough for UI automation? Which backend validations should be covered by API tests? |

---

## Test Plan Summary

| Item | Detail |
|---|---|
| Objective | Validate that customers can securely view accurate account balances across web and mobile. |
| In Scope | Functional balance display, access control, privacy masking, basic security checks, localization checks, accessibility checks, performance observation, cross-app sync. |
| Out of Scope | Real production banking data, real payment network testing, penetration testing beyond QA-safe checks, regulatory certification. |
| Test Types | Functional, negative, security-aware, privacy, internationalization, localization, accessibility, performance, cross-platform, regression. |
| Priority | High because balance visibility is customer-facing and financial-data related. |

---

## Manual Test Case: Account Balance Overview

### Test Case ID
TC-BANK-001

### Title
Verify customer can log in and view correct masked account balance details.

### Priority
Critical

### Test Type
Functional / Privacy / Security-Aware

### Preconditions
1. Customer test account exists.
2. Customer has at least one active account.
3. Test data uses synthetic banking data only.
4. User has valid credentials.
5. Test environment is not production.

### Test Data

| Data | Example |
|---|---|
| Customer | qa.customer01 |
| Account type | Savings |
| Account number | 1234567890, expected masked display: ******7890 |
| Available balance | 10,000.00 |
| Ledger balance | 10,500.00 |
| Pending debit | 500.00 |
| Currency | PHP |

### Steps

| Step | Action | Expected Result |
|---:|---|---|
| 1 | Open the banking web app. | Login page loads over secure connection. |
| 2 | Enter valid username and password. | Credentials are accepted. |
| 3 | Complete MFA if required by environment. | User is authenticated successfully. |
| 4 | Navigate to Account Overview. | Account list is displayed. |
| 5 | Check account number display. | Account number is masked except allowed last digits. |
| 6 | Check available balance. | Available balance matches expected test data. |
| 7 | Check ledger/current balance. | Ledger balance matches expected test data. |
| 8 | Check pending transaction effect. | Available balance reflects pending debit if business rules require it. |
| 9 | Refresh the page. | Balance values remain consistent. |
| 10 | Log out. | Session ends and protected pages are no longer accessible. |

### Expected Result
The customer can securely view accurate, properly masked account information. Protected account data is unavailable after logout.

---

## Negative Test Cases

| Test ID | Scenario | Expected Result | Priority |
|---|---|---|---|
| TC-BANK-002 | Login with wrong password | Login fails without revealing whether username exists | Critical |
| TC-BANK-003 | Access account page after logout using browser back | User is redirected to login or access denied | Critical |
| TC-BANK-004 | Customer attempts to view another customer account ID | Access is denied and event is logged | Critical |
| TC-BANK-005 | Account has negative balance | Balance displays according to confirmed business rule | High |
| TC-BANK-006 | Pending transaction exists | Available and ledger balance display correctly | High |
| TC-BANK-007 | Unsupported language selected | App falls back to default language or shows controlled error | Medium |
| TC-BANK-008 | Slow 3G profile on mobile | App remains usable or shows loading feedback within SLA | High |

---

## Security-Aware QA Checks

These are QA-safe checks, not a full penetration test.

| Test ID | Scenario | Expected Result |
|---|---|---|
| SEC-BANK-001 | Enter script-like text in editable fields such as nickname or search | Text is sanitized and not executed in the browser |
| SEC-BANK-002 | Session token after logout | Token cannot be reused to access account data |
| SEC-BANK-003 | Direct URL to another account | Server denies unauthorized access |
| SEC-BANK-004 | Sensitive data in URL | Account numbers, tokens, and personal data are not exposed in the URL |
| SEC-BANK-005 | Browser cache after logout | Protected data is not accessible from cached pages |

---

## Privacy Checks

| Test ID | Scenario | Expected Result |
|---|---|---|
| PRIV-BANK-001 | Account number display | Account number is masked according to policy |
| PRIV-BANK-002 | Statement preview | Personal and account data are only shown to authorized user |
| PRIV-BANK-003 | Logs and error messages | Sensitive customer data is not exposed in client-visible errors |
| PRIV-BANK-004 | Cookie consent and tracking | Tracking behavior follows regional privacy requirements if applicable |

---

## Internationalization and Localization Checks

| Test ID | Scenario | Expected Result |
|---|---|---|
| I18N-BANK-001 | Customer logs in from a different country | Behavior follows confirmed bank policy |
| I18N-BANK-002 | Spoofed or unusual IP location | App follows risk/security policy, such as step-up authentication or block |
| L10N-BANK-001 | Change language to supported language | Labels, errors, and buttons render correctly |
| L10N-BANK-002 | Currency and number format | Amounts follow selected locale rules |
| L10N-BANK-003 | Long translated strings | UI does not overlap, truncate critical information, or break layout |

---

## Accessibility Checks

| Test ID | Scenario | Expected Result |
|---|---|---|
| A11Y-BANK-001 | Navigate login and account overview using keyboard only | User can complete critical flow without mouse |
| A11Y-BANK-002 | Screen reader reads account cards | Account labels and balances are announced clearly |
| A11Y-BANK-003 | Color contrast on balance text | Text is readable and does not rely on color alone |
| A11Y-BANK-004 | Error messages | Errors are programmatically associated with related fields |
| A11Y-BANK-005 | Images and icons | Icons have accessible labels where needed |

---

## Performance and Mobile Checks

| Test ID | Scenario | Expected Result |
|---|---|---|
| PERF-BANK-001 | Account overview page load on stable network | Loads within agreed SLA |
| PERF-BANK-002 | Account overview on simulated 3G | App remains usable and shows loading state |
| PERF-BANK-003 | Tap balance refresh button | Response completes within agreed SLA or shows clear pending state |
| PERF-BANK-004 | Mobile app background then foreground | Session and displayed data follow security/session policy |
| PERF-BANK-005 | Battery/memory observation during normal use | No abnormal drain or crash during basic session |

---

## Cross-App / Cross-Platform Checks

| Test ID | Scenario | Expected Result |
|---|---|---|
| CROSS-BANK-001 | View balance on web, then mobile | Same account data is displayed based on sync rules |
| CROSS-BANK-002 | Update account nickname on mobile | Change reflects on web within expected sync time |
| CROSS-BANK-003 | Logout from mobile while web session is active | Behavior follows confirmed concurrent session policy |
| CROSS-BANK-004 | Check supported browsers and devices | Layout and functionality remain consistent |

---

## Automation Priority

| Layer | Good Automation Candidate | Why |
|---|---|---|
| Unit | Balance calculation helpers | Fast and reliable for calculation rules |
| API | Account overview response, authorization, masking | Critical backend behavior; less fragile than UI |
| UI | Login smoke, account overview display, logout | Covers customer journey but should focus on stable critical paths |
| Accessibility | Automated contrast and label scans | Catches common issues early |
| Performance | Account overview response time baseline | Useful for regression trend monitoring |
| Manual | Exploratory security/privacy, localization review, screen reader review | Needs human judgment and domain confirmation |

---

## Sample Bug Report

### Bug ID
BUG-BANK-001

### Title
Account balance page displays full account number instead of masked account number.

### Severity
High

### Priority
P1

### Environment
Web staging, Chrome latest, QA test account qa.customer01

### Steps to Reproduce
1. Log in as qa.customer01.
2. Complete MFA if prompted.
3. Navigate to Account Overview.
4. Observe the account number on the Savings account card.

### Expected Result
The account number should be masked according to policy, such as ******7890.

### Actual Result
The full account number is displayed.

### Impact
Sensitive financial data is exposed on the customer-facing screen. This may create privacy, shoulder-surfing, screenshot, and compliance risk.

### Evidence
Screenshot, test account ID, browser version, timestamp, and network response if allowed.

---

## Severity Examples

| Issue | Suggested Severity | Reason |
|---|---|---|
| Balance button does nothing and user cannot view balance | High | Blocks a critical customer function |
| Wrong available balance is displayed | Critical | Financial accuracy issue |
| Full account number is exposed | High | Privacy and security risk |
| Minor font size shift after clicking balance | Low | Cosmetic issue if information remains readable |
| Unauthorized user can view another account | Critical | Access control and privacy failure |

---

## Portfolio Summary

Designed a banking QA test case package for a fictional account overview feature. The case study covers requirement gap analysis, functional testing, security-aware QA checks, privacy validation, internationalization, localization, accessibility, performance, cross-platform consistency, automation prioritization, and severity assessment.
