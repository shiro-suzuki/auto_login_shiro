from selenium import webdriver
from time import sleep
import datetime

url = 'https://dev104731.service-now.com/'
# url = 'https://scraping-for-beginner.herokuapp.com/login_page'

browser = webdriver.Chrome()
browser.get(url)

sleep(1)

# loginフォームのフォームの含まれるiframe要素を取得する
elem_login_iframe = browser.find_element_by_xpath("//*[@id='gsft_main']")

# 指定したiframe内へ移動
browser.switch_to_frame(elem_login_iframe)

# ユーザー名フォームの要素取得＋入力
elem_username = browser.find_element_by_id('user_name')
elem_username.send_keys('test.tester1')
# パスワードフォームの要素取得＋入力
elem_password = browser.find_element_by_id('user_password')
elem_password.send_keys('adminpass')

# sleep
sleep(1)

# ログインボタンの要素取得＋クリック
elem_login_btn = browser.find_element_by_id('sysverb_login')
elem_login_btn.click()

browser.switch_to.default_content()

# browser.get('https://dev104731.service-now.com/nav_to.do?uri=%2Fincident_list.do%3Fsysparm_userpref_module%3Db55b4ab0c0a80009007a9c0f03fb4da9%26sysparm_clear_stack%3Dtrue')
# Incidet: Create New
browser.get('https://dev104731.service-now.com/incident.do?sys_id=-1&sysparm_query=active=true&sysparm_stack=incident_list.do?sysparm_query=active=true')

elem_caller = browser.find_element_by_id('sys_display.incident.caller_id')
elem_caller.send_keys('1 tester')

sleep(1)

nowdate = datetime.datetime.now()
str_nowdate = nowdate.strftime('%Y-%m-%d %H:%M:%S')
send_shortdesc = 'TEST_' + str_nowdate

elem_shortdesc = browser.find_element_by_id('incident.short_description')
elem_shortdesc.send_keys(send_shortdesc)

elem_submit = browser.find_element_by_id('sysverb_insert_bottom')
elem_submit.click()

sleep(1)

browser.quit()

# Newボタンの要素取得＋クリック
# elem_incident_newbtn = browser.find_element_by_id('sysverb_new')
# elem_incident_newbtn.click()
