from googlesearch import search

query = "find top 5 attraction site"

print(f"Fetching Google Web Results for: '{query}'\n")

results = search(query, num_results=5, advanced=True)

for i, result in enumerate(results, 1):
    print(f"{i}. {result.title}")
    print(f"   Description: {result.description}")
    print("-" * 50)
