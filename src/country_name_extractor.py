import requests
from bs4 import BeautifulSoup
from loguru import logger
import json

# Configuration
NUMBEO_URL = "https://www.numbeo.com/cost-of-living/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

def fetch_country_names(url=NUMBEO_URL):
    """
    Fetches a list of country names from the given Numbeo Cost of Living URL.

    Args:
        url (str): The URL of the Numbeo page to scrape country names from.

    Returns:
        list: A list of country names if successful, otherwise an empty list.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find("table", {"class": "related_links"})

        # Check if the table is found
        if table:
            # Extract country names from anchor tags in the table
            country_names = [link.text.strip() for link in table.find_all("a")]
            logger.info(f"Found {len(country_names)} country names.")
            return country_names
        else:
            logger.warning("The table with class 'related_links' was not found on the page.")
            return []

    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return []
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return []
def save_to_json(data, filename):
    """
    Saves a list of data to a JSON file.

    Args:
        data (list): The list of data to save.
        filename (str): The path to the JSON file to write to.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)  # Write the data to the file with indentation for readability
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"An error occurred while saving the data: {e}")

# Example usage
if __name__ == "__main__":
    countries = fetch_country_names()
    if countries:
        save_to_json(countries, 'country_names.json')
    else:
        print("No countries were scraped.")
