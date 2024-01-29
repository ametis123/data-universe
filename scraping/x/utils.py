import re
from typing import Optional
from urllib.parse import urlparse


def is_valid_twitter_url(url: str) -> bool:
    """Verifies a URL is both a valid URL and is for twitter.com."""
    if not url:
        return False

    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc]) and "twitter.com" in result.netloc
    except ValueError:
        return False


def get_user_from_twitter_url(url: str) -> Optional[str]:
    match = re.search(r"https://twitter.com/([^/]+)/status/", url)

    if match:
        return "@" + match.group(1)
    else:
        return None
