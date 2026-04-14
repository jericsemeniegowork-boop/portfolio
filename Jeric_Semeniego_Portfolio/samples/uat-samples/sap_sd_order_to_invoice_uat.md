# SAP SD Order-to-Invoice — Representative UAT Sample

## Objective
Validate the core order-to-invoice flow from sales order creation through delivery, billing, and invoice confirmation.

## Scope
- Create sales order
- Confirm order data
- Process outbound delivery
- Post goods issue
- Create billing document
- Confirm invoice output and status

## Representative UAT Scenarios
### UAT-01 Create sales order with valid customer and material
**Expected Result:** Sales order is created successfully and a document number is generated.

### UAT-02 Block incomplete order from proceeding
**Expected Result:** Missing mandatory information prevents order completion and a clear message is shown.

### UAT-03 Create outbound delivery from approved order
**Expected Result:** Delivery document is generated and linked to the sales order.

### UAT-04 Post goods issue for delivery
**Expected Result:** Goods issue updates the delivery status correctly.

### UAT-05 Create billing document after goods issue
**Expected Result:** Billing document is created successfully and references the related sales flow documents.

### UAT-06 Confirm final invoice output
**Expected Result:** Invoice status, values, and document references are accurate and complete.

## What this sample demonstrates
- Business-process validation across multiple steps
- UAT thinking focused on expected flow and document linkage
- Clear step/result format that can be tracked in Excel or shared with stakeholders
