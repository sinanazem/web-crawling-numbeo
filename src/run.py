from src.country_name_extractor import fetch_country_names
from src.numbeo_web_crawler import API
from src.utils.db import create_cost_of_living_table




if __name__ == "__main__":
    
    # create Cost of Living table
    create_cost_of_living_table()
    
    # Fetch Country Names
    countries = fetch_country_names()
    
    # ETL 
    BASE_URL = "https://www.numbeo.com/cost-of-living/"
    for country in countries[25:27]:
        api = API(BASE_URL, country, city=1) 
    