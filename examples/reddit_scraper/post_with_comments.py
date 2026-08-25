"""Open a post and read its comments
==================================

Compose two public operations: pick one live post from a subreddit listing, then
load the post body and comment tree from its permalink.
"""
# sphinx_gallery_tags = ["post", "comments", "composition"]
# sphinx_gallery_thumbnail_path = "_static/gallery/post-comments.svg"

from __future__ import annotations

import os

import reddit_scraper


# %%
# Select one live post
# --------------------
def first_permalink() -> str | None:
    """Return the first permalink from a small hot listing."""
    response = reddit_scraper.fetch_subreddit_posts(
        "Python",
        options=reddit_scraper.SubredditPostsOptions(limit=3, category="hot"),
        client=reddit_scraper.ClientOptions(
            session_cookie=os.getenv("REDDIT_SESSION_COOKIE"),
            timeout=15,
        ),
    )
    if not response.results:
        return None
    permalink = response.results[0].get("permalink")
    return str(permalink) if permalink else None


# %%
# Load the post details and comments
# ----------------------------------
# The second public call turns the permalink into a typed ``PostDetailsResponse``.
if __name__ == "__main__":
    permalink = first_permalink()
    if permalink is None:
        print("No post was available in the live listing.")
    else:
        post = reddit_scraper.scrape_post_details(
            permalink,
            session_cookie=os.getenv("REDDIT_SESSION_COOKIE"),
            timeout=15,
        )
        if post is None:
            print("The selected post could not be loaded.")
        else:
            print(f"title: {post.title}")
            print(f"top-level comments: {len(post.comments)}")
            for comment in post.comments[:2]:
                body = str(comment.get("body", ""))[:90]
                print(f"- u/{comment.get('author')}: {body}")

# %%
# This is a representative composition flow, not a crawler: pagination, deep
# comment traversal, retries, and failure matrices remain in e2e/workbench.
