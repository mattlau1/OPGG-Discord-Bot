'''
Gets runes from OP.GG by screenshotting rune page for champion in
specified lane.
'''
import io
from selenium import webdriver
from PIL import Image

def get_runes(champ, lane):
    '''
    Screenshots rune page for champion in specified lane and attempts
    to make background transparent.

    Input: Champion, Lane
    Returns: PIL image object
    '''
    # get screenshot of rune page
    google_chrome_options = webdriver.chrome.options.Options()
    google_chrome_options.headless = True
    google_chrome_options.add_argument('--window-size=568,300')
    web_driver = webdriver.Chrome(
        executable_path="/usr/bin/chromedriver",
        options=google_chrome_options
    )
    url = f"https://op.gg/champion/{champ}/statistics/{lane}"
    web_driver.get(url)
    element = web_driver.find_element_by_class_name('perk-page-wrap')
    element = element.screenshot_as_png
    web_driver.close()

    # start processing image byte by byte
    img = Image.open(io.BytesIO(element))
    img = img.convert("RGBA")
    data = img.getdata()

    # change bg
    new_data = []
    for item in data:
        if item[0] == 245 and item[1] == 245 and item[2] == 245:
            new_data.append((0, 0, 255, 0))
        else:
            new_data.append(item)

    # update img
    img.putdata(new_data)

    return img
