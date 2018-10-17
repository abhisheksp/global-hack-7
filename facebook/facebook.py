import json
from time import sleep

from browser import get_browser_driver

driver = get_browser_driver()


def initial_setup():
    with open('creds.json') as f:
        data = json.load(f)
        username = data['username']
        password = data['password']

    def fb_login(username, password):
        driver.get('https://www.facebook.com')
        driver.find_element_by_id('email').send_keys(username)
        driver.find_element_by_id('pass').send_keys(password)
        driver.find_element_by_id('loginbutton').click()

    fb_login(username, password)
    sleep(1)


initial_setup()


def group_link(group_id):
    return 'https://www.facebook.com/groups/{}/'.format(group_id)


def group_post(message, group_ids):
    for group_id in group_ids:
        group_url = group_link(group_id)
        driver.get(group_url)
        post_box = driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
        post_box.send_keys(message)
        post_button = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']")
        while True:
            cursor = post_button.find_element_by_tag_name('span').value_of_css_property("cursor")
            if cursor == "pointer":
                break
        post_button.click()
        sleep(2)
    return 'Message Posted!'
