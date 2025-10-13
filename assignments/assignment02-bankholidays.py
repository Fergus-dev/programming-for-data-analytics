import requests
import pandas as pd
 
url = "https://www.gov.uk/bank-holidays.json" 
response = requests.get(url)
response = response.json()

# referred to page 188 of Python for Data Analysis by Wes McKinney
northern_ireland_events = pd.DataFrame(response['northern-ireland']['events'], columns=['title', 'date'])
print(northern_ireland_events)

