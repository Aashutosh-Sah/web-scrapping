import wikipediaapi
from database import insert_data

# Function to get Wikipedia content with a proper User-Agent
def get_wikipedia_summary(topic):
    user_agent = "MyWikipediaScraper/1.0 (your-email@example.com)"  # Replace with your email
    wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)
    page = wiki.page(topic)

    if page.exists():
        return page.summary[:1000]  # Limiting summary to 1000 characters
    else:
        return None

# Ask user for input
topic = input("Enter the Wikipedia topic you want to search for: ").strip()

if topic:
    print("\nFetching from Wikipedia...\n")
    summary = get_wikipedia_summary(topic)

    if summary:
        print(summary)  # Show scraped data to user

        # Store data in database
        insert_data(topic, summary)
        print("\nData has been saved to the database.")
    else:
        print("Sorry, no Wikipedia page found for that topic.")
else:
    print("Invalid input. Please enter a valid topic.")
