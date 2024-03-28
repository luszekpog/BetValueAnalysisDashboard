from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from io import StringIO
import datetime
import pandas as pd 

options  = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)
current_date = datetime.datetime.now()
    
def handleScrapping():
    #getting element using selenium scrapper
    try:
        xpath = '//table[@id="team_misc"]'
        urlstart = "https://www.basketball-reference.com/teams/{}/{}.html"
        url = urlstart.format("BOS",current_date.year)
        driver.get(url)
        element = driver.find_element(By.XPATH,xpath)
    except:
        print('Error obtaining data table.')
        return None
    
    #extracting and cleaning table using bs4
    table = f'<table>{element.get_attribute("innerHTML")}</table>'
    soup = BeautifulSoup(table, 'html.parser')
    soup.find('tr', class_="over_header").decompose()
    team_stats = pd.read_html(StringIO(str(soup)))[0]
    
    getDefRtg(team_stats_table=team_stats)

def getDefRtg(team_stats_table):
    defrtg = team_stats_table['DRtg'][0]
    print(defrtg)
    return defrtg
    
handleScrapping()