# IMDB-Movie-Scraper

In this project, I have made a IMDB Scraper (https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in) in which I have scraped a total of 250 movies using BeautifulSoup and Requests Library, and performed different analysis based on years, decades, genres, directors, languages and casts. 
I have also stored all the data in the cache files in json format.

## Requirements

### BeautifulSoup

Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping. If you're using Linux based OS, you can install BeautifulSoup using following command in terminal.

Here, pip is a package-management system used to install and manage software packages written in Python.

```
sudo apt-get update && sudo apt-get install python3-pip
pip3 install beautifulsoup4
```

### Requests Library

Requests is an Apache2 Licensed HTTP library, written in Python. Requests will allow you to send HTTP/1.1 requests using Python.
You can install requests library using following code in your terminal in Linux.

`pip3 install requests`

After finishing installation process above, you can run the tasks, using `python3 file_name.py`.
