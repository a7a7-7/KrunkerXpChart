from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
import time
from constants.enums.weap_info import weapClass
from bs4 import BeautifulSoup
import graph

# input username
user = input("Type user name:")
# weap_xp = input("weapon:")
classes = weapClass.classes 
weaps = weapClass.weaps
weap_xp_ori = [0 for i in range(14)]
weap_xp = [0 for i in range(14)]
i = 0

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument('--disk-cache-dir=C:\\Users\\Admin\\a6a6\\krunkers\\browser_cache')
options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 2,
        }
)
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"

#       execute chrome webdriver
#   * chromedriver now works for me *
#       !!chrome number one!!
driver = webdriver.Chrome(options=options)
driver.get('https://krunker.io/social.html?p=profile&q={}'.format(user))

# wait for website loading
# Accept privacy policy
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()
logging.info('website loaded successfully!')

# Get user's clan
def user_clan():
    clan = driver.find_elements(by=By.XPATH, value='/html/body/div[2]/div[9]/div[1]/div[3]/div[2]/a')[0].text

    return clan

html_content = driver.page_source

# print(html_content)

# input()
soup = BeautifulSoup(html_content, 'html.parser')
##main_stat_divs = soup.body.find_all("div", {"class": "pSt"})
class_xp_divs = soup.body.find_all("div", {"class": "classCard"})

print("General Stats")

##for div in main_stat_divs:
##    print(div.get_text())

print("\nClass Stats")

i = 0
for div in class_xp_divs:
    weap_xp_ori[i] = div.get_text()
    i += 1

j = 0
for i in weap_xp_ori:
    tmp = i.replace(classes[j] + weaps[j], " ")
    tmp = tmp.split('/')[0]
    weap_xp[j] = tmp
    j += 1

# Close the browser window
driver.quit()

graph.stat_graph(weap_xp, user)