# Numbeo Web Crawling Project
<img src="https://pngimg.com/uploads/world_map/world_map_PNG28.png" width=550>

This project involves scraping cost of living data from the Numbeo website, storing the data in a PostgreSQL database, and using Docker to manage the environment.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)

## Overview

The goal of this project is to extract country names from the Numbeo website, create a PostgreSQL database to store the cost of living data, and scrape cost of living information for each country and city. The project uses Docker and Docker Compose for containerization and environment management.

## Project Structure

Here's a brief overview of the project structure:

```
.
├── Dockerfile
├── LICENSE
├── README.md
├── docker-compose.yaml
├── notebooks
│   ├── numbeo-v2.ipynb
│   ├── numbeo-v3.ipynb
│   ├── numbeo-v4.ipynb
│   └── numbeo.ipynb
├── requirements.txt
└── src
    ├── country_name_extractor.py
    ├── numbeo_web_crawler.py
    ├── run.py
    └── utils
        └── db.py
```

- `Dockerfile`: Defines the Docker image for the project.
- `docker-compose.yaml`: Configuration for Docker Compose to set up services.
- `requirements.txt`: Python package dependencies.
- `src/`: Source code directory.
  - `country_name_extractor.py`: Extracts country names from the Numbeo website.
  - `numbeo_web_crawler.py`: Scrapes cost of living data.
  - `run.py`: Entry point for executing the project.
  - `utils/db.py`: Utility functions for database operations.
- `notebooks/`: Jupyter notebooks for analysis and experimentation.

## Requirements

Before setting up the project, ensure you have the following installed on your system:

- Docker
- Docker Compose
- Python 3.11 or later

## Setup and Installation

Follow these steps to set up the project:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sinanazem/numbeo-web-crawling.git
   cd web-crawling-numbeo
   ```

2. **Build and Start Docker Containers**

   Build the Docker image and start the containers using Docker Compose:

   ```bash
   docker-compose up --build
   ```

   This will create and start the necessary containers for the project, including the PostgreSQL database.

3. **Access the Docker Container**

   You can access the running container to interact with the application:

   ```bash
   docker-compose exec app /bin/bash
   ```

4. **Install Python Dependencies**

   Inside the container, install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Extract Country Names**

   Run the script to extract country names:

   ```bash
   python src/country_name_extractor.py
   ```

2. **Scrape Cost of Living Data**

   Execute the web crawler to scrape the cost of living data:

   ```bash
   python src/numbeo_web_crawler.py
   ```

3. **Run the Application**

   To run the full application:

   ```bash
   python src/run.py
   ```

