#
#
#
#  API peviitor test
#  https://api.peviitor.ro
#
#
from typing import Final
import requests
#
from .__config import DEFAULT_USER_AGENT

HEADERS_GET: Final = {
    'authority': 'api.peviitor.ro',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.8',
    'origin': 'https://peviitor.ro',
    'referer': 'https://peviitor.ro/',
    'sec-fetch-site': 'same-site',
    'user-agent': DEFAULT_USER_AGENT,
}


def get_jobs_num_from_peviitor(company: str) -> int:
    '''
    ... this func return all jobs from peviitor API.
    '''

    response = requests.get(
        f'https://api.peviitor.ro/v3/search/?q={company.lower()}&country=Rom%C3%A2nia&page=1',
        headers=HEADERS_GET
    )

    return response.json()['response']['numFound']


def get_all_jobs_from_peviitor(company: str) -> list:
    '''
    ... this func return all jobs from peviitor API.
    '''
    dict_with_titles_links = list()
    page = 1

    response = requests.get(
        f'https://api.peviitor.ro/v3/search/?q={company.lower()}&country=Rom%C3%A2nia&page={page}',
        headers=HEADERS_GET,
    )

    if len(response.json()['response']['docs']) < 10:
        for lt in response.json()['response']['docs']:
            dict_with_titles_links.append({
                'job_title': lt['job_title'][0],
                'job_link': lt['job_link'][0],
            })
    elif len(response.json()['response']['docs']) == 10:

        while len(response.json()['response']['docs']) != 0:
            response = requests.get(
                f'https://api.peviitor.ro/v3/search/?q={company.lower()}&country=Rom%C3%A2nia&page={page}',
                headers=HEADERS_GET,
            )
            for lt in response.json()['response']['docs']:
                dict_with_titles_links.append({
                    'job_title': lt['job_title'][0],
                    'job_link': lt['job_link'][0],
                })

            page += 1

    return sorted(dict_with_titles_links, key=lambda job: job['job_title'])
