---
name: local-attractions
description: Find local attractions (sights, museums, parks, restaurants, things to do) near the user or a named place by opening a Google search in the browser. Use when the user asks for attractions, places to visit, things to do, or sightseeing near a location, e.g. "find attractions near me", "things to do in Paris", "museums in Chicago".
---

# Local Attractions Finder

Opens Google (Maps by default) in the user's default browser with a search for attractions near a location.

## How to use

Run the bundled script with Bash:

```bash
python3 ~/.claude/skills/local-attractions/scripts/find_attractions.py [LOCATION] [--type TYPE] [--web] [--print-only]
```

- `LOCATION` (optional): a city, neighborhood, address, or landmark. Leave it out to search "near me".
- `--type TYPE`: what to look for. Default `tourist attractions`. Examples: `museums`, `parks`, `restaurants`, `things to do`.
- `--web`: open a regular Google web search instead of Google Maps.
- `--print-only`: print the URL without opening the browser.

## Picking a search type

If the user's request is vague ("something fun", "date ideas", "rainy day"), read
`references/search_types.md` to map it to a good `--type` value. Run the script
more than once if the user asked for several kinds of places.

## After running

Reply using the format in `assets/results_template.md`: say Google was opened and
include each printed URL so the user can click it if the browser didn't open.
