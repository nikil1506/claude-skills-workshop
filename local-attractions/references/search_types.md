# Search type reference

Map what the user says to a `--type` value for `find_attractions.py`.

| User says...                          | `--type` value                  | Maps or `--web`? |
|---------------------------------------|---------------------------------|------------------|
| attractions, sights, sightseeing      | `tourist attractions` (default) | Maps             |
| things to do, activities, fun         | `things to do`                  | Maps             |
| museums, art, galleries               | `museums` / `art galleries`     | Maps             |
| parks, nature, outdoors, hiking       | `parks` / `hiking trails`       | Maps             |
| food, restaurants, where to eat       | `restaurants`                   | Maps             |
| coffee, cafes                         | `cafes`                         | Maps             |
| nightlife, bars                       | `bars` / `nightlife`            | Maps             |
| kids, family                          | `family friendly attractions`   | Maps             |
| rainy day, indoors                    | `indoor activities`             | Maps             |
| date ideas, romantic                  | `romantic things to do`         | `--web`          |
| events, concerts, this weekend        | `events this weekend`           | `--web`          |
| hidden gems, off the beaten path      | `hidden gems`                   | `--web`          |
| itinerary, day trip, "plan my day"    | `one day itinerary`             | `--web`          |

## Tips

- Maps is best for physical places (it shows pins, ratings, hours).
- `--web` is better for lists, articles, events, and itineraries.
- No location given → the script searches "near me" and Google uses the browser's location.

## URL formats the script builds

- Maps: `https://www.google.com/maps/search/<query>`
- Web:  `https://www.google.com/search?q=<query>`
