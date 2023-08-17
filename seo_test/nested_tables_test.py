import requests
from bs4 import BeautifulSoup


def has_nested_tables(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')
        # Find all table elements
        table_elements = soup.select("table")
        # Check for nested tables
        nested_tables = 0
        for table in table_elements:
            parent_tables = table.find_parents("table")
            if parent_tables:
                nested_tables += 1
        if nested_tables > 0:
            print(f"The page has {nested_tables} nested table(s).")
        else:
            print("The page does not have nested tables.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


# Replace this with the URL you want to check
url_to_check = "https://www.javatpoint.com/html-nested-table"
has_nested_tables(url_to_check)
