# Purchase Request & Approval System — Test Cases

### TC-01 Login with valid credentials
**Module:** Authentication  
**Precondition:** Active requester account exists  
**Steps:**
1. Open login page
2. Enter valid username and password
3. Click Sign In

**Expected Result:** User logs in successfully and lands on dashboard.

---

### TC-02 Login with invalid password
**Module:** Authentication  
**Steps:**
1. Open login page
2. Enter valid username and wrong password
3. Click Sign In

**Expected Result:** Login is blocked and a clear validation message is shown.

---

### TC-03 Create request with valid required data
**Module:** Purchase Request Form  
**Steps:**
1. Open request form
2. Enter valid supplier, category, amount, cost center, and justification
3. Click Save Draft

**Expected Result:** Draft request is saved successfully and a request ID is generated.

---

### TC-04 Create request with blank required fields
**Module:** Purchase Request Form  
**Steps:**
1. Open request form
2. Leave required fields blank
3. Click Save Draft or Submit

**Expected Result:** System blocks save/submit and shows required-field messages.

---

### TC-05 Amount field rejects invalid format
**Module:** Purchase Request Form  
**Steps:**
1. Enter letters or invalid characters in amount
2. Attempt to save

**Expected Result:** System rejects invalid amount input.

---

### TC-06 Submit request for approval
**Module:** Workflow  
**Precondition:** Valid draft exists  
**Steps:**
1. Open valid draft
2. Click Submit
3. Confirm submission

**Expected Result:** Request moves to Pending Approval and correct approver is assigned.

---

### TC-07 Double-click submit does not create duplicate request
**Module:** Workflow / Reliability  
**Steps:**
1. Open valid draft
2. Double-click Submit quickly

**Expected Result:** Only one submission is created and no duplicate workflow entry appears.

---

### TC-08 Reject request without mandatory reason
**Module:** Approval  
**Precondition:** Approver opens pending request  
**Steps:**
1. Click Reject
2. Leave rejection reason blank
3. Confirm

**Expected Result:** System blocks rejection and requires a reason.

---

### TC-09 Approve request
**Module:** Approval  
**Steps:**
1. Open pending request as approver
2. Click Approve

**Expected Result:** Status changes to Approved and action is recorded in audit history.

---

### TC-10 Approved request becomes read-only
**Module:** Role / Workflow Integrity  
**Precondition:** Request already approved  
**Steps:**
1. Open approved request as requester
2. Try editing protected fields

**Expected Result:** Protected fields are read-only and save is blocked.

---

### TC-11 Repository search by request ID
**Module:** Repository  
**Steps:**
1. Go to repository page
2. Search by exact request ID

**Expected Result:** Correct record is returned.

---

### TC-12 Filter repository by status
**Module:** Repository  
**Steps:**
1. Apply filter = Approved
2. Review results

**Expected Result:** Only approved requests are shown.

---

### TC-13 Sort repository by date
**Module:** Repository  
**Steps:**
1. Sort by created date ascending
2. Sort by created date descending

**Expected Result:** Records sort correctly both ways.

---

### TC-14 Export filtered repository results
**Module:** Repository / Export  
**Steps:**
1. Apply status filter
2. Click Export

**Expected Result:** Exported file contains only filtered results and correct columns.

---

### TC-15 Repository and detail view show same status
**Module:** Data Consistency  
**Steps:**
1. Open repository
2. Note request status
3. Open detail page

**Expected Result:** Status matches in both views.

---

### TC-16 Audit trail records approval action
**Module:** Audit Trail  
**Steps:**
1. Approve a pending request
2. Open audit history

**Expected Result:** Audit history shows action, actor, and timestamp.

---

### TC-17 Session timeout while editing draft
**Module:** Session Handling  
**Steps:**
1. Open draft
2. Leave page idle until session expires
3. Try saving

**Expected Result:** User is redirected or prompted safely, and no silent data corruption occurs.

---

### TC-18 Unauthorized user cannot approve request
**Module:** Access Control  
**Steps:**
1. Login as requester
2. Open request awaiting approval
3. Attempt to approve

**Expected Result:** Approval action is not available or access is blocked.

---

### TC-19 Large remarks field at max boundary
**Module:** Validation / Edge Case  
**Steps:**
1. Enter remarks at maximum allowed character length
2. Save request

**Expected Result:** Save succeeds if within limit and fails cleanly if exceeded.

---

### TC-20 Upload unsupported attachment type
**Module:** Attachment Validation  
**Steps:**
1. Attach unsupported file type
2. Submit

**Expected Result:** Upload is blocked with a clear error message.

---
