#
#
#
#  Build for Chrome extension
#  Module OOP for full functionality testing
#  -------------------
#  Default CHROME driver build
#  -------------------
#  Project build by Andrei Cojocaru
#  Github: https://github.com/andreireporter13
#  LinkedIn: https://www.linkedin.com/in/andrei-cojocaru-985932204/
#
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
from typing import Final

# special dict
BY_MAP: Final = {
                'ID': By.ID,
                'TAG_NAME': By.TAG_NAME,
                'CLASS_NAME': By.CLASS_NAME,
                'CSS': By.CSS_SELECTOR
            }


def cautare_element_by_EC(driver, by_name, element):
    '''
    ... search element by EC...
    '''

    wait = WebDriverWait(driver, 10)
    by = BY_MAP.get(by_name)
    if by is None:
        raise ValueError(f'Invalid "by_name" value: {by_name}')

    return wait.until(EC.visibility_of_element_located((by, element)))


def cautare_elemente_by_EC(driver, by_name, element):
    '''
    ... search elements by EC ...
    '''

    wait = WebDriverWait(driver, 10)
    by = BY_MAP.get(by_name)
    if by is None:
        raise ValueError(f'Invalid "by_name" value: {by_name}')

    return wait.until(EC.presence_of_all_elements_located((by, element)))
