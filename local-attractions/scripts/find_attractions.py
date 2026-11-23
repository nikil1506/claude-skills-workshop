#!/usr/bin/env python3
"""Open a Google search for attractions near a location."""

import argparse
import sys
import webbrowser
from typing import Optional
from urllib.parse import quote_plus


def build_query(location: Optional[str], kind: str) -> str:
    location = (location or "").strip()
    return f"{kind} in {location}" if location else f"{kind} near me"


def build_url(query: str, use_web: bool) -> str:
    if use_web:
        return f"https://www.google.com/search?q={quote_plus(query)}"
    return f"https://www.google.com/maps/search/{quote_plus(query)}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Find local attractions on Google.")
    parser.add_argument("location", nargs="*", help="City, address, or landmark (omit for 'near me')")
    parser.add_argument("--type", default="tourist attractions", help="What to search for")
    parser.add_argument("--web", action="store_true", help="Use Google web search instead of Maps")
    parser.add_argument("--print-only", action="store_true", help="Print the URL without opening a browser")
    args = parser.parse_args()

    query = build_query(" ".join(args.location), args.type)
    url = build_url(query, args.web)

    print(f"Search: {query}")
    print(f"URL:    {url}")

    if not args.print_only:
        if webbrowser.open(url):
            print("Opened in your default browser.")
        else:
            print("Could not open a browser; use the URL above.", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())