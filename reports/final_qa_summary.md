# Final QA Summary — Kredily HRMS Mobile APK

## Scope
Screenshots supplied from the Kredily HRMS Android application were reviewed across:
- Login
- Home/dashboard
- Approvals
- Attendance
- Directory
- Profile

## Functional coverage
20 test cases are included. Current evidence supports execution results for 12 cases; 8 cases require live interaction and are marked Not executed.

## Defects
2 defects are directly supported by the supplied evidence:
- BUG-001 — registered directory email rejected by password login (High)
- BUG-002 — malformed email receives misleading mobile-number validation message (Medium)

The assignment asks for 5 genuine bugs "if available". Only two are directly defensible from the supplied screenshots; additional bugs should be added after live execution rather than fabricated.

## Automation
Five Appium/pytest journey skeletons are included. They require the APK binary, Appium server, device/emulator, and valid credentials for execution.

## API testing
A Postman collection template is included. Real API host/routes were not visible in the supplied screenshots, so no endpoint has been fabricated.

## AI-assisted QA
AI assistance was used to generate and refine test ideas, evidence-based defect candidates, and the automation structure. The prompt, generated output summary, and human validation changes are documented.

## Evidence
All eight supplied screenshots are copied into `evidence/screenshots/`.
