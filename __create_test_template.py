#
#
#
#  New Template for testing in Python
#  ... project made by Andrei Cojocaru &
#  LinkedIn: https://www.linkedin.com/in/andrei-cojocaru-985932204/
#  Github: https://github.com/andreireporter13
#  Echipa de testeri de la Peviitor.ro
#
#  Makek new template for testing:
#  python3 __create_test_template.py "nume_scraper" "link_scraper"
#
import sys
import os


def create_test_template(nume_test_scraper: str, link_scraper: str):
    config_content = f"""#
#
#  General Test Template
#  Selenium + Chrome Driver
#  ... and EC elements for testing
#
#
# Test Name ---> {nume_test_scraper}
# Link Scraper ------> {link_scraper}
#
#
from __utils import (
    cautare_element_by_EC,
    cautare_elemente_by_EC,
    driver_config,
    get_jobs_num_from_peviitor,
    get_all_jobs_from_peviitor,
)
import pytest

'''
    Testare Automata cu Selenium + Chrome Driver

    Deci:
    ########################################################################
    1) ---> function cautare_element_by_EC(driver, by_name, element):
    ... in loc de by_name se pune: ID, TAG_NAME, CLASS_NAME, CSS
    ... si element este un element din pagina pe care vrem sa-l cautam

    b.-> functia cautare_elemente_by_EC(by_name, element)
    ... in loc de by_name se pune: ID, TAG_NAME, CLASS_NAME, CSS
    ... si elementele pe care vrem sa le cautam in pagina

    ########################################################################

    2) ---> driver_config() definit la nivel de decorator @pytest.fixture(scope="session")
    ... daca vreti sa vedeti browserul,
    ---> si headless: bool = True, daca vreti sa rulati testele pe fundal,
    ... fara browser deschis.

    ########################################################################

    3) ---> get_jobs_num_from_peviitor(company: str)
    ... returneaza numarul de job-uri din API peviitor

    ########################################################################

    4) ---> get_all_jobs_from_peviitor(company: str)
    ... returneaza o lista cu dictionare care contine titluri si link-uri.
    Se acceseaza exact dupa aceleasi chei ca la scraperi:
    - job_link
    - job_title
'''


def get_number_of_jobs_from_site() -> list[dict]:
    '''
    ... a function that returns number of jobs from site.
    '''
    lst_dict = list()
    try:
        driver.get('{link_scraper}')
        links_titles = search.cautare_elemente_by_EC('CLASS_NAME', 'jobTitle-link')
        for lt in links_titles:
            if lt.text.strip() != '':
    except Exception as e:
        print(e)
    finally:
        driver.quit()

    return sorted(lst_dict, key=lambda job: job['job_title'])


def test_{nume_test_scraper.lower()}():

    job_site = get_number_of_jobs_from_site()
    job_api = get_all_jobs_from_peviitor('{nume_test_scraper}')

    # verification for job_site and job_api number
    assert len(job_site) == len(job_api)

    # verification for == job_site and job_api
    for i in range(len(job_site)):
            pass
        else:
            raise AssertionError('Titlurile sau link-urile nu sunt identice.')


def test_final_FLAG():
    print("\n=== Testele au fost rulate cu succes ===\n")
"""

    with open(f'{nume_test_scraper.lower()}_test.py', 'w') as f:
        f.write(config_content)
    print(f'Template test {nume_test_scraper.lower()}_test.py was succesfully created!')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 create_test_template.py \"nume_test_scraper\" \"link_scraper\"")
    else:
        nume_test_scraper = sys.argv[1]
        link_scraper = sys.argv[2]

        # Verificați dacă fișierul scraper există deja sau nu
        if os.path.exists(f'{nume_test_scraper.lower()}_test.py'):
            print(f"File {nume_test_scraper.lower()}_test.py already exists!")
        else:
            create_test_template(nume_test_scraper, link_scraper)
