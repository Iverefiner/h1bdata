import bs4
from pathlib import Path
import requests

class get_file:

    def __init__(self):
        self.BASE_URL = 'https://www.dol.gov'
        self.query = ''
        self.soup = ''

        return self

    def scrape_dom():

# function to extract html document from given url
        def getHTMLdocument(url):
    # request for HTML document of given url
            response = requests.get(url)
    # response will be provided in JSON format
            return response.text

        url_to_scrape = 'https://www.dol.gov/agencies/eta/foreign-labor/performance'

# create document
        html_document = getHTMLdocument(url_to_scrape)

# create soup object
        soup = bs4.BeautifulSoup(html_document, 'html.parser')

        return soup

# asks the user to input year and date to filter out search query/download only one file

    def get_user_input():
        year = ""
        quarter = ""
        
        while (year.isnumeric() != True):
            year = input('Enter the desired year: ')

        quarter = input('Which quarter? (Q1, Q2, Q3, Q4): ')

        query = f'a[href*=LCA_Disclosure_Data_FY{year}_{quarter}]'

        return query

# Find the links to the relevant excel files

    def download_file(self):
        matching_tag_elements = self.soup.select(self.query)


        for tag_element in matching_tag_elements:

    # tag_element is the entire class a tag that contains the href so this will extract the value of href
            path = tag_element['href']

    # href value is the  subdirectory so it's combined with the main website URL
            file_url = self.BASE_URL + path
    # Download file to memory
            response = requests.get(file_url)

    # Create folder to hold the data
            if not Path('data').is_dir():
                Path('data').mkdir()

    # Save the data in memory to disk
            file_name = f"data/{file_url.split('/')[-1]}"
            with open(file_name, 'wb') as output_file:
                output_file.write(response.content)

# EXECUTE FUNCTIONS
get_file.scrape_dom()
get_file.get_user_input()
get_file.download_file()