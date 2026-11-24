import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

place = " ".join(sys.argv[1:]) or input("Place: ")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"Search Google and list the top 5 tourist attractions in {place}. "
             "Give just the names, numbered 1 to 5, with one short line about each.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())]
    ),
)

print(response.text)