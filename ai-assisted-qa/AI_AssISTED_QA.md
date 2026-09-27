# AI-Assisted QA

## AI tool
ChatGPT

## Prompt used
> Review the supplied Kredily HRMS mobile-app screenshots and propose functional test cases, identify only defects directly supported by visible evidence, and suggest an Appium test structure. Do not invent backend behavior or claim tests were executed when only screenshots are available.

## AI-generated output
The AI proposed:
- Login positive/negative/edge cases
- Dashboard and shift validation
- Approvals/regularization workflows
- Attendance and directory checks
- Profile completion validation
- Appium + pytest structure
- Two evidence-supported issues: the account-not-found inconsistency and the misleading email/mobile validation message.

## What I changed / validated
1. Converted the generated ideas into exactly 20 functional test cases.
2. Marked screenshot-supported cases as Pass only where the screenshot provides enough evidence.
3. Marked interaction-dependent cases as Not executed rather than fabricating results.
4. Reviewed the screenshots manually and retained only two confirmed/evidence-supported bugs.
5. Added a separate observations file for items that require live execution.
6. Added Appium code as an executable starting point, while clearly marking locators/credentials that must be finalized on the real APK.
