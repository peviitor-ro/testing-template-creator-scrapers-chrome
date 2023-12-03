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
#  run tests: pytest --verbose bunge_test.py
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
    get_logo_from_api,
)

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

    5) ---> get_logo_from_api(company_name: str) -> bool
    Aceasta functie verifica daca exista logo pentru companie cautata.
'''


def get_number_of_jobs_from_site(driver) -> list[dict]:
    '''
    ... a function that returns number of jobs from site.
    '''
    lst_dict = list()
    try:
        driver.get('{link_scraper}')
        links_titles = cautare_elemente_by_EC(driver, 'CLASS_NAME', 'jobTitle-link')
        for lt in links_titles:
            if lt.text.strip() != '':
                lst_dict.append(dict(job_title=lt.text.strip(), job_link=lt.get_attribute('href').strip()))
    except Exception as e:
        print(e)

    return sorted(lst_dict, key=lambda job: job['job_title'])


def test_logo_{nume_test_scraper}():
    '''
    ... test logo from peviitor API.
    '''
    logo = get_logo_from_api('bunge')
    assert logo == True


def test_equality_jobs_peviitor_and_company_site(driver_config):
    '''
    ... test every job_link from peviitor and {nume_test_scraper}.
    '''
    job_api = get_all_jobs_from_peviitor('{nume_test_scraper}')
    job_site = get_number_of_jobs_from_site(driver_config)

    # verification for job_site and job_api number
    assert len(job_site) == len(job_api)

    # verification for == job_site and job_api # # # # # # # # # # # # # # # #
    #
    for i in range(len(job_site)):
        if job_site[i]['job_title'] == job_api[i]['job_title'].strip() and job_site[i]['job_link'] == job_api[i]['job_link'].strip():
            pass
        else:
            raise AssertionError('Titlurile sau link-urile nu sunt identice.')
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # verification for job from peviitor with jobs from company site # # # # #
    #
    for idx, job in enumerate(job_site):
        driver_config.get(job['job_link'])

        title_ = cautare_element_by_EC(driver_config, 'ID', 'job-title')
        if title_:
            title_ = title_.text.strip()
            assert title_ == job_api[idx]['job_title'].strip()
        else:
            raise AssertionError('Titlul nu a fost gasit. Probabil 404 sau job expirat!')
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def test_ALL_TEST_PASSED():
    assert True
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
