from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_runes(champ, lane):
    googleChromeOptions = webdriver.chrome.options.Options()
    googleChromeOptions.headless = True
    googleChromeOptions.add_argument('--window-size=1920,1080')
    googleChrome = webdriver.Chrome(executable_path="/usr/bin/chromedriver",
    options=googleChromeOptions)
    pageUrl = f"https://oce.op.gg/champion/{champ}/statistics/{lane}"
    googleChrome.get(pageUrl)
    element = googleChrome.find_element_by_class_name('perk-page-wrap')
    element = element.screenshot_as_png

    with open('images/out.png', 'wb') as f:
        f.write(element)
    googleChrome.close()

if __name__ == "__main__":
    get_runes('twistedfate', 'mid')
    get_runes('katarina', 'jg')