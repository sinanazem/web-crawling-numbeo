import requests
from bs4 import BeautifulSoup
import psycopg2
import re
from loguru import logger
from src.utils.db import connect_to_db

class ExtractTable:
    """Extracts the table from the BeautifulSoup HTML page and inserts into PostgreSQL"""
    
    def __init__(self, page, country, city=None):
        self.Table = page.find("table", {'class': 'data_wide_table'})  # Finding table with class name
        self.country = country
        self.city = city

    def clean_string(self, s):
        """Cleans unwanted characters from a string"""
        s = re.sub(r"\u00a0", " ", s)  # Replace non-breaking space with a regular space
        s = re.sub(r"\n+", "", s)      # Remove newline characters
        return s.strip()               # Remove any leading or trailing whitespace

    def extract(self):
        """Extracts the table contents and stores them to a PostgreSQL database"""
        if not self.Table:
            return None  # Return None if the table is not found

        connection = connect_to_db()
        if not connection:
            logger.error("Failed to connect to the database.")
            return

        cursor = connection.cursor()
        key = None
        for row in self.Table("tr"):
            if row("th"):
                key = self.clean_string(row("th")[0].text)
            elif key:
                cleaned_row = [self.clean_string(cell.text) for cell in row("td")]
                self.insert_into_db(connection, cursor, key, cleaned_row)
        
        cursor.close()
        connection.close()

    def insert_into_db(self, connection, cursor, category, row):
        """Insert extracted data into the PostgreSQL database"""
        query = """
        INSERT INTO cost_of_living (country, city, category, item, price)
        VALUES (%s, %s, %s, %s, %s)
        """
        city_value = self.city if self.city else "N/A"
        cursor.execute(query, (self.country, city_value, category, row[0], row[1]))
        connection.commit()


class API(object):
    """API to get a country and optionally its cities"""
    
    def __init__(self, BASE_URL, Country, city=0):
        self.base = BASE_URL
        self.url = BASE_URL + "country_result.jsp?country=" + Country + "&displayCurrency=USD"
        self.country = Country
        self.city = None
        response = self.get_page(self.url)
        if response:
            self.page = BeautifulSoup(response.text, "html.parser")
            self.get_city()
            EX = ExtractTable(self.page, Country)
            EX.extract()
            if city:
                self.get_all_city()
        else:
            self.page = None
            self.city = None

    def get_page(self, url):
        """Get the page from the URL"""
        try:
            request = requests.get(url)
            if request.status_code != 200:
                return None
            return request
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            return None

    def get_city(self):
        """Get all cities for a given country"""
        self.city_form = self.page.find("form", {"class": "standard_margin"})
        if self.city_form:
            self.city = [values["value"] for values in self.city_form("option")]

    def get_single_city(self, city):
        """Get table with the city name for the country"""
        city_page_url = f"{self.base}city_result.jsp?country={self.country}&city={city}&displayCurrency=USD"
        city_page = self.get_page(city_page_url)
        if city_page:
            city_soup = BeautifulSoup(city_page.text, "html.parser")
            table = ExtractTable(city_soup, self.country, city)
            table.extract()
        else:
            logger.error(f"Failed to retrieve data for city: {city}")

    def get_all_city(self):
        """Get the table of all the cities and store as a dict"""
        if not self.city:
            logger.info(f"No cities found for country: {self.country}")
            return

        for city in self.city:
            logger.info(f"Crawling Country -> {self.country}, City -> {city}")
            self.get_single_city(city)

# Example usage
if __name__ == "__main__":
    BASE_URL = "https://www.numbeo.com/cost-of-living/"
    country = "Western Sahara"
    api = API(BASE_URL, country, city=1) 
