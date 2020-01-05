from selenium import webdriver
import pickle, time, sys
print(
'''
_________ .__            __
\\_   ___ \\|  |__ _____  |  | ______________
/    \\  \\/|  |  \\\\__  \\ |  |/ /\\_  __ \\__  \\
\\     \\___|   Y  \\/ __ \\|    <  |  | \\// __ \\_
 \\______  /___|  (____  /__|_ \\ |__|  (____  /
        \\/     \\/     \\/     \\/            \\/
    > Chakra Engine [v1.] Instagram Story Reader
    by aaaddress1@chroot.org
''')

web = webdriver.Chrome("chromedriver.exe")

web.get('https://www.instagram.com/')
for cookie in  pickle.load(open('igSession.pkl', 'rb')):
    if 'expiry' in cookie:
         del cookie['expiry']
    web.add_cookie(cookie)
web.get('https://www.instagram.com/')
web.set_window_position(0,0)
web.set_window_size(1200,1200)

alertBtn = web.find_elements_by_xpath('//button[contains(text(), "稍後再說")]')
if len(alertBtn) > 0:
    alertBtn[0].click()
    time.sleep(1)

while True:
    try:
        web.find_element_by_link_text('全部觀看').click()
        break
    except Exception as e:
        time.sleep(1)
        pass

while True:
    time.sleep(1.5)
    try:
        web.find_element_by_class_name('coreSpriteRightChevron').click()
        usrname = web.find_element_by_xpath('//a[string(text())]').text
        print(f"read {usrname}'s story.")
    except Exception as e:
        print(e)
        web.quit()
        sys.exit(0)
