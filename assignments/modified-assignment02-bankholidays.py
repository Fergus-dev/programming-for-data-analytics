import requests
import pandas as pd

# below I use the requests library to get the json data from the gov.uk website
 
url = "https://www.gov.uk/bank-holidays.json" 
response = requests.get(url)
response = response.json()

# I create seperate dataframes of events in each jurisdiction by subsetting the response dictionary
# I referred to page 188 of Wes McKinney's Python for Data Analysis while doing this

northern_ireland_events = pd.DataFrame(response['northern-ireland']['events'], columns=['title', 'date'])
print(northern_ireland_events)

england_and_wales_events = pd.DataFrame(response['england-and-wales']['events'], columns=['title', 'date'])
#print(england_and_wales_events)

scotland_events = pd.DataFrame(response['scotland']['events'], columns=['title', 'date'])
#print(scotland_events)

#  I then cross reference data frames to find bank holidays unique to Northern Ireland
# Copilot conversation for reference: https://copilot.microsoft.com/shares/wMh5d19vqpjtsBuyaonvQ
# So the following code in English says, create a new data frame from whatever data that is in the events column of the northern ireland
# data frame and is not in the events column of the england and wales data frame and not in the events column of the scotland data frame
# the ~ flips the boolean values. So although the .isin is being used, the ~ essentially makes it a "is not in" operation

ni_only_holidays = northern_ireland_events[~northern_ireland_events['title'].isin(england_and_wales_events['title'])\
                                           & ~northern_ireland_events['title'].isin(scotland_events['title'])]

# upon printing out the data frame, the same two holidays were repeated, so I'm removing duplicates
# page 210 of Wes McKinney's Python for Data Analysis
print(ni_only_holidays.drop_duplicates(subset="title"))


