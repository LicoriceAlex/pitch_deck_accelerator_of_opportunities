from bs4 import BeautifulSoup

import re

from selenium import webdriver
from selenium.webdriver.common.by import By

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

def initialise_driver():
    return webdriver.Chrome()


### что не работает
# RetailTech
# Web3
# Gaming выдаёт неправильную информацию
# FoodTech не работает, а вот Food Tech, работает
# Consumer Goods & Services неправильно
# Aero & SpaceTech неправильно
# Legal & RegTech неправильно
# Transport & Logistics неправильно

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
