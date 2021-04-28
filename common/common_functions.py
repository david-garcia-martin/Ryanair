import configparser
import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common import keys

import HtmlTestRunner


configParser = configparser.RawConfigParser()
configParser.read(rf'{os.path.join(os.path.dirname(__file__), "Ryanair_config.txt")}')

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
html_report_folder = rf'{os.path.join(parent_directory,configParser.get("ryanair-config", "html_report_folder"))}'
url = configParser.get('ryanair-config', 'url')
browser = configParser.get('ryanair-config', 'browser')

origin = configParser.get('ryanair-config', 'origin')
destination = configParser.get('ryanair-config', 'destination')
adults = int(configParser.get('ryanair-config', 'adults'))
children = int(configParser.get('ryanair-config', 'children'))

email = configParser.get('ryanair-config', 'email')
password = configParser.get('ryanair-config', 'password')
phone_number = configParser.get('ryanair-config', 'phone_number')
cc = configParser.get('ryanair-config', 'cc')
cc_cvv = configParser.get('ryanair-config', 'cc_cvv')
address = configParser.get('ryanair-config', 'address')
address2 = configParser.get('ryanair-config', 'address2')
city = configParser.get('ryanair-config', 'city')
country = configParser.get('ryanair-config', 'country')
zip_code = configParser.get('ryanair-config', 'zip_code')


def randomize_list(list_to_randomize, return_slice=None):
    new_list = []
    while list_to_randomize:
        index = random.randrange(len(list_to_randomize))
        new_list.append(list_to_randomize[index])
        list_to_randomize.remove(list_to_randomize[index])
    return new_list[:return_slice]


def random_phrase(letters, length_of_word):
    import string
    if not letters:
        letters = []
        for alpha in range(52):
            letters.append(string.ascii_letters[alpha])
        letters = randomize_list(letters, length_of_word)
        letters = "".join(letters)
    from itertools import permutations
    random_list = []
    for word in permutations(letters, length_of_word):
        rand_phrase = "".join(word)
        random_list.append(rand_phrase)
    word = random.choice(random_list)
    return word


def random_word(letters=None, length_of_word=4, words_in_sentence=5):
    rand_word = None
    if words_in_sentence:
        rand_word = ''
        for x in range(words_in_sentence):
            rand_word += random_phrase(letters, length_of_word)
            if x < words_in_sentence - 1:
                rand_word += ' '
    return rand_word


def get_random_fn_and_ln():
    fn_ln = []
    for i in range(adults + children):
        fn = random_word(length_of_word=6, words_in_sentence=1).title()
        ln = random_word(length_of_word=6, words_in_sentence=1).title()
        fn_ln.extend([fn, ln])
    return fn_ln


def initiate_driver(browser):
    driver = None
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    elif browser == 'Edge':
        driver = webdriver.Edge()
    driver.maximize_window()
    return driver


def get_report_description():
    current_ver = 'version_test_prod'
    if 'qa' in url:
        env = 'QA'
    else:
        env = 'PROD'
    report_description = {'Code': current_ver, 'Env': env}
    return report_description


def html_test_reporter_util(suite, suite_name, title, description):
    html_report_template = os.path.join(os.path.dirname(__file__), 'html_reports_template.html')

    required_args = ' | '.join('{0}: {1}'.format(key, val) for key, val in sorted(description.items()))

    html_template_args = {'report_description': required_args}

    runner = HtmlTestRunner.HTMLTestRunner(output=html_report_folder, template=html_report_template,
                                           combine_reports=True, template_args=html_template_args,
                                           report_name=suite_name, report_title=title, add_timestamp=True)
    runner.run(suite)
    test_print(f'Tests completed!!! HTML Report can be found at: {html_report_folder}', flash='/')


def test_print(print_statement, flash='#'):
    print(len(print_statement) * flash)
    try:
        print(print_statement)
    except:
        print((repr(print_statement)))
    print(len(print_statement) * flash)


def wait_for_element(driver, index=0, attempts=10, css_select=None):
    some_element = None
    counter = 1
    while not some_element:
        try:
            some_element = driver.find_elements_by_css_selector(css_select)[index]
        except:
            test_print('ELEMENT NOT FOUND - Attempt {0} of {1}'.format(counter, attempts))
            time.sleep(1)
        counter += 1
        if counter > attempts and not some_element:
            raise Exception('Element not found after {0} attempts!'.format(attempts))
            # noinspection PyUnreachableCode
            break
    return some_element


def wait_for_elements(driver, index=0, attempts=10, css_select=None):
    wait_for_element(driver, index=index, attempts=attempts, css_select=css_select)
    some_elements = driver.find_elements_by_css_selector(css_select)
    return some_elements


def wait_for_element_text(driver, index=0, attempts=10, css_select=None):
    element_text = ''
    counter = 1
    while element_text == '':
        try:
            element_text = driver.find_elements_by_css_selector(css_select)[index].text
        except:
            test_print('TRYING TO GET TEXT - Attempt {0} of {1}'.format(counter, attempts))
            time.sleep(1)
        if element_text != '':
            break
        else:
            counter += 1
            time.sleep(1)
        if counter >= attempts:
            raise Exception('ERROR: Did not find text after {0} attempts!'.format(attempts))

    return element_text


def wait_click(driver, index=0, attempts=10, css_select=None):
    try:
        driver.find_elements_by_css_selector(css_select)[index].click()
    except:
        wait_for_element(driver, index=index, attempts=attempts, css_select=css_select)
        while attempts > 0:
            try:
                driver.find_elements_by_css_selector(css_select)[index].click()
                break
            except:
                test_print('UNABLE TO CLICK ELEMENT - Attempt {0}'.format(attempts))
                attempts -= 1
                time.sleep(1)
            if attempts == 0:
                raise Exception('Unable to click element after {0} attempts!'.format(attempts))


def wait_click_url(driver, attempts=10, index=0, css_select=None):
    chk_url = driver.current_url
    counter = 1
    while chk_url == driver.current_url:
        try:
            driver.find_elements_by_css_selector(css_select)[index].click()
        except:
            test_print('UNABLE TO CLICK ELEMENT - Attempt {0} of {1}'.format(counter, attempts))
            time.sleep(1)

        counter += 1
        time.sleep(1)

        if counter == attempts:
            raise Exception('Clicked element, but url did not change after {0} attempts!'.format(attempts))


def wait_write(driver, text_to_write, attempts=10, index=0, css_select=None):
    wait_for_element(driver, attempts=attempts, index=index, css_select=css_select)
    while attempts > 0:
        try:
            textfield = driver.find_elements_by_css_selector(css_select)[index]
            textfield.send_keys(keys.Keys().COMMAND, 'a')
            textfield.send_keys(keys.Keys().DELETE)
            textfield.send_keys('{0}'.format(text_to_write))
            break
        except:
            test_print('UNABLE TO WRITE TO ELEMENT - Attempt {0}'.format(attempts))
            attempts -= 1
            time.sleep(1)
        if attempts == 0:
            raise Exception('Unable to write to element after {0} attempts!'.format(attempts))
