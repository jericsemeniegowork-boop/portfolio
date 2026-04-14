-- Representative SQL checks for validating workflow state and approval history

-- Confirm the current status of the request
SELECT request_id, status, updated_at
FROM purchase_requests
WHERE request_id = 'PR-10025';

-- Review the workflow history for the request
SELECT request_id, action, actor, action_time
FROM purchase_request_history
WHERE request_id = 'PR-10025'
ORDER BY action_time DESC;

-- Check for conflicting final statuses
SELECT request_id, COUNT(*) AS conflicting_rows
FROM purchase_requests
WHERE request_id = 'PR-10025'
  AND status IN ('Approved', 'Rejected')
GROUP BY request_id
HAVING COUNT(*) > 1;
