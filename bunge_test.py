#
#
#  General Test Template
#  Selenium + Chrome Driver
#  ... and EC elements for testing
#
#
# Test Name ---> bunge
# Link Scraper ------> https://peviitor.ro/rezultate?q=bunge&country=Rom%C3%A2nia&page=1
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
    1) ---> Clasa TestChrome:
    ... are doua metode:
    a.-> driver.cautare_element_by_EC(by_name, element)
    ... in loc de by_name se pune: ID, TAG_NAME, CLASS_NAME, CSS
    ... si element este un element din pagina pe care vrem sa-l cautam

    b.-> driver.cautare_elemente_by_EC(by_name, element)
    ... in loc de by_name se pune: ID, TAG_NAME, CLASS_NAME, CSS
    ... si elementele pe care vrem sa le cautam in pagina

    ########################################################################

    2) ---> chromedriver_config(headless: bool = False,
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


def get_number_of_jobs_from_site(driver) -> list[dict]:
    '''
    ... a function that returns number of jobs from site.
    '''
    lst_dict = list()
    try:
        driver.get('https://jobs.bunge.com/search/?createNewAlert=false&q=&locationsearch=Romania&optionsFacetsDD_country=')
        links_titles = cautare_elemente_by_EC(driver, 'CLASS_NAME', 'jobTitle-link')
        for lt in links_titles:
            if lt.text.strip() != '':
                lst_dict.append(dict(job_title=lt.text.strip(), job_link=lt.get_attribute('href').strip()))
    except Exception as e:
        print(e)

    return sorted(lst_dict, key=lambda job: job['job_title'])


def test_logo_bunge():
    '''
    ... test logo from peviitor API.
    '''
    logo = get_logo_from_api('bunge')
    assert logo


def test_every_job_link_from_site(driver_config):
    '''
    ... test every job_link from site.
    '''
    job_api = get_all_jobs_from_peviitor('bunge')
    job_site = get_number_of_jobs_from_site(driver_config)

    # verification for job_site and job_api number
    assert len(job_site) == len(job_api)

    # verification for == job_site and job_api # # # # # # # # # # # # # # # #
    for i in range(len(job_site)):

        # ## ## ## ## ## ## ## ##
        if job_site[i]['job_title'] == job_api[i]['job_title'].strip():
            pass
        else:
            raise AssertionError('Titlurile nu sunt identice.')

        # ## ## ## ## ## ## ## ##
        if job_site[i]['job_link'] == job_api[i]['job_link'].strip():
            pass
        else:
            raise AssertionError('Link-urile nu sunt identice.')
    #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # verification for job from peviitor with jobs from company site # # # # #
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
