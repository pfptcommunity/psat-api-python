# PSAT Live Smoke Tests

These scripts are maintainer release checks, not user examples. They require a live PSAT API token and are meant to
validate that every modeled reporting endpoint still matches the live API.

## Settings

Copy `examples/settings.example.json` to `settings.json` at the project root, or place `settings.json` in this
directory.

Required settings:

- `region`
- `api_token`

## Read-Only Smoke Test

```bash
PYTHONPATH=src python3 tools/live_smoke/read_only.py
```

The smoke test is read-only. It calls each v0.3.0 report endpoint once and prints the modeled resource URL, page
metadata, pagination links, item count, and the first row shape returned by the API.

Covered endpoints:

- `GET https://{region-host}/api/reporting/v0.3.0/cyberstrength`
- `GET https://{region-host}/api/reporting/v0.3.0/trainingenrollments`
- `GET https://{region-host}/api/reporting/v0.3.0/phishalarm`
- `GET https://{region-host}/api/reporting/v0.3.0/phishing`
- `GET https://{region-host}/api/reporting/v0.3.0/phishing_extended`
- `GET https://{region-host}/api/reporting/v0.3.0/training`
- `GET https://{region-host}/api/reporting/v0.3.0/users`
