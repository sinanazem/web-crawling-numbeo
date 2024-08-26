# Numbeo Cost of Living Data Scraper

This project is a web scraping tool designed to extract cost of living data from the [Numbeo](https://www.numbeo.com/cost-of-living/) website. The data can be used for various analyses, such as comparing living costs between different cities or countries.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Scrape Cost of Living Data**: Extracts detailed cost of living data including rent, groceries, transportation, and more.
- **Customizable Scraping**: Easily adjust the script to scrape data for specific cities or countries.
- **Output in Various Formats**: Save the scraped data in formats such as CSV, JSON, or Excel for further analysis.

## Installation

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/numbeo-scraper.git
cd numbeo-scraper
```

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

To scrape data, run the following command:

```bash
python scraper.py
```

You can customize the cities or countries you want to scrape by modifying the `config.json` file:

```json
{
    "cities": ["New York", "London", "Tokyo"]
}
```

The scraped data will be saved in the `output/` directory by default.

### Command-Line Arguments

You can also pass command-line arguments to customize the scraping process:

```bash
python scraper.py --city "New York" --output-format "csv"
```

## Dependencies

- Python 3.x
- Requests
- BeautifulSoup
- Pandas

These dependencies are listed in the `requirements.txt` file.

## Project Structure

```plaintext
numbeo-scraper/
│
├── scraper.py             # Main script for scraping data
├── config.json            # Configuration file for cities/countries
├── requirements.txt       # List of dependencies
├── output/                # Directory where scraped data is saved
│   └── example.csv
├── README.md              # Project documentation
└── LICENSE                # License information
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to follow the coding guidelines and write tests for any new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Numbeo](https://www.numbeo.com) for providing the data source.
- Contributors and open-source community for their valuable input.
