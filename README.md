# reddit-scraper

Standalone Python library for replay-tested Reddit scraping.

## What It Provides

- Global Reddit search and subreddit search.
- Frontpage, r/all, r/popular, and subreddit listing fetches.
- Post details with comments.
- User posts/comments scraping.
- Optional media download with route selection, limits, and local cache reuse.
- Python-declared defaults, structured logging, retry, and disk-backed cache support.

## Quickstart

```bash
uv sync --group dev
uv run pytest tests/reddit_scraper/e2e --record-mode=none --snapshot-warn-unused --no-cov
```

```python
import reddit_scraper

response = reddit_scraper.search_reddit(
    "python",
    options=reddit_scraper.SearchOptions(limit=5),
)
print(response.count)
```

Proxy-backed e2e and workbench flows read `HTTP_PROXY` / `HTTPS_PROXY` from
`../betabit-secrets/browser-automation/proxy.sops.env` through `direnv` +
`sops`. Set `BETABIT_SECRETS_ROOT` only if the secrets checkout lives elsewhere.

## Docs

- [Package docs](docs/reddit_scraper/README.md)
- [Usage](docs/reddit_scraper/usage.md)
- [Verification](docs/reddit_scraper/verification/README.md)
- [Setup](SETUP.md)
- [Contributing](CONTRIBUTING.md)
