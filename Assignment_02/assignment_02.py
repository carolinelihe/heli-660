# coding: utf-8

# In[160]:

from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd
import numpy as np
import bs4
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import random
import time

# In[161]:

driver = webdriver.Firefox(executable_path=r'/Users/heli/Desktop/geckodriver')

# In[162]:

driver.get('http://www.mlb.com')

# In[163]:

stats_header_bar = driver.find_element_by_class_name('megamenu-navbar-overflow__menu-item--stats')

# In[164]:

stats_header_bar.click()

# In[165]:

stats_line_items = stats_header_bar.find_elements_by_tag_name('li')

# In[166]:

stats_line_items[0].click()

# In[167]:

hitting_season_element = driver.find_element_by_id('sp_hitting_season')
season_select = Select(hitting_season_element)

# In[168]:

season_select.select_by_value('2015')

# In[169]:

Team_header_bar = driver.find_element_by_id('st_parent')

# In[170]:

Team_header_bar.click()

# In[171]:

regular_season = driver.find_element_by_id('st_hitting_game_type')
season_select = Select(regular_season)

# In[172]:

season_select.select_by_visible_text('Regular Season')

# In[173]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[174]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[175]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[176]:

df1 = pd.DataFrame(columns=head)

# In[177]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[182]:

for i in range(30):
    df1.loc[i] = list_b[i]

# ### Q1 ###

# In[183]:

df1.to_csv(r'/users/heli/Desktop/hr.csv')

# In[184]:

df1

# In[185]:

df1.sort_values(by=['HR'], ascending=False)

# ## answer 1 ##

# In[186]:

max_hr = df1.iloc[1, 1]
print(max_hr)

# In[187]:

AL_header_bar = driver.find_element_by_xpath('//*[@id="st_hitting-0"]/fieldset[2]/label[2]')

# In[188]:

AL_header_bar.click()

# In[189]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[190]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[191]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[192]:

df2 = pd.DataFrame(columns=head)

# In[193]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[194]:

for i in range(15):
    df2.loc[i] = list_b[i]

# In[195]:

df2.to_csv(r'/users/heli/Desktop/AL.csv')

# In[196]:

df2

# In[197]:

hr_average = pd.DataFrame(df2['HR'], dtype=np.float)

# In[198]:

print('the average number of AL is', hr_average['HR'].mean())

# In[199]:

NL_header_bar = driver.find_element_by_xpath('//*[@id="st_hitting-0"]/fieldset[2]/label[3]/span')

# In[200]:

NL_header_bar.click()

# In[201]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[202]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[203]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[204]:

df3 = pd.DataFrame(columns=head)

# In[205]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[206]:

for i in range(15):
    df3.loc[i] = list_b[i]

# In[207]:

df3.to_csv(r'/users/heli/Desktop/NL.csv')

# In[208]:

df3

# In[209]:

hr2_average = pd.DataFrame(df3['HR'], dtype=np.float)

# In[210]:

print('the average number of NL is', hr2_average['HR'].mean())

# ## answer 2 a ##

# In[211]:

if hr_average['HR'].mean() >= hr2_average['HR'].mean():
    print("the greatest average number of American league homeruns is:", hr_average['HR'].mean())
else:
    print("the greatest average number of American league homeruns is:", hr2_average['HR'].mean())

# In[212]:

first_inning = driver.find_element_by_id('st_hitting_hitting_splits')
first_inning_select = Select(first_inning)

# In[213]:

first_inning_select.select_by_visible_text('First Inning')

# In[214]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[215]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[216]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[217]:

df4 = pd.DataFrame(columns=head)

# In[218]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[219]:

for i in range(15):
    df4.loc[i] = list_b[i]

# In[220]:

df4.to_csv(r'/users/heli/Desktop/NL_FIRST_Inning.csv')

# In[221]:

df4

# In[222]:

hr_inn_average = pd.DataFrame(df4['HR'], dtype=np.float)

# In[223]:

print('the average number of NL in the first inning is', hr_inn_average['HR'].mean())

# In[224]:

AL_header_bar = driver.find_element_by_xpath('//*[@id="st_hitting-0"]/fieldset[2]/label[2]')

# In[225]:

AL_header_bar.click()

# In[226]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[227]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[228]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[229]:

df5 = pd.DataFrame(columns=head)

# In[230]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[231]:

for i in range(15):
    df5.loc[i] = list_b[i]

# In[232]:

df5.to_csv(r'/users/heli/Desktop/AL_FIRST_Inning.csv')

# In[233]:

df5

# In[234]:

hr_inn2_average = pd.DataFrame(df5['HR'], dtype=np.float)

# In[235]:

print('the average number of AL in the first inning is', hr_inn2_average['HR'].mean())

# ## answer 2 b ##

# In[236]:

if hr_inn_average['HR'].mean() >= hr_inn2_average['HR'].mean():
    print("the greatest average number of American league homeruns is:", hr_inn_average['HR'].mean())
else:
    print("the greatest average number of American league homeruns is:", hr_inn2_average['HR'].mean())

# ## q3 ##

# In[238]:

MLB_header_bar = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[3]/div/div[1]/div[3]/div/div[4]/div/fieldset[2]/label[1]/span')

# In[239]:

MLB_header_bar.click()

# In[240]:

hitting_season_element = driver.find_element_by_id('st_hitting_season')
season_select = Select(hitting_season_element)

# In[241]:

season_select.select_by_visible_text('2017')

# In[242]:

Player_header_bar = driver.find_element_by_id('sp_parent')

# In[243]:

Player_header_bar.click()

# In[244]:

team_season_element = driver.find_element_by_id('sp_hitting_team_id')
team_select = Select(team_season_element)

# In[245]:

team_select.select_by_visible_text('New York Yankees')

# In[246]:

AB_header_bar = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/thead/tr/th[8]/abbr')

# In[247]:

AB_header_bar.click()

# In[248]:

select = driver.find_element_by_id('sp_hitting_hitting_splits')
select_split = Select(select)

# In[249]:

select_split.select_by_visible_text('Select Split')

# In[250]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[251]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[252]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df6 = pd.DataFrame(columns=head)

# In[253]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.text)
    print(list)
    list_b.append(list)

# In[254]:

for i in range(30):
    df6.loc[i] = list_b[i]

# In[255]:

df6.to_csv(r'/users/heli/Desktop/AB_bats.csv')

# In[256]:

df6

# In[257]:

df6.to_csv(r'/users/heli/Desktop/nyy.csv')

# In[258]:

read = pd.read_csv(r'/users/heli/Desktop/nyy.csv')
read

# ## answer 3 A ##

# In[259]:

read.iloc[0, 1]
print('full-name:', 'Garrett N. Cooper')
print('position:', read.iloc[0, 6])

# ## answer 3 b ##

# In[260]:

select = driver.find_element_by_id('sp_hitting_position')
select_split = Select(select)

# In[261]:

select_split.select_by_visible_text('RF')

# In[262]:

AVG_header_bar = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/thead/tr/th[19]/abbr')

# In[263]:

AVG_header_bar.click()

# In[264]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, 'html5lib')
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df7 = pd.DataFrame(columns=head)

# In[265]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.text)
    print(list)
    list_b.append(list)

# In[266]:

for i in range(2):
    df7.loc[i] = list_b[i]

# In[267]:

df7.to_csv(r'/users/heli/Desktop/RF.csv')

# In[268]:

df7

# In[269]:

select = driver.find_element_by_xpath('//*[@id="sp_hitting_position"]')
select_split = Select(select)

# In[270]:

select_split.select_by_visible_text('CF')

# In[271]:

AVG_header_bar = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/thead/tr/th[19]/abbr')
AVG_header_bar.click()

# In[272]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, 'html5lib')
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df8 = pd.DataFrame(columns=head)

# In[273]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.text)
    print(list)
    list_b.append(list)

# In[274]:

for i in range(3):
    df8.loc[i] = list_b[i]

# In[275]:

df8.to_csv(r'/users/heli/Desktop/CF.csv')

# In[276]:

df8

# In[277]:

select = driver.find_element_by_id('sp_hitting_position')
select_split = Select(select)

# In[278]:

select_split.select_by_visible_text('LF')

# In[279]:

AVG_header_bar = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/thead/tr/th[19]/abbr')
AVG_header_bar.click()

# In[280]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, 'html5lib')
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df9 = pd.DataFrame(columns=head)

# In[281]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.text)
    print(list)
    list_b.append(list)

# In[282]:

for i in range(2):
    df9.loc[i] = list_b[i]

# In[283]:

df9.to_csv(r'/users/heli/Desktop/LF.csv')

# In[284]:

df9

# In[285]:

df9.iloc[0, 1]
print('full-name:', 'Brett M. Gardner')
print('position:', df9.iloc[0, 5])

# In[286]:

frames = [df7, df8, df9]
df10 = pd.concat(frames)
df10

# In[287]:

df10.to_csv(r'/users/heli/Desktop/concat.csv')

# In[288]:

df10

# In[289]:

df10.iloc[0, 1]
print('full-name:', 'Aaron James Judg')
print('position:', df10.iloc[0, 5])

# ## q4 ##

# In[290]:

hitting_pos_element = driver.find_element_by_xpath('//*[@id="sp_hitting_position"]')
pos_select = Select(hitting_pos_element)
pos_select.select_by_visible_text('All Positions')

# In[291]:

AL_header_bar = driver.find_element_by_xpath('//*[@id="sp_hitting-1"]/fieldset[1]/label[2]/span')

# In[292]:

AL_header_bar.click()

# In[293]:

hitting_season_element = driver.find_element_by_xpath('//*[@id="sp_hitting_season"]')
season_select = Select(hitting_season_element)

# In[294]:

season_select.select_by_visible_text('2015')

# In[295]:

hitting_team_element = driver.find_element_by_id('sp_hitting_team_id')
team_select = Select(hitting_team_element)

# In[296]:

team_select.select_by_visible_text('All Teams')

# In[297]:

AB_header_bar = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/thead/tr/th[8]/abbr')
AB_header_bar.click()

# In[298]:

qualifiers_header_bar = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[1]/fieldset[5]/label[2]/span')
qualifiers_header_bar.click()

# In[299]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, 'html5lib')
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df11 = pd.DataFrame(columns=head)

# In[300]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.text)
    print(list)
    list_b.append(list)

# In[301]:

for i in range(50):
    df11.loc[i] = list_b[i]

# In[302]:

df11.to_csv(r'/users/heli/Desktop/q4.csv')

# In[303]:

df11

# ## answer 4 ##

# In[304]:

name_bar = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/tbody/tr[1]/td[2]/a')

# In[305]:

name_bar.click()

# In[306]:

name_player = driver.find_element_by_class_name('full-name')

# In[307]:

print(name_player.text)
df11.iloc[0, 1]
print('position:', df11.iloc[0, 5])

# In[308]:

mouse = "var q=document.documentElement.scrollTop=0"
driver.execute_script(mouse)

# In[309]:

driver.back()

# ## q5 ##

# In[326]:

MLB_header_bar = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/fieldset[1]/label[1]/span')

# In[327]:

MLB_header_bar.click()

# In[328]:

hitting_season_element = driver.find_element_by_class_name('season_select')
season_select = Select(hitting_season_element)

# In[329]:

season_select.select_by_visible_text('2014')

# In[330]:

# MLB_header_bar = driver.find_element_by_class_name('ui-button-text')


# In[331]:

# MLB_header_bar.click()


# In[332]:

re_season_element = driver.find_element_by_id('sp_hitting_game_type')
re_select = Select(re_season_element)

# In[333]:

re_select.select_by_visible_text('All-Star Game')

# In[334]:

latin_coun = '''Argentina;Bolivia;Brazil;Chile;Colombia;Costa Rica;Cuba;Dominican Republic;Ecuador;El Salvador;French Guiana;Guadeloupe;Guatemala;Haiti;Honduras;Martinique;Mexico;Nicaragua;Panama;Paraguay;Peru;Puerto Rico;Saint Barthélemy;Saint Martin;Uruguay;Venezuela'''
latin_list = latin_coun.split(';')

# In[335]:

print(latin_list)

# In[336]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[337]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[338]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df12 = pd.DataFrame(columns=head)

# In[339]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.text)
    print(list)
    list_b.append(list)

# In[340]:

for i in range(41):
    df12.loc[i] = list_b[i]

# In[341]:

df12.to_csv(r'/users/heli/Desktop/q5.csv')
df12

# In[342]:

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# ## q6 ##

# In[343]:

import http.client, urllib.request, urllib.parse, urllib.error, base64

# In[344]:

import json


# In[345]:

def api(html):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': '50dd039638564f8687b0961e2df52ed7',
    }
    conn = http.client.HTTPSConnection('api.fantasydata.net')
    conn.request("GET", html, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close
    return data

# In[ ]:



