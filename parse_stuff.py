from bs4 import BeautifulSoup

import re

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def money_from_str(text):
    pattern = r"(\d+(?:[.,]\d+)?)\s*(трлн|млрд|млн)"
    result = re.search(pattern, str(text))
    return result

def make_total(result):
    if result.group(2) == "млн": d = 10**6
    elif result.group(2) == "млрд" : d = 10**9
    elif result.group(2) == "трлн" : d = 10**12
    else: raise RuntimeError(f"{result.group(2)} is not unsderstood")
    
    m = float(result.group(1).replace(',', '.'))
    total = int(m * d)
    
    return total

def text2money(text):
    money = money_from_str(text)
    if money:
        return make_total(money)

### что не работает
# RetailTech
# Web3
# Gaming выдаёт неправильную информацию
# FoodTech не работает, а вот Food Tech, работает
# Consumer Goods & Services неправильно
# Aero & SpaceTech неправильно
# Legal & RegTech неправильно
# Transport & Logistics неправильно

def initialise_driver():
    return webdriver.Chrome()

def parse_money(driver, market : str):
    """
    driver = initialise_driver()
    money = parse_money(driver, "IndustrialTech") # Объём рынка
    """
    
    driver.get('http://www.google.com')

    search = driver.find_element(By.NAME, 'q')
    # search.send_keys("tadviser какой объём рынка в россии AI")
    search.send_keys(f"tadviser какой объём рынка в России {market}")
    search.send_keys(Keys.RETURN) # hit return after you enter search text
    sleep(.5)
    
    html = driver.page_source
    
    soup = BeautifulSoup(html, 'html.parser')
    
    if str(soup).find("Выделенное описание из Интернета") != -1: # если есть быстрый ответ
        elems = soup.find_all('span', {"class" : "hgKElc"})

        if elems:
            elems = soup.find_all('span', {"class" : "ILfuVd"})
            text = elems[0].find_all('b')[0]
            
        money = money_from_str(text)
        if money:
            return make_total(money)

    else: # берём с описания первых 2 сайтов
        texts = soup.find_all('div', {"class" : "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"})
        text = texts[0].get_text()
        
        money = money_from_str(text)
        if money:
            return make_total(money)
        
        text = texts[1].get_text()
        
        money = money_from_str(text)
        if money:
            return make_total(money)
        
    raise RuntimeError("Can't parse money")

def initialise_driver():
    
    driver = webdriver.Chrome()
    
    width = 500
    height = 400
    driver.set_window_size(width, height)

    return driver


def get_revenue(soup):
    numbers = soup.find_all("tspan")
    
    for i in range(len(numbers)):
        text = numbers[i]
        
        if "Выручка:" in text:
            break
            
    num = numbers[i+1].get_text()
    
    num = num.replace("руб.", "")
    num = re.sub("\s+", "", num)
    
    return int(num)


def get_all_revenue(driver, url, local=False):
    # driver.get('https://zachestnyibiznes.ru/company/ul/1027402055251_7444020700_OOO-KOMPAS-PLYuS/statistics')
    # driver.get('https://zachestnyibiznes.ru/company/ul/1027700229193_7736207543_OOO-YaNDEKS/statistics')
    driver.get(url)

    # WebDriverWait(driver, 10) #.until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    sleep(.5)
    
    if not local:
        elem = driver.find_elements(By.XPATH, "//*[contains(text(), 'Российская Федерация')]")
        elem[0].click()
        sleep(.5)
    
    elem = driver.find_elements(By.CLASS_NAME, "highcharts-point")[8]
    elem.click()
    elem.click()
    
    sleep(0.5)
    
    # html = driver.find_element(By.CLASS_NAME, "highcharts-root").click()
    elem = driver.find_element(By.CLASS_NAME, "highcharts-root")
    html = elem.get_attribute('outerHTML')
    
    soup = BeautifulSoup(html, 'html.parser')
    
    return get_revenue(soup)

def parse_conc(driver, okved : str = "010000"):
    url = f"https://checko.ru/company/select?code={okved}"
    
    driver.get(url)
    
    sleep(0.5)
    
    # elem = driver.find_element(By.CLASS_NAME, "slide-checkbox")
    elem = find_by_name(driver, "Только действующие", False)

    elem.click()

    sleep(.5)
    
    elem = driver.find_element(By.CLASS_NAME, "uk-table-responsive")
    
    conck = []
    conck.append(elem.find_elements(By.TAG_NAME, "tr")[0].find_element(By.CLASS_NAME, "link").get_attribute('title'))
    conck.append(elem.find_elements(By.TAG_NAME, "tr")[1].find_element(By.CLASS_NAME, "link").get_attribute('title'))
    conck.append(elem.find_elements(By.TAG_NAME, "tr")[2].find_element(By.CLASS_NAME, "link").get_attribute('title'))
    
    return conck

def find_by_name(driver, text, explicit=False):
    if not explicit:
        return driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
    return driver.find_element(By.XPATH, f"//div[text()='{text}']")

def get_parent(elem):
    return elem.find_element(By.XPATH, "./..")

def get_tam_sam_som(driver, region="Москва", okved="611000", market="Gaming", our_part=0.05):
    driver.get("https://zachestnyibiznes.ru/search?query=#")
    sleep(10)
    
    button = driver.find_element(By.CLASS_NAME, "serach-filter-button-sm")
    button.click()
    sleep(.5)
    
    # elem = driver.find_element(By.CLASS_NAME, "slide-checkbox")
    elem = find_by_name(driver, " ИП", False)
    elem.click()
    sleep(.5)
    
    # elem = driver.find_element(By.CLASS_NAME, "slide-checkbox")
    elem = find_by_name(driver, "Статус", False)
    elem.click()
    sleep(.5)
    
    elem = driver.find_element(By.CLASS_NAME, "custom-checkbox") # действующее
    elem.click()
    sleep(.5)
    
    # Вид деятельности (ОКВЭД)

    # elem = driver.find_element(By.CLASS_NAME, "slide-checkbox")
    elem = find_by_name(driver, "Вид деятельности (ОКВЭД)", False)
    elem.click()
    sleep(.5)
    
    # Вид деятельности (ОКВЭД)

    elem = driver.find_element(By.NAME, okved[:2])
    # elem = find_by_name(driver, "61", False)
    elem = elem.find_element(By.XPATH, "following-sibling::*[1]")
    elem.click()
    sleep(.5)
    
    
    # Вид деятельности (ОКВЭД)
    elem = find_by_name(driver, "Готово", False)
    elem.click()
    sleep(.5)
    
    
    # регион
    # elem = driver.find_element(By.CLASS_NAME, "slide-checkbox")
    elem = find_by_name(driver, "Регион", False)

    elem.click()

    sleep(.5)
    
    
    # регион
    # elem = driver.find_element(By.CLASS_NAME, "slide-checkbox")
    elem = find_by_name(driver, region, False)
    elem.click()
    sleep(.5)
    
    
    # Поиск
    elem = driver.find_element(By.CLASS_NAME, "btn-danger")
    # elem = find_by_name(driver, " Искать ", True)

    elem.click()
    sleep(.5)
    button.click()
    sleep(.5)
    
    
    # регион
    # elem = driver.find_element(By.CLASS_NAME, "slide-checkbox")
    elem = find_by_name(driver, "ООО", False)

    elem.get_attribute("href")

    # sleep(.5)
    
    href = elem.get_attribute("href") + r"/statistics"
    
    tam = get_all_revenue(driver, href)
    
    sam = parse_money(driver, market)
    
    som = int(sam * our_part)
    
    conc = parse_conc(driver, okved)
    
    return tam, sam, som, conc

driver = initialise_driver()

tam, sam, som, conc = get_tam_sam_som(driver, region="Москва", okved="611000", market="Gaming", our_part=0.05)

driver.quit()