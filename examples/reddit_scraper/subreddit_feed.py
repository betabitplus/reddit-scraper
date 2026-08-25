"""Read a subreddit feed
======================

Fetch a small live listing from one subreddit and keep listing options explicit
at the call site.
"""
# sphinx_gallery_tags = ["feed", "subreddit", "reddit"]
# sphinx_gallery_thumbnail_path = "_static/gallery/subreddit-feed.svg"

from __future__ import annotations

import os

import reddit_scraper


# %%
# Configure direct Reddit access
# ------------------------------
def build_client() -> reddit_scraper.ClientOptions:
    """Build direct Reddit client options from the current environment."""
    return reddit_scraper.ClientOptions(
        session_cookie=os.getenv("REDDIT_SESSION_COOKIE"),
        timeout=15,
    )


# %%
# Fetch a small hot listing
# -------------------------
if __name__ == "__main__":
    response = reddit_scraper.fetch_subreddit_posts(
        "Python",
        options=reddit_scraper.SubredditPostsOptions(limit=5, category="hot"),
        client=build_client(),
    )

    print(
        f"source: r/{response.metadata['subreddit']} ({response.metadata['category']})"
    )
    print(f"posts: {response.count}")
    for post in response.results[:3]:
        print(f"- {post.get('title')}")

# %%
# Changing the subreddit or listing category does not change the shape of the
# returned ``SearchResponse``.
