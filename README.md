# Job-Tracker
**Importing Libraries:**
The script starts by importing necessary libraries, including BeautifulSoup for web scraping, requests for making HTTP requests, and other libraries for data manipulation and visualization.
Fetching Data from the Website:

The script sends a request to the Shine job portal's URL and checks the response status.
It uses BeautifulSoup to parse the HTML content and extracts relevant job information such as titles, company names, locations, experience requirements, and vacancies.

**Data Cleaning:**
The extracted data is cleaned using regular expressions and string manipulations to remove unnecessary characters and spaces.
Creating a DataFrame:

The cleaned data is then organized into a Pandas DataFrame.

**Removing Duplicates:**
Duplicates in the DataFrame are identified based on job titles and removed.

**Web Scraping Multiple Pages:**
The script is designed to scrape job information from multiple pages (specified by the 'Range' variable) and combines the data into a single DataFrame.

**Data Analysis and Visualization:**
The script includes various visualizations using Seaborn and Matplotlib to analyze and present insights from the scraped job data. This includes visualizations for category distribution, positions histogram, firm-wise vacancy count, and category count plot.
