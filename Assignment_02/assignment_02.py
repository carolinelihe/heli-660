# coding: utf-8

# In[1]:

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

# In[2]:

driver = webdriver.Firefox(executable_path=r'/Users/heli/Desktop/geckodriver')

# In[3]:

driver.get('http://www.mlb.com')

# In[4]:

stats_header_bar = driver.find_element_by_class_name('megamenu-navbar-overflow__menu-item--stats')

# In[5]:

stats_header_bar.click()

# In[6]:

stats_line_items = stats_header_bar.find_elements_by_tag_name('li')

# In[7]:

stats_line_items[0].click()

# In[8]:

hitting_season_element = driver.find_element_by_id('sp_hitting_season')
season_select = Select(hitting_season_element)

# In[9]:

season_select.select_by_value('2015')

# In[10]:

Team_header_bar = driver.find_element_by_id('st_parent')

# In[11]:

Team_header_bar.click()

# In[12]:

regular_season = driver.find_element_by_id('st_hitting_game_type')
season_select = Select(regular_season)

# In[13]:

season_select.select_by_visible_text('Regular Season')

# In[14]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[15]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[16]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[17]:

df1 = pd.DataFrame(columns=head)

# In[18]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[19]:

for i in range(30):
    df1.loc[i] = list_b[i]

# ### Q1 ###

# In[20]:

df1.to_csv(r'/users/heli/Desktop/hr.csv')

# In[21]:

df1

# In[22]:

df1.sort_values(by=['HR'], ascending=False)

# ## answer 1 ##

# In[23]:

max_hr = df1.iloc[1, 1]
print(max_hr)

# In[24]:

AL_header_bar = driver.find_element_by_xpath('//*[@id="st_hitting-0"]/fieldset[2]/label[2]')

# In[25]:

AL_header_bar.click()

# In[26]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[27]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[28]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[29]:

df2 = pd.DataFrame(columns=head)

# In[30]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[31]:

for i in range(15):
    df2.loc[i] = list_b[i]

# In[32]:

df2.to_csv(r'/users/heli/Desktop/AL.csv')

# In[33]:

df2

# In[39]:

hr_average = pd.DataFrame(df2['HR'], dtype=np.float)

# In[40]:

print('the average number of AL is', hr_average['HR'].mean())

# In[41]:

NL_header_bar = driver.find_element_by_xpath('//*[@id="st_hitting-0"]/fieldset[2]/label[3]/span')

# In[42]:

NL_header_bar.click()

# In[43]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[44]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[45]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[46]:

df3 = pd.DataFrame(columns=head)

# In[47]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[48]:

for i in range(15):
    df3.loc[i] = list_b[i]

# In[49]:

df3.to_csv(r'/users/heli/Desktop/NL.csv')

# In[50]:

df3

# In[51]:

hr2_average = pd.DataFrame(df3['HR'], dtype=np.float)

# In[52]:

print('the average number of NL is', hr2_average['HR'].mean())

# ## answer 2 a ##

# In[53]:

if hr_average['HR'].mean() >= hr2_average['HR'].mean():
    print("the greatest average number of American league homeruns is:", hr_average['HR'].mean())
else:
    print("the greatest average number of American league homeruns is:", hr2_average['HR'].mean())

# In[54]:

first_inning = driver.find_element_by_id('st_hitting_hitting_splits')
first_inning_select = Select(first_inning)

# In[55]:

first_inning_select.select_by_visible_text('First Inning')

# In[56]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[57]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[58]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[59]:

df4 = pd.DataFrame(columns=head)

# In[60]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[61]:

for i in range(15):
    df4.loc[i] = list_b[i]

# In[62]:

df4.to_csv(r'/users/heli/Desktop/NL_FIRST_Inning.csv')

# In[63]:

df4

# In[64]:

hr_inn_average = pd.DataFrame(df4['HR'], dtype=np.float)

# In[65]:

print('the average number of NL in the first inning is', hr_inn_average['HR'].mean())

# In[66]:

AL_header_bar = driver.find_element_by_xpath('//*[@id="st_hitting-0"]/fieldset[2]/label[2]')

# In[67]:

AL_header_bar.click()

# In[68]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[69]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[70]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]

# In[71]:

df5 = pd.DataFrame(columns=head)

# In[72]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[73]:

for i in range(15):
    df5.loc[i] = list_b[i]

# In[74]:

df5.to_csv(r'/users/heli/Desktop/AL_FIRST_Inning.csv')

# In[75]:

df5

# In[76]:

hr_inn2_average = pd.DataFrame(df5['HR'], dtype=np.float)

# In[77]:

print('the average number of AL in the first inning is', hr_inn2_average['HR'].mean())

# ## answer 2 b ##

# In[78]:

if hr_inn_average['HR'].mean() >= hr_inn2_average['HR'].mean():
    print("the greatest average number of American league homeruns is:", hr_inn_average['HR'].mean())
else:
    print("the greatest average number of American league homeruns is:", hr_inn2_average['HR'].mean())

# ## q3 ##

# In[79]:

MLB_header_bar = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/fieldset[1]/label[1]/span')

# In[80]:

MLB_header_bar.click()

# In[81]:

hitting_season_element = driver.find_element_by_id('st_hitting_season')
season_select = Select(hitting_season_element)

# In[82]:

season_select.select_by_visible_text('2017')

# In[164]:

Player_header_bar = driver.find_element_by_id('sp_parent')

# In[165]:

Player_header_bar.click()

# In[166]:

team_season_element = driver.find_element_by_id('sp_hitting_team_id')
team_select = Select(team_season_element)

# In[167]:

team_select.select_by_visible_text('New York Yankees')

# In[168]:

AB_header_bar = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/thead/tr/th[8]/abbr')

# In[169]:

AB_header_bar.click()

# In[180]:

select = driver.find_element_by_id('sp_hitting_hitting_splits')
select_split = Select(select)

# In[181]:

select_split.select_by_visible_text('Select Split')

# In[182]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[183]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[184]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df6 = pd.DataFrame(columns=head)

# In[186]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[187]:

for i in range(30):
    df6.loc[i] = list_b[i]

# In[188]:

df6.to_csv(r'/users/heli/Desktop/AB_bats.csv')

# In[189]:

df6

# In[190]:

df6.to_csv(r'/users/heli/Desktop/nyy.csv')

# In[191]:

read = pd.read_csv(r'/users/heli/Desktop/nyy.csv')
read

# ## answer 3 A ##

# In[195]:

read.iloc[0, 1]
print('full-name:', 'Garrett N. Cooper')
print('position:', read.iloc[0, 6])

# ## answer 3 b ##

# In[297]:

select = driver.find_element_by_id('sp_hitting_position')
select_split = Select(select)

# In[298]:

select_split.select_by_visible_text('RF')

# In[299]:

AVG_header_bar = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/thead/tr/th[19]/abbr')

# In[300]:

AVG_header_bar.click()

# In[301]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, 'html5lib')
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df7 = pd.DataFrame(columns=head)

# In[303]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[304]:

for i in range(2):
    df7.loc[i] = list_b[i]

# In[305]:

df7.to_csv(r'/users/heli/Desktop/RF.csv')

# In[306]:

df7

# In[310]:

select = driver.find_element_by_xpath('//*[@id="sp_hitting_position"]')
select_split = Select(select)

# In[311]:

select_split.select_by_visible_text('CF')

# In[312]:

AVG_header_bar = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/thead/tr/th[19]/abbr')
AVG_header_bar.click()

# In[313]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, 'html5lib')
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df8 = pd.DataFrame(columns=head)

# In[315]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[316]:

for i in range(3):
    df8.loc[i] = list_b[i]

# In[317]:

df8.to_csv(r'/users/heli/Desktop/CF.csv')

# In[318]:

df8

# In[321]:

select = driver.find_element_by_id('sp_hitting_position')
select_split = Select(select)

# In[322]:

select_split.select_by_visible_text('LF')

# In[323]:

AVG_header_bar = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/thead/tr/th[19]/abbr')
AVG_header_bar.click()

# In[324]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, 'html5lib')
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df9 = pd.DataFrame(columns=head)

# In[326]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[327]:

for i in range(2):
    df9.loc[i] = list_b[i]

# In[328]:

df9.to_csv(r'/users/heli/Desktop/LF.csv')

# In[329]:

df9

# In[330]:

df9.iloc[0, 1]
print('full-name:', 'Brett M. Gardner')
print('position:', df9.iloc[0, 5])

# In[336]:

frames = [df7, df8, df9]
df10 = pd.concat(frames)
df10

# In[337]:

df10.to_csv(r'/users/heli/Desktop/concat.csv')

# In[338]:

df10

# In[339]:

df10.iloc[0, 1]
print('full-name:', 'Aaron James Judg')
print('position:', df10.iloc[0, 5])

# ## q4 ##

# In[383]:

hitting_pos_element = driver.find_element_by_xpath('//*[@id="sp_hitting_position"]')
pos_select = Select(hitting_pos_element)
pos_select.select_by_visible_text('All Positions')

# In[384]:

AL_header_bar = driver.find_element_by_xpath('//*[@id="sp_hitting-1"]/fieldset[1]/label[2]/span')

# In[385]:

AL_header_bar.click()

# In[386]:

hitting_season_element = driver.find_element_by_xpath('//*[@id="sp_hitting_season"]')
season_select = Select(hitting_season_element)

# In[387]:

season_select.select_by_visible_text('2015')

# In[388]:

hitting_team_element = driver.find_element_by_id('sp_hitting_team_id')
team_select = Select(hitting_team_element)

# In[389]:

team_select.select_by_visible_text('All Teams')

# In[390]:

AB_header_bar = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/thead/tr/th[8]/abbr')
AB_header_bar.click()

# In[391]:

qualifiers_header_bar = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[1]/fieldset[5]/label[2]/span')
qualifiers_header_bar.click()

# In[392]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, 'html5lib')
head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df11 = pd.DataFrame(columns=head)

# In[397]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[398]:

for i in range(50):
    df11.loc[i] = list_b[i]

# In[399]:

df11.to_csv(r'/users/heli/Desktop/q4.csv')

# In[400]:

df11

# ## answer 4 ##

# In[401]:

name_bar = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/tbody/tr[1]/td[2]/a')

# In[402]:

name_bar.click()

# In[403]:

name_player = driver.find_element_by_class_name('full-name')

# In[404]:

print(name_player.text)
df11.iloc[0, 1]
print('position:', df11.iloc[0, 5])

# In[405]:

mouse = "var q=document.documentElement.scrollTop=0"
driver.execute_script(mouse)

# In[406]:

driver.back()

# ## q5 ##

# In[407]:

MLB_header_bar = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/fieldset[1]/label[1]/span')

# In[408]:

MLB_header_bar.click()

# In[409]:

hitting_season_element = driver.find_element_by_class_name('season_select')
season_select = Select(hitting_season_element)

# In[410]:

season_select.select_by_visible_text('2014')

# In[411]:

# MLB_header_bar = driver.find_element_by_class_name('ui-button-text')


# In[412]:

# MLB_header_bar.click()


# In[413]:

re_season_element = driver.find_element_by_id('sp_hitting_game_type')
re_select = Select(re_season_element)

# In[414]:

re_select.select_by_visible_text('All-Star Game')

# In[415]:

latin_coun = '''Argentina;Bolivia;Brazil;Chile;Colombia;Costa Rica;Cuba;Dominican Republic;Ecuador;El Salvador;French Guiana;Guadeloupe;Guatemala;Haiti;Honduras;Martinique;Mexico;Nicaragua;Panama;Paraguay;Peru;Puerto Rico;Saint Barthélemy;Saint Martin;Uruguay;Venezuela'''
latin_list = latin_coun.split(';')

# In[416]:

print(latin_list)

# In[417]:

data = driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')

# In[418]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')

# In[419]:

head = [t.text.replace("▼", "") for t in soup.thead.find_all("th")]
df12 = pd.DataFrame(columns=head)

# In[421]:

list_b = []
trs = soup.tbody.find_all("tr")
for tr in trs:
    list = []
    for td in tr:
        list.append(td.string)
    print(list)
    list_b.append(list)

# In[422]:

for i in range(41):
    df12.loc[i] = list_b[i]

# In[423]:

df12.to_csv(r'/users/heli/Desktop/q5.csv')
df12

# In[424]:

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# ## q6 ##

# In[4]:

import http.client, urllib.request, urllib.parse, urllib.error, base64

# In[5]:

import json


# In[6]:

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

