from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image

def get_runes(champ, lane):
    googleChromeOptions = webdriver.chrome.options.Options()
    googleChromeOptions.headless = True
    googleChromeOptions.add_argument('--window-size=568,300')
    googleChrome = webdriver.Chrome(executable_path="/usr/bin/chromedriver",
    options=googleChromeOptions)
    pageUrl = f"https://oce.op.gg/champion/{champ}/statistics/{lane}"
    googleChrome.get(pageUrl)
    element = googleChrome.find_element_by_class_name('perk-page-wrap')
    element = element.screenshot_as_png

    
    with open('images/out.png', 'wb') as f:
        f.write(element)

    img = Image.open('images/out.png')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 245 and item[1] == 245 and item[2] == 245:
            newData.append((0, 0, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("images/out2.png", "PNG")
    googleChrome.close()

if __name__ == "__main__":
    get_runes('twistedfate', 'mid')
    get_runes('katarina', 'jg')