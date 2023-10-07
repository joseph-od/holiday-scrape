import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
URL = "https://www.kenwoodtravel.co.uk/holiday-search?search%5Btype%5D=package&search%5Bdestinations%5D%5B%5D=P32&search%5Bdeparture%5D=A11&search%5Bdeparture_date%5D=2024-09-02&search%5Bnights%5D%5B%5D=17&search%5Bpassengers%5D%5B0%5D%5Badults%5D=2&search%5Bpassengers%5D%5B0%5D%5Bchildren%5D=0&submit="
page = requests.get(URL, headers=headers, timeout=15)

soup1 = BeautifulSoup(page.content, "html.parser")
results = soup1.find(id="resultsContainer")

chrome_options = Options()
#chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
#chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
driver.implicitly_wait(10)
page_source = driver.page_source
driver.quit()
soup = BeautifulSoup(page_source, "html.parser")

# Find the element with the specified ID
results_container = soup.find(id="resultsContainer").find("dt", text="Total").find_next("dd").find("strong").text

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    print(results_container)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
