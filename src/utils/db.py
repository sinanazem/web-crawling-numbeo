import os
import psycopg2
from loguru import logger

import time

def connect_to_db():
    """Establish a connection to the PostgreSQL database."""
    for _ in range(5):  # Retry up to 5 times
        try:
            connection = psycopg2.connect(
                host=os.getenv("POSTGRES_HOST"),
                database=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD")
            )
            return connection
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(f"Error connecting to the database: {error}")
            time.sleep(5)  # Wait for 5 seconds before retrying
    return None

def create_cost_of_living_table():
    """Create a table in the PostgreSQL database."""
    connection = connect_to_db()
    if connection is not None:
        try:
            cursor = connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS cost_of_living (
                id SERIAL PRIMARY KEY,  -- Unique identifier for each record
                country VARCHAR(255),   -- Country name
                city VARCHAR(255),      -- City name (can be NULL if not applicable)
                category VARCHAR(255),  -- Category of the cost (e.g., Food, Transport)
                item VARCHAR(255),      -- Item name
                price VARCHAR(255)      -- Price of the item (stored as text for simplicity)
            );
            """
            cursor.execute(create_table_query)
            connection.commit()
            logger.success("Table 'cost_of_living' created successfully.")
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(f"Error creating table: {error}")
        finally:
            cursor.close()
            connection.close()
    else:
        logger.error("Failed to connect to the database.")
