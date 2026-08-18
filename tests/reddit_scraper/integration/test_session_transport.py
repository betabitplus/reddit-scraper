"""Authenticated Reddit session transport integration tests."""

from __future__ import annotations

import reddit_scraper


def test_session_cookie_is_scoped_to_reddit_hosts() -> None:
    """Send the configured Reddit session only to Reddit requests."""
    config = reddit_scraper.ScraperConfig(session_cookie="session-secret")
    options = reddit_scraper.ClientOptions(session_cookie="session-secret")
    assert "session-secret" not in repr(config)
    assert "session-secret" not in repr(options)

    scraper = reddit_scraper.RedditScraper(config=config)
    try:
        reddit_request = scraper.client.build_request(
            "GET", "https://www.reddit.com/search.json?q=python"
        )
        external_request = scraper.client.build_request(
            "GET", "https://example.com/image.jpg"
        )
    finally:
        scraper.close()

    assert reddit_request.headers.get("cookie") == "reddit_session=session-secret"
    assert "cookie" not in external_request.headers
