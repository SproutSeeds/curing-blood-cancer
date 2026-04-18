# Static Synthetic Caregiver Intake Frontend Smoke Test v0

Stewarded by [frg.earth](https://frg.earth/).

- disease program: `multiple-myeloma`
- artifact id: `multiple-myeloma-static-synthetic-caregiver-intake-frontend-smoke-test-v0`
- status: public safety smoke-test report
- claim level: open-question
- clinical boundary: research-use-only, not medical advice
- data boundary: no real case data, no identifiers, no raw records, no uploads,
  no storage, no submission path, no backend call
- target frontend:
  [Static Synthetic Caregiver Intake Frontend v0](static-synthetic-caregiver-intake-frontend-v0.html)
- last reviewed: `2026-04-18`

## Purpose

This smoke test records whether the static synthetic caregiver intake frontend
stays inside its public-safe boundary before any future frontend iteration.

The target is a no-build static HTML/CSS/JS artifact for organizing synthetic
multiple myeloma intake sections. It is not a live intake form, backend, upload
flow, private-lab handoff, diagnostic tool, treatment tool, trial tool,
prognosis tool, or emergency workflow.

## Test Context

| Field | Value |
| --- | --- |
| test date | `2026-04-18` |
| local serving method | `python3 -m http.server 8787 --bind 127.0.0.1` |
| browser check | Playwright against loopback URL |
| desktop viewport | `1440x1000` |
| mobile viewport | `390x844` |
| target path | `disease-programs/multiple-myeloma/case-intake/static-synthetic-caregiver-intake-frontend-v0.html` |
| image asset | `disease-programs/multiple-myeloma/case-intake/assets/medical-care-commons.jpg` |

## Static Source Scan

| Check | Method | Result | Status |
| --- | --- | --- | --- |
| no form submission path | DOM scan and text scan for `<form>`, `action=`, submit controls | `0` forms, `0` submit controls | pass |
| no upload control | DOM scan and text scan for file inputs | `0` file inputs | pass |
| no backend or data calls | scan for `fetch`, `XMLHttpRequest`, `sendBeacon`, `WebSocket`, `EventSource`, `indexedDB` | no matches | pass |
| no browser storage code | scan for `localStorage`, `sessionStorage`, `document.cookie` | no storage-writing code | pass |
| no email path | scan for `mailto:` | no matches | pass |
| no external static dependency | CSP and image source inspection | image localized to `assets/medical-care-commons.jpg`; CSP uses `img-src 'self' data:` and `connect-src 'none'` | pass |

## Browser Smoke Checks

| Check | Observation | Status |
| --- | --- | --- |
| page loads | target returned `200 OK` over loopback | pass |
| local image loads | local image returned `200 OK` or browser cache `304 Not Modified` over loopback | pass |
| console health | no console errors or warnings after favicon repair | pass |
| navigation | all 12 synthetic intake sections navigated and displayed expected headings | pass |
| disabled handoff controls | `Private handoff not live` and `Submit disabled in public demo` remained disabled | pass |
| storage after interaction | `localStorage.length = 0`, `sessionStorage.length = 0`, `document.cookie.length = 0` after clicking through all sections | pass |
| public boundary copy | public demo warning, no-advice boundary, emergency boundary, clinician-review boundary, and frg.earth stewardship text were present | pass |
| unknown states | `unknown`, `not sure`, and `not collected` synthetic states were present | pass |
| desktop layout | desktop viewport rendered without smoke-test layout blockers | pass |
| mobile layout | `390x844` viewport had no horizontal overflow and no offscreen element offenders | pass |

## Asset Repair

The first smoke pass observed a public Wikimedia image request. That request was
not a case-data path or backend call, but it created an unnecessary external
dependency for a public safety prototype.

The localized image is the Wikimedia Commons `Medical Care.jpg` file. The file
page records the upstream Pixabay source, author, and CC0 1.0 public-domain
dedication. The local copy was kept generic and stripped of metadata before
commit.

Repair applied:

- copied the generic Wikimedia image into a local static asset
- stripped image metadata with `jpegtran -copy none -optimize`
- updated the frontend to reference `assets/medical-care-commons.jpg`
- tightened CSP from external-image allowlisting to `img-src 'self' data:`
- added an empty data favicon to avoid a browser favicon `404`

## Result

The frontend passes this public safety smoke test for the current static
prototype scope.

Safe claims:

- static public prototype only
- synthetic fixture content only
- no form submission path
- no file upload control
- no backend or data-call code path
- no local storage, session storage, cookie, email, auth, account, or database
  behavior
- no external image dependency
- no treatment, trial, prognosis, monitoring, urgency, or emergency advice

Unsafe claims:

- not a full security audit
- not accessibility certification
- not clinical, legal, privacy, regulatory, or publication approval
- not permission to collect real case data
- not permission to connect this frontend to a private lab
- not evidence that any patient-specific system is safe

## Follow-Up

The next public-safe work should leave caregiver intake collection blocked and
derive the model-facing synthetic state schema from
[Myeloma Machine Representation Stack v0](../machine-representation-stack-v0.md).
That handoff is complete as
[Myeloma State Object Schema v0](../../../schemas/myeloma-state-object-schema-v0.md);
the current next implementation atom is `synthetic-myeloma-state-fixture-v0`.

## Public Safety Check

This artifact contains no patient-identifying information, no private records,
no real case data, no upload path, no backend endpoint, no model output, no
patient-specific prediction, no recommendation, and no claim that multiple
myeloma has been cured.
