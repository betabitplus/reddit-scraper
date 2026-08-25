"""Download media directly and reuse the cache
=============================================

Download one small public image twice with media caching enabled. The example
explicitly keeps proxy routing disabled and shows the cache decision in the
returned ``MediaItem``.
"""
# sphinx_gallery_tags = ["media", "cache", "direct"]
# sphinx_gallery_thumbnail_path = "_static/gallery/media-cache.svg"

from __future__ import annotations

from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory

import reddit_scraper

IMAGE_URL = "https://picsum.photos/seed/reddit-scraper-docs/320/180.jpg"


# %%
# Build an explicit direct-download configuration
# -----------------------------------------------
def build_media_config() -> reddit_scraper.MediaConfig:
    """Enable image downloads and caching without proxy routing."""
    return replace(
        reddit_scraper.get_default_media_config(),
        enabled=True,
        allowed_types={"image"},
        cache_media=True,
        use_proxy_for_small=False,
        use_proxy_for_large=False,
        max_total_downloads=2,
    )


# %%
# Download twice through the same cache
# -------------------------------------
if __name__ == "__main__":
    with TemporaryDirectory(prefix="reddit-scraper-media-") as temp_dir:
        cache_dir = str(Path(temp_dir))
        config = build_media_config()
        first = reddit_scraper.download_media(
            IMAGE_URL,
            config=config,
            cache_dir=cache_dir,
        )
        second = reddit_scraper.download_media(
            IMAGE_URL,
            config=config,
            cache_dir=cache_dir,
        )

    first_item = first.items[0] if first.items else None
    second_item = second.items[0] if second.items else None
    first_from_cache = first_item.from_cache if first_item else None
    second_from_cache = second_item.from_cache if second_item else None
    print(f"first download:  from_cache={first_from_cache}")
    print(f"second download: from_cache={second_from_cache}")
    print(f"bytes: {second_item.size_bytes if second_item else 0}")

# %%
# The expected live result is a network download followed by a cache hit, with no
# proxy traffic consumed by either call.
