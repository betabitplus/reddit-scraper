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

Live e2e and workbench flows use direct network access by default. `.envrc`
still loads the declared Reddit session and proxy secret material from
`betabit-secrets`, but removes proxy environment variables unless
`REDDIT_SCRAPER_USE_PROXY=1` is explicitly set. The opt-in keeps dedicated
proxy-routing probes available without spending proxy quota during ordinary
scripts or documentation builds.

## Docs

- [Package docs](docs/reddit_scraper/README.md)
- [Usage](docs/reddit_scraper/usage.md)
- [Verification](docs/reddit_scraper/verification/README.md)
- [Setup](SETUP.md)
- [Contributing](CONTRIBUTING.md)
