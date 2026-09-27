# 20 Functional Test Cases

Execution is based on the supplied APK screenshots. Cases requiring interaction not captured in screenshots are marked **Not executed** rather than fabricated as passed.

| ID | Test | Type | Priority | Status |
|---|---|---|---|---|
| TC-001 | Login with valid registered email and password | Positive | High | Pass* |
| TC-002 | Login with unregistered email | Negative | High | Pass* |
| TC-003 | Login with incorrect password | Negative | High | Not executed |
| TC-004 | Email/mobile field rejects malformed email | Negative | Medium | Fail |
| TC-005 | Password field masks password | Positive | Low | Pass |
| TC-006 | Forgot password navigation | Positive | Medium | Not executed |
| TC-007 | Back navigation from password screen | Positive | Low | Not executed |
| TC-008 | Dashboard loads after authentication | Positive | High | Pass |
| TC-009 | Upcoming shift countdown accuracy | Edge | Medium | Pass |
| TC-010 | Clock In before shift starts | Negative | High | Not executed |
| TC-011 | Approvals page with Leave tab | Positive | Medium | Pass |
| TC-012 | Approvals page with regularization requests | Positive | High | Pass |
| TC-013 | Approve a regularization request | Positive | High | Not executed |
| TC-014 | Reject a regularization request | Negative | High | Not executed |
| TC-015 | View regularization request details | Positive | Medium | Not executed |
| TC-016 | Attendance Team view current day | Positive | Medium | Pass |
| TC-017 | Attendance historical day filter | Positive | Low | Pass |
| TC-018 | Directory search employee | Positive | Medium | Pass |
| TC-019 | Profile sections navigation | Positive | Medium | Pass |
| TC-020 | Profile completion indicator consistency | Edge | Low | Pass |