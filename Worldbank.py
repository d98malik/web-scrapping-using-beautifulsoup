import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://data.worldbank.org/country"



def get_country_name(url):
    """
    This function takes a world bank site URL as input and scrapes the corresponding webpage 
    to extract the names of all the countries listed on the page. It returns a 
    list of country names.

    Parameters:
    url (str): The URL of the webpage to scrape.

    Returns:
    list: A list of strings, where each string represents the name of a country.
    """
    content = requests.get(url)
    soup = BeautifulSoup(content.text, 'lxml')

    #locating the required content from the main div
    main_div = soup.find('div', {'class': 'wrapper',"id":"main"})
    sub_main_div = main_div.find('div', {'class': 'overviewArea body'})
    all_a = sub_main_div.find_all('a')

    countries = []
    for a in all_a:
        countries.append(a.text)
    
    return countries

countries = get_country_name(url)


def get_country_data_link(country):
    data_links = []
    for country in countries:
        try:
            modified_url = url + "/" + country + "?view=chart"
            content = requests.get(modified_url)
            soup = BeautifulSoup(content.text, 'lxml')
            download_div = soup.find("div",{'class':'btn-item download'})
            excel_download_link = download_div.find_all('a')[2].get("href")
            data_links.append({f"{country}":excel_download_link})
            print(f"Successfuly extracted data link for {country}.") 
        except:
            print(f"Failed to extract data link for {country}.") 
            
    return data_links



