---
name: reddit-scraper-docs
doc_type: index
description: Index of the Reddit scraper docs. Use when you need to find the right package document.
---

# Reddit Scraper Docs

## Overview

These docs describe the Reddit scraper package, its runtime architecture,
dependencies, and verification surfaces. Runnable caller workflows live in
`examples/reddit_scraper` and are rendered by Sphinx-Gallery.

## Files

- [Architecture](architecture/README.md)
  Explains the public package boundary, private runtime, and behavior slices.
  Use it to understand how the package holds together.
- [Dependencies](dependencies.md)
  Explains why each shipped runtime dependency exists.
  Use it to review whether a dependency belongs in the runtime package.
- [Verification](verification/README.md)
  Explains how tests, e2e replay, and workbench probes prove product behavior.
  Use it to find the proof surface for one behavior slice.
