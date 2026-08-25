"""Search Reddit and inspect typed results
=======================================

Run one live global search through the function-based public API and inspect the
typed ``SearchResponse`` instead of dealing with Reddit JSON directly.
"""
# sphinx_gallery_tags = ["search", "reddit", "typed-response"]
# sphinx_gallery_thumbnail_path = "_static/gallery/search-reddit.svg"

from __future__ import annotations

import os

import reddit_scraper


# %%
# Configure the Reddit client
# ---------------------------
# The session cookie comes from the caller's environment. No proxy is passed, so
# this example follows reddit-scraper's direct-first default.
def build_client() -> reddit_scraper.ClientOptions:
    """Build direct Reddit client options from the current environment."""
    return reddit_scraper.ClientOptions(
        session_cookie=os.getenv("REDDIT_SESSION_COOKIE"),
        timeout=15,
    )


# %%
# Search and inspect the result
# -----------------------------
# ``search_reddit()`` returns a typed response while keeping each normalized
# Reddit result available as a dictionary.
if __name__ == "__main__":
    response = reddit_scraper.search_reddit(
        "Python 3.14",
        options=reddit_scraper.SearchOptions(limit=5),
        client=build_client(),
    )

    print(f"results: {response.count}")
    for item in response.results[:3]:
        print(f"r/{item.get('subreddit')}: {item.get('title')}")

# %%
# The response count and normalized title/subreddit pairs are the caller-facing
# evidence that the live search completed successfully.
