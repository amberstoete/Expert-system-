
# coding: utf-8

# In[3]:


#All information about the boroughs is added to a dict. Thhe adjacent boroughs are added based on the coordinates. 
Centrum = {'name': 'Centrum', 'coordinates': '', 'budget': 2000000, 'parking zones': '', 'occupancy rate': 0.9, 'available parking sensors': 
           {'in-ground': 6, 'computer vision': 70}, 'transportation options': ['train', 'metro', 'tram', 'bus', 'ferry', 'bike']
           , 'population density': 5042, 'job density': 2500, 'smartphone': 5, 'car sharing': 5, 'travel allowance': 4,
           'bundled parking': 3, 'build': 2, 'regulations': 3, 'influence': 2, 'adjacent boroughs': ['Oost','West']}

Oost = {'name': 'Oost', 'coordinates': '', 'budget': 2000000, 'parking zones': '', 'occupancy rate': 0.7, 'available parking sensors': 
           {'in-ground': 6, 'computer vision': 70}, 'transportation options': ['train', 'metro', 'tram', 'bus', 'bike']
           , 'population density': 5042, 'job density': 2500, 'smartphone': 5, 'car sharing': 5, 'travel allowance': 4,
           'bundled parking': 3, 'build': 2, 'regulations': 3, 'influence': 2, 'adjacent boroughs': ['Zuid','Centrum']}

West = {'name': 'West', 'coordinates': '', 'budget': 2000000, 'parking zones': '', 'occupancy rate': 0.8, 'available parking sensors': 
           {'in-ground': 6, 'computer vision': 70}, 'transportation options': ['train', 'metro', 'tram', 'bus', 'bike']
           , 'population density': 5042, 'job density': 2500, 'smartphone': 5, 'car sharing': 5, 'travel allowance': 4,
           'bundled parking': 3, 'build': 2, 'regulations': 3, 'influence': 2, 'adjacent boroughs': ['Zuid','Centrum']}

Zuid = {'name': 'Zuid', 'coordinates': '', 'budget': 2000000, 'parking zones': '', 'occupancy rate': 0.9, 'available parking sensors': 
           {'in-ground': 6, 'computer vision': 70}, 'transportation options': ['train', 'metro', 'tram', 'bus', 'bike']
           , 'population density': 5042, 'job density': 2500, 'smartphone': 5, 'car sharing': 5, 'travel allowance': 4,
           'bundled parking': 3, 'build': 2, 'regulations': 3, 'influence': 2, 'adjacent boroughs': ['Oost, Centrum']}

Noord = {'name': 'Noord', 'coordinates': '', 'budget': 2000000, 'parking zones': '', 'occupancy rate': 0.4, 'available parking sensors': 
           {'in-ground': 6, 'computer vision': 70}, 'transportation options': ['train', 'metro', 'tram', 'bus', 'ferry', 'bike']
           , 'population density': 5042, 'job density': 2500, 'smartphone': 5, 'car sharing': 5, 'travel allowance': 4,
           'bundled parking': 3, 'build': 2, 'regulations': 3, 'influence': 2, 'adjacent boroughs': []}

Boroughs = [Centrum, Oost, West, Zuid, Noord]


# In[4]:


result = []


# In[5]:


options = ['train', 'metro', 'tram', 'bus', 'ferry', 'bike']


# In[6]:


for borough in Boroughs:
    if borough['occupancy rate'] > 0.2:    
        if borough['build'] == 1:
            if len(borough['transportation options'])/len(options) > 0.5:
                if borough['influence'] == 1 and borough['regulations'] == 0: 
                    result.append(borough['name'] + ': '+ 'Influence people to use public transport.')
                if borough['influence'] == 0 and borough['regulations'] == 1:
                    result.append(borough['name'] + ': '+ 'Increase parking tariffs in peak hours.')

        if borough['build'] == 2:
            if borough['influence'] == 2 and borough['regulations'] == 2:
                for x in borough['adjacent boroughs']:
                    if globals()[x]['availability'] > 0.3:
                        result.append(borough['name'] + 'Guide people to ' + x)
                    elif globals()[x]['availability'] < 0.3:
                        result.append(borough['name'] + ': '+ 'Influence people to use public transport and increase parking tariffs in peak hours.')
            elif borough['regulations'] == 2:
                presult.append(borough['name'] + ': ' + 'Increase parking tariffs in peak hours.')
            elif borough['influence'] == 2:
                result.append(borough['name'] + ': ' + 'Influence people to use public transport.')
            elif borough['regulations'] == 1 and borough['influence'] == 1:
                result.append(borough['name'] + ': '+ 'Influence people to use public transport and increase parking tariffs in peak hours.')

        if borough['build'] == 3:
            if borough['influence'] == 2 and borough['regulations'] == 2:
                result.append(borough['name'] + ': ' + 'Influence people to use public transport and increase parking tariffs in peak hours.')
            elif borough['regulations'] == 2:
                result.append(borough['name'] + ': ' + 'Increase parking tariffs in peak hours.')
            elif borough['influence'] == 2:
                result.append(borough['name'] + ': ' + 'Influence people to use public transport.')
            elif borough['regulations'] == 1 and borough['influence'] == 1:
                result.append(borough['name'] + ': ' + 'Influence people to use public transport and increase parking tariffs in peak hours.')
            else:
                result.append(borough['name'] + ': ' + 'Build ... more parking spots')
                
        if borough['travel allowance'] < 3:
            if borough['influence'] > 2:
                if len(borough['transportation options']) > 3:
                    result.append(borough['name'] + ': ' + 'Try to make a deal with companies to provide a travel allowance only to people that commute using public transport. This will cause a decrease the amount of cars in the city and therefore reduce the parking problems.')
      
        if borough['bundled parking'] < 3:
            if borough['regulations'] > 2:
                result.append(borough['name' + ': ' + ''])   
    
            
            


# In[7]:


result


# In[133]:


a = []
for x in test:
    if 'Centrum' in x:
        a.append(x)
a


# In[11]:


nbconvert rules.ipynb

