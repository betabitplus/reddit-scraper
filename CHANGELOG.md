# Changelog

## [0.3.2](https://github.com/betabitplus/reddit-scraper/compare/v0.3.1...v0.3.2) (2026-08-25)


### Bug Fixes

* make proxy usage opt in ([#64](https://github.com/betabitplus/reddit-scraper/issues/64)) ([282cf16](https://github.com/betabitplus/reddit-scraper/commit/282cf16d48488be7997681e44018fadc1b4de54f))

## [0.3.1](https://github.com/betabitplus/reddit-scraper/compare/v0.3.0...v0.3.1) (2026-08-18)


### Bug Fixes

* make reddit live e2e authoritative ([#48](https://github.com/betabitplus/reddit-scraper/issues/48)) ([830a6ad](https://github.com/betabitplus/reddit-scraper/commit/830a6ada9d35c62c3b2179cf8e5512f3ddddf2fe))

## v0.3.0 (2026-07-12)

### Feat

- **env**: configure shared proxy secrets (#45)

## v0.2.6 (2026-07-04)

### Fix

- promote repository rename sync
- sync repository rename references

## v0.2.5 (2026-06-21)

### Fix

- use cleaned starter workflow sources
- use cleaned starter template ref
- pin cleaned starter baseline

## v0.2.4 (2026-06-19)

### Fix

- enforce single-run main CI

## v0.2.3 (2026-06-15)

### Fix

- validate cache backend dependency
- include runtime cache dependency
- add package examples path
- add examples import root package
- mark workbench modules as runnable cells

## v0.2.2 (2026-05-23)

### Fix

- use shared package root imports

## v0.2.1 (2026-05-18)

### Refactor

- complete py-lib starter rollout

## v0.2.0 (2026-05-08)

### Feat

- establish reddit scraper library package structure

### Refactor

- align config lifecycle organization
- prune synthetic workbench probes
- align reddit scraper with library rules

## 0.1.0

- Establish Reddit scraper library package with the standard py-lib repo structure.
- Add public search, feed, post, user, cache, retry, and media behavior slices.
- Add hermetic VCR/snapshot-backed e2e verification.
