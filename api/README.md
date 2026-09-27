# API Testing

The APK screenshots supplied for this assessment do not expose API hostnames, routes, request schemas, or captured network traffic. It would be misleading to invent real endpoints.

`Kredily_API_Collection.postman_collection.json` is therefore a **discovery-ready Postman template** with three required API areas: login, dashboard, and attendance.

## How to complete live API testing
1. Run the APK on a device/emulator.
2. Capture traffic using the approved test environment/proxy or inspect the app's network configuration.
3. Replace the placeholder base URL and endpoints.
4. Add positive and negative tests (200/201, 400 validation, 401/403 auth, 404/5xx as applicable).
5. Export the final Postman collection and environment into this folder.
