#pandas basic of time series of time-series manipulation

#Although time series is also available in scikit-learn but Pandas has some sort of compiled more features. In this module of Pandas, we can include the date and time for every record and can fetch the records of dataframe. We can find out the data within a certain range of date and time by using pandas module named Time series. Let’s discuss some major objectives to introduce the pandas time series analysis.
O#bjectives of time series analysis
 

#Create the series of date
#Work with data timestamp
#Convert string data to timestamp
#Slicing of data using timestamp
#Resample your time series for different time period aggregates/summary statistics
#Working with missing data
#Now, let’s do some practical analysis on some data to demonstrate the use of pandas time series.
#Code #1:


import pandas as pd
from datetime import datetime
import numpy as np

range_date = pd.date_range(start ='1/1/2019', end ='1/08/2019',
												freq ='Min')
print(range_date)

#Explanation: 
#Here in this code, we have created the timestamp on the bases of minutes for date ranges from 1/1/2019 – 8/1/2019. We can vary the frequency by hours to minutes or seconds. This function will help you to track the record of data stored per minute. As we can see in the output the length of the datetime stamp is 10081. Remember pandas use data type as datetime64[ns].
#Code #2:



import pandas as pd
from datetime import datetime
import numpy as np

range_date = pd.date_range(start ='1/1/2019', end ='1/08/2019',
												freq ='Min')
print(type(range_date[110]))




#Output: 
#<class 'pandas._libs.tslibs.timestamps.Timestamp'>
 

#Explanation: 
#We are checking the type of our object named range_date. 
#Code #3:
 


import pandas as pd
from datetime import datetime
import numpy as np
 
range_date = pd.date_range(start ='1/1/2019', end ='1/08/2019',
                                                   freq ='Min')
 
df = pd.DataFrame(range_date, columns =['date'])
df['data'] = np.random.randint(0, 100, size =(len(range_date)))
 
print(df.head(10))



#Output: 
#                  date  data
#0 2019-01-01 00:00:00    49
#1 2019-01-01 00:01:00    58
#2 2019-01-01 00:02:00    48
#3 2019-01-01 00:03:00    96
#4 2019-01-01 00:04:00    42
#5 2019-01-01 00:05:00     8
#6 2019-01-01 00:06:00    20
#7 2019-01-01 00:07:00    96
#8 2019-01-01 00:08:00    48
#9 2019-01-01 00:09:00    78
 

#Explanation:
#We have first created a time series then converted this data into dataframe and use random function to generate the random data and map over the dataframe. Then to check the result we use print function. 
#In order to do time series manipulation, we need to have a datetime index so that dataframe is indexed on the timestamp. Here, we are adding one more new column in pandas dataframe.
#Code #4:
import pandas as pd
from datetime import datetime
import numpy as np

range_date = pd.date_range(start ='1/1/2019', end ='1/08/2019',
												freq ='Min')

df = pd.DataFrame(range_date, columns =['date'])
df['data'] = np.random.randint(0, 100, size =(len(range_date)))

string_data = [str(x) for x in range_date]
print(string_data[1:11])


#Output: 
#[‘2019-01-01 00:01:00’, ‘2019-01-01 00:02:00’, ‘2019-01-01 00:03:00’, ‘2019-01-01 00:04:00’, ‘2019-01-01 00:05:00’, ‘2019-01-01 00:06:00’, ‘2019-01-01 00:07:00’, ‘2019-01-01 00:08:00’, ‘2019-01-01 00:09:00’, ‘2019-01-01 00:10:00’] 
 
#Explanation: 
#This code just use the elements of data_rng and converted to string and due to lot of data we slice the data and print first ten values list string_data. By using the for each loop in list, we got all the values that are in the series range_date. When we are using date_range we always have to specify the start and end date.
#Example:


import pandas as pd
from datetime import datetime
import numpy as np

range_data = pd.date_range(start ='1/1/2019', end ='1/08/2019',
												freq ='Min')

df = pd.DataFrame(range_data, columns =['date'])
df['data'] = np.random.randint(0, 100, size =(len(range_data)))

df['datetime'] = pd.to_datetime(df['date'])
df = df.set_index('datetime')
df.drop(['date'], axis = 1, inplace = True)

print(df['2019-01-05'][1:11])

#Output: 
#                     data
#datetime                 
#2019-01-05 00:01:00    99
#2019-01-05 00:02:00    21
#2019-01-05 00:03:00    29
#2019-01-05 00:04:00    98
#2019-01-05 00:05:00     0
#2019-01-05 00:06:00    72
#2019-01-05 00:07:00    69
#2019-01-05 00:08:00    53
#2019-01-05 00:09:00     3
#2019-01-05 00:10:00    37

 
 









