
# coding: utf-8

# In[ ]:

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


# In[ ]:

driver = webdriver.Firefox(executable_path=r'/Users/heli/Desktop/geckodriver')


# In[ ]:

driver.get('http://www.mlb.com')


# In[ ]:

stats_header_bar = driver.find_element_by_class_name('megamenu-navbar-overflow__menu-item--stats')


# In[ ]:

stats_header_bar.click()


# In[ ]:

stats_line_items = stats_header_bar.find_elements_by_tag_name('li')


# In[ ]:

stats_line_items[0].click()


# In[ ]:

hitting_season_element = driver.find_element_by_id('sp_hitting_season')
season_select = Select(hitting_season_element)


# In[ ]:

season_select.select_by_value('2015')


# In[ ]:

Team_header_bar = driver.find_element_by_id('st_parent')


# In[ ]:

Team_header_bar.click()


# In[ ]:

regular_season = driver.find_element_by_id('st_hitting_game_type')
season_select = Select(regular_season)


# In[ ]:

season_select.select_by_visible_text('Regular Season')


# In[ ]:

data=driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')


# In[ ]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')


# In[ ]:

head = [t.text.replace("▼","") for t in soup.thead.find_all("th")]


# In[ ]:

df1 = pd.DataFrame(columns = head)


# In[ ]:

list = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        list.append(a.text)


# In[ ]:

list_b = []
for i in range(int(len(list)/len(head))):
    x = list[i*len(head):(i+1)*len(head)]
    list_b.append(x)


# In[ ]:

for i in range(30):
    df1.loc[i] = list_b[i]


# ### Q1 ###

# In[ ]:

df1.to_csv(r'/users/heli/Desktop/hr.csv')


# In[ ]:

df1


# In[ ]:

df1.sort_values(by = ['HR'], ascending = False)


# ## answer 1 ##

# In[ ]:

max_hr = df1.iloc[1,1]
print(max_hr)


# In[ ]:

AL_header_bar = driver.find_element_by_xpath('//*[@id="st_hitting-0"]/fieldset[2]/label[2]')


# In[ ]:

AL_header_bar.click()


# In[ ]:

data=driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')


# In[ ]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')


# In[ ]:

head = [t.text.replace("▼","") for t in soup.thead.find_all("th")]


# In[ ]:

df2 = pd.DataFrame(columns = head)


# In[ ]:

list = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        list.append(a.text)


# In[ ]:

list_b = []
for i in range(int(len(list)/len(head))):
    x = list[i*len(head):(i+1)*len(head)]
    list_b.append(x)


# In[ ]:

for i in range(15):
    df2.loc[i] = list_b[i]


# In[ ]:

df2.to_csv(r'/users/heli/Desktop/AL.csv')


# In[ ]:

df2


# In[ ]:

hr_average = pd.DataFrame(df2['HR'],dtype = np.float)


# In[ ]:

print( 'the average number of AL is',hr_average['HR'].mean())


# In[ ]:

NL_header_bar = driver.find_element_by_xpath('//*[@id="st_hitting-0"]/fieldset[2]/label[3]/span')


# In[ ]:

NL_header_bar.click()


# In[ ]:

data=driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')


# In[ ]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')


# In[ ]:

head = [t.text.replace("▼","") for t in soup.thead.find_all("th")]


# In[ ]:

df3 = pd.DataFrame(columns = head)


# In[ ]:

list = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        list.append(a.text)


# In[ ]:

list_b = []
for i in range(int(len(list)/len(head))):
    x = list[i*len(head):(i+1)*len(head)]
    list_b.append(x)


# In[ ]:

for i in range(15):
    df3.loc[i] = list_b[i]


# In[ ]:

df3.to_csv(r'/users/heli/Desktop/NL.csv')


# In[ ]:

df3


# In[ ]:

hr2_average = pd.DataFrame(df3['HR'],dtype = np.float)


# In[ ]:

print( 'the average number of NL is',hr2_average['HR'].mean())


# ## answer 2 a ##

# In[ ]:

if hr_average['HR'].mean() >=  hr2_average['HR'].mean():
   print ("the greatest average number of American league homeruns is:", hr_average['HR'].mean())
else:
   print ("the greatest average number of American league homeruns is:", hr2_average['HR'].mean())


# In[ ]:

first_inning = driver.find_element_by_id('st_hitting_hitting_splits')
first_inning_select = Select(first_inning)


# In[ ]:

first_inning_select.select_by_visible_text('First Inning')


# In[ ]:

data=driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')


# In[ ]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')


# In[ ]:

head = [t.text.replace("▼","") for t in soup.thead.find_all("th")]


# In[ ]:

df4 = pd.DataFrame(columns = head)


# In[ ]:

list = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        list.append(a.text)


# In[ ]:

list_b = []
for i in range(int(len(list)/len(head))):
    x = list[i*len(head):(i+1)*len(head)]
    list_b.append(x)


# In[ ]:

for i in range(15):
    df4.loc[i] = list_b[i]


# In[ ]:

df4.to_csv(r'/users/heli/Desktop/NL_FIRST_Inning.csv')


# In[ ]:

df4


# In[ ]:

hr_inn_average = pd.DataFrame(df4['HR'],dtype = np.float)


# In[ ]:

print( 'the average number of NL in the first inning is',hr_inn_average['HR'].mean())


# In[ ]:

AL_header_bar = driver.find_element_by_xpath('//*[@id="st_hitting-0"]/fieldset[2]/label[2]')


# In[ ]:

AL_header_bar.click()


# In[ ]:

data=driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')


# In[ ]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')


# In[ ]:

head = [t.text.replace("▼","") for t in soup.thead.find_all("th")]


# In[ ]:

df5 = pd.DataFrame(columns = head)


# In[ ]:

list = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        list.append(a.text)


# In[ ]:

list_b = []
for i in range(int(len(list)/len(head))):
    x = list[i*len(head):(i+1)*len(head)]
    list_b.append(x)


# In[ ]:

for i in range(15):
    df5.loc[i] = list_b[i]


# In[ ]:

df5.to_csv(r'/users/heli/Desktop/AL_FIRST_Inning.csv')


# In[ ]:

df5


# In[ ]:

hr_inn2_average = pd.DataFrame(df5['HR'],dtype = np.float)


# In[ ]:

print( 'the average number of AL in the first inning is',hr_inn2_average['HR'].mean())


# ## answer 2 b ##

# In[ ]:

if hr_inn_average['HR'].mean() >=  hr_inn2_average['HR'].mean():
   print ("the greatest average number of American league homeruns is:", hr_inn_average['HR'].mean())
else:
   print ("the greatest average number of American league homeruns is:", hr_inn2_average['HR'].mean())


# In[ ]:

MLB_header_bar = driver.find_element_by_xpath('//*[@id="st_hitting-0"]/fieldset[2]/label[1]/span')


# In[ ]:

MLB_header_bar.click()


# In[ ]:

hitting_season_element = driver.find_element_by_id('st_hitting_season')
season_select = Select(hitting_season_element)


# In[ ]:

season_select.select_by_visible_text('2017')


# In[ ]:

Player_header_bar = driver.find_element_by_id('sp_parent')


# In[ ]:

Player_header_bar.click()


# In[ ]:

team_season_element = driver.find_element_by_id('sp_hitting_team_id')
team_select = Select(team_season_element)


# In[ ]:

team_select.select_by_visible_text('New York Yankees')


# In[ ]:

AB_header_bar = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/thead/tr/th[8]/abbr')


# In[ ]:

AB_header_bar.click()


# In[ ]:

select = driver.find_element_by_id('sp_hitting_hitting_splits')
select_split = Select(select)


# In[ ]:

select_split.select_by_visible_text('Select Split')


# In[ ]:

data=driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')


# In[ ]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')


# In[ ]:

head = [t.text.replace("▼","") for t in soup.thead.find_all("th")]
df6=pd.DataFrame(columns=head)


# In[ ]:

list = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        player = a.text.strip()
        list.append(player)


# In[ ]:

list_b = []
for i in range(int(len(list)/len(head))):
    x = list[i*len(head):(i+1)*len(head)]
    list_b.append(x)


# In[ ]:

for i in range(44):
    df6.loc[i] = list_b[i]


# In[ ]:

df6.to_csv(r'/users/heli/Desktop/AB_bats.csv')


# In[ ]:

df6


# In[ ]:

df6.to_csv(r'/users/heli/Desktop/nyy.csv')


# In[ ]:

read = pd.read_csv(r'/users/heli/Desktop/nyy.csv')
read


# ## answer 3 b ##

# In[ ]:

max = 0.0
for i in range(44):
        
        if read.loc[i]['Pos'] == 'RF' or read.loc[i]['Pos'] == 'CF' or read.loc[i]['Pos'] == 'LF':
            if read.loc[i]['AVG'][1:].isdigit():
                if float (read.loc[i]['AVG']) >= max:
                    max = float (read.loc[i]['AVG'])
                    name = read.loc[i]['Player']
                    Position = read.loc[i]['Pos']
print(name,max,Position)            


# In[ ]:

new = df6.sort_values(by = ['AVG'], ascending = False)
new


# ## answer 3 a ##

# In[ ]:

new.iloc[0,1]
print('full-name:', 'Garrett N. Cooper')
print('position:', new.iloc[0,5])


# ## q4 ##

# In[ ]:

AL_header_bar = driver.find_element_by_xpath('//*[@id="sp_hitting-1"]/fieldset[1]/label[2]/span')


# In[ ]:

AL_header_bar.click()


# In[ ]:

hitting_season_element = driver.find_element_by_xpath('//*[@id="sp_hitting_season"]')
season_select = Select(hitting_season_element)


# In[ ]:

season_select.select_by_visible_text('2015')


# In[ ]:

hitting_team_element = driver.find_element_by_id('sp_hitting_team_id')
team_select = Select(hitting_team_element)


# In[ ]:

team_select.select_by_visible_text('All Teams')


# In[ ]:

import time
data=driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')
soup = bs4.BeautifulSoup(data_html, 'html5lib')
head = [t.text.replace("▼","") for t in soup.thead.find_all("th")]
df7=pd.DataFrame(columns=head)
for x in range(12):

    if x != 0:
        next_page = driver.find_element_by_class_name('paginationWidget-next')
        next_page.click()
        time.sleep(5)
    data=driver.find_element_by_id('datagrid')
    data_html = data.get_attribute('innerHTML')
    soup = bs4.BeautifulSoup(data_html, 'html5lib')
 
    list = []
    for t in soup.tbody.find_all("tr"):
        for a in t.find_all("td"):
            player = a.text.strip()
            list.append(player)
    list_b = []
    for m in range(int(len(list)/len(head))):
        n = list[m*len(head):(m+1)*len(head)]
        list_b.append(n) 
    print(list)
    if x == 11:
        for i in range(49):
            df7.loc[x*50+i] = list_b[i]
    else: 
        for i in range(50):
            df7.loc[x*50+i] = list_b[i]


# In[ ]:

df7.to_csv(r'/users/heli/Desktop/q4.csv')
df7


# ## answer 4 ##

# In[ ]:

name_bar = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/div[8]/table/tbody/tr[1]/td[2]/a')


# In[ ]:

name_bar.click()


# In[ ]:

name_player = driver.find_element_by_class_name('full-name')


# In[ ]:

print(name_player.text)
df7.iloc[0,1]
print('position:', df7.iloc[0,5])


# In[ ]:

mouse="var q=document.documentElement.scrollTop=0"  
driver.execute_script(mouse)


# In[ ]:

driver.back()


# ## q5 ##

# In[ ]:

MLB_header_bar = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/fieldset[1]/label[1]/span')


# In[ ]:

MLB_header_bar.click()


# In[ ]:

hitting_season_element = driver.find_element_by_class_name('season_select')
season_select = Select(hitting_season_element)


# In[ ]:

season_select.select_by_visible_text('2014')


# In[ ]:

#MLB_header_bar = driver.find_element_by_class_name('ui-button-text')


# In[ ]:

#MLB_header_bar.click()


# In[ ]:

re_season_element = driver.find_element_by_id('sp_hitting_game_type')
re_select = Select(re_season_element)


# In[ ]:

re_select.select_by_visible_text('All-Star Game')


# In[ ]:

latin_coun ='''Argentina;Bolivia;Brazil;Chile;Colombia;Costa Rica;Cuba;Dominican Republic;Ecuador;El Salvador;French Guiana;Guadeloupe;Guatemala;Haiti;Honduras;Martinique;Mexico;Nicaragua;Panama;Paraguay;Peru;Puerto Rico;Saint Barthélemy;Saint Martin;Uruguay;Venezuela'''
latin_list = latin_coun.split(';')


# In[ ]:

print(latin_list)


# In[ ]:

data=driver.find_element_by_id('datagrid')
data_html = data.get_attribute('innerHTML')


# In[ ]:

soup = bs4.BeautifulSoup(data_html, 'html5lib')


# In[ ]:

head = [t.text.replace("▼","") for t in soup.thead.find_all("th")]
df8=pd.DataFrame(columns=head)


# In[ ]:

list = []
for t in soup.tbody.find_all("tr"):
    for a in t.find_all("td"):
        player = a.text.strip()
        list.append(player)


# In[ ]:

list_b = []
for i in range(int(len(list)/len(head))):
    x = list[i*len(head):(i+1)*len(head)]
    list_b.append(x)
    


# In[ ]:

for i in range(41):
    df8.loc[i] = list_b[i]


# In[ ]:

df8.to_csv(r'/users/heli/Desktop/AB_bats.csv')
df8


# In[ ]:

w_list = df8['Player']
player_list =[]
for i in range(41):
    player_list.append(w_list[i]) 
    
name_list=set(player_list)
name_list


# In[ ]:

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# In[ ]:

wait = WebDriverWait(driver, 10)
q5 = []
for name in name_list:     
        player_bar = driver.find_elements_by_link_text(name)
        for e in range(len(player_bar)):
            
            print(name)
            time.sleep(3)
            player_bar_temp = driver.find_elements_by_link_text(name)
            player_bar_temp[k].click()
            player_bio = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'player-bio')))

        
            
            for country in latin_list:
                if country in player_bio.text:
                                        
                                        player_name = driver.find_element_by_class_name('full-name').text
                                        datahtml= wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'dropdown.team'))).text
                                        team_name = datahtml.split('\n')[0].strip()
                                        print('player_name:',player_name)
                                        q5.append(player_name)
                                        print('team_name:', team_name)
                                        q5.append(team_name)


            
            time.sleep(5)
            driver.back()


# In[ ]:

q5


# In[ ]:

head_q5 = ['Player', 'Team']
pd_q5 = pd.DataFrame(columns= head_q5)


# In[ ]:

q5_format = []
for i in range(int(len(q5)/len(head_q5))):
    q5_format.append(q5[i*len(head_q5) : (i+1) * len(head_q5)])
    
for q in range(16):
    pd_q5.loc[q] = q5_format[q]
    
pd_q5


# In[ ]:

pd_q5.to_csv(r'/users/heli/Desktop/q5.csv')
pd_q5


# ## answer q5 ##

# In[ ]:

print(pd_q5)


# ## q6 ##

# In[206]:

import http.client, urllib.request, urllib.parse, urllib.error, base64


# In[207]:

import json


# In[212]:

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


# In[213]:

stats_stadium = api("/v3/mlb/stats/json/Stadiums")
time.sleep(4)
stats_stadium = json.loads(stats_stadium)
stats_stadium


# In[214]:

match_list = []
for i in stats_stadium:
    match_list.append([i["StadiumID"], i["Name"], i["City"], i["State"]])
    
match_list
    


# In[215]:

stats_game = json.loads(api("/v3/mlb/stats/json/Games/2016"))
stats_game


# In[216]:

game_list = []
for i in stats_game:
    game_list.append([i["HomeTeam"], i["AwayTeam"], i["DateTime"][0:10], i["StadiumID"]])
    
game_list


# In[217]:

general_list = []

for i in match_list:
    for j in game_list:
        if i[0] == j[3]:
            temp = j[:-1]+i[1:]
            general_list.append(temp)
            
general_list


# In[218]:

data_q6 = []
for a in general_list:
    
    if 'HOU' in a:
        
        data_q6.append(a)
    
        
data_q6


# In[219]:

df_q6 = pd.DataFrame(columns= ['Home Team', 'Away Team', 'Date', 'Stadium Name', 'City', 'State'])

for i in range(len(data_q6)):
    df_q6.loc[i] = data_q6[i]
    
df_q6


# In[220]:

df_q6.to_csv('D:\BIA-660D\Q_6.csv')


# In[ ]:



