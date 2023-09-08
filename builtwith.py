import requests
from bs4 import BeautifulSoup


class BuiltWithParser:
    BASE_URL = 'https://builtwith.com/'
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0",
    }

    def __init__(self, domain: str):
        self.domain = domain.strip()

    def get_page_records(self):
        page = self.session.get(self.BASE_URL + self.domain, headers=self.headers)
        soup = BeautifulSoup(page.content, 'lxml')
        # print(soup.select_one('[class="card-body pb-0"] .card-title').text)
        cards = soup.select('[class="card-body pb-0"]')
        for card in cards:
            title = card.select_one('.card-title').text
            print(title)
            technologies = card.select('.row.mb-1.mt-1')
            technology_list = []
            for item in technologies:
                technology_name = item.select_one('h2 a').text
                sub_list = item.select('.row.mb-1')
                if sub_list:
                    sub_technologies = list(map(lambda x: x.select_one('a').text, item.select('.row.mb-1')))
                    technology_list.append({technology_name: sub_technologies})
                else:
                    technology_list.append({technology_name})
            print(technology_list)


if __name__ == '__main__':
    parser = BuiltWithParser('4phones.eu')
    parser.get_page_records()
