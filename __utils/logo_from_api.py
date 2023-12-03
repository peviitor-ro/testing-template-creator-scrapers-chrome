#
#
#
#
import requests
from .__config import DEFAULT_USER_AGENT


def get_logo_from_api(company_name: str) -> bool:
    """
    Get logo from pe viitor API.
    """

    response = requests.get(
        url='https://api.peviitor.ro/v1/logo/',
        headers={
            'User-Agent': DEFAULT_USER_AGENT,
        }
    ).json()["companies"]

    for item in response:
        if item['name'].lower() == company_name.lower().strip():
            if item['logo'] == '' or item['logo'].lower() == 'no logo found':
                return False
            else:
                return True

    return False
