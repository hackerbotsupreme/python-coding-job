#how to iterate over rows in pandas dataframe
 
#How to iterate over rows in a DataFrame in Pandas
#Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric Python packages. Pandas is one of those packages and makes importing and analyzing data much easier. 



#Method 1: Using the index attribute of the Dataframe. 

# import pandas package as pd
import pandas as pd
  
# Define a dictionary containing students data
data = {'Name': ['Ankit', 'Amit',
                 'Aishwarya', 'Priyanka'],
        'Age': [21, 19, 20, 18],
        'Stream': ['Math', 'Commerce',
                   'Arts', 'Biology'],
        'Percentage': [88, 92, 95, 70]}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age', 
                                 'Stream', 'Percentage'])
  
print("Given Dataframe :\n", df)
  
print("\nIterating over rows using index attribute :\n")
  
# iterate through each row and select
# 'Name' and 'Stream' column respectively.
for ind in df.index:
    print(df['Name'][ind], df['Stream'][ind])
#Output:

#Given Dataframe :
#         Name  Age    Stream  Percentage
#0      Ankit   21      Math          88
#1       Amit   19  Commerce          92
#2  Aishwarya   20      Arts          95
#3   Priyanka   18   Biology          70

#Iterating over rows using index attribute :

#Ankit Math
#Amit Commerce
#Aishwarya Arts
#Priyanka Biology

  Method 2: Using loc[] function of the Dataframe. 


# import pandas package as pd
import pandas as pd
  
# Define a dictionary containing students data
data = {'Name': ['Ankit', 'Amit',
                 'Aishwarya', 'Priyanka'],
        'Age': [21, 19, 20, 18],
        'Stream': ['Math', 'Commerce',
                   'Arts', 'Biology'],
        'Percentage': [88, 92, 95, 70]}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age',
                                 'Stream', 
                                 'Percentage'])
  
print("Given Dataframe :\n", df)
  
print("\nIterating over rows using loc function :\n")
  
# iterate through each row and select
# 'Name' and 'Age' column respectively.
for i in range(len(df)):
    print(df.loc[i, "Name"], df.loc[i, "Age"])
#Output:

#Given Dataframe :
#         Name  Age    Stream  Percentage
#0      Ankit   21      Math          88
#1       Amit   19  Commerce          92
#2  Aishwarya   20      Arts          95
#3   Priyanka   18   Biology          70

#Iterating over rows using loc function :

#Ankit 21
#Amit 19
#Aishwarya 20
#Priyanka 18



#  Method 3: Using iloc[] function of the DataFrame. 
# import pandas package as pd
import pandas as pd
  
# Define a dictionary containing students data
data = {'Name': ['Ankit', 'Amit', 
                 'Aishwarya', 'Priyanka'],
        'Age': [21, 19, 20, 18],
        'Stream': ['Math', 'Commerce', 
                   'Arts', 'Biology'],
        'Percentage': [88, 92, 95, 70]}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age',
                                 'Stream', 'Percentage'])
  
print("Given Dataframe :\n", df)
  
print("\nIterating over rows using iloc function :\n")
  
# iterate through each row and select
# 0th and 2nd index column respectively.
for i in range(len(df)):
    print(df.iloc[i, 0], df.iloc[i, 2])
#Output:

#Given Dataframe :
#         Name  Age    Stream  Percentage
#0      Ankit   21      Math          88
#1       Amit   19  Commerce          92
#2  Aishwarya   20      Arts          95
#3   Priyanka   18   Biology          70

#Iterating over rows using iloc function :

#Ankit Math
#Amit Commerce
#Aishwarya Arts
#Priyanka Biology
​
# Method 4: Using iterrows() method of the Dataframe. 


# import pandas package as pd
import pandas as pd

# Define a dictionary containing students data
data = {'Name': ['Ankit', 'Amit',
				'Aishwarya', 'Priyanka'],
		'Age': [21, 19, 20, 18],
		'Stream': ['Math', 'Commerce',
				'Arts', 'Biology'],
		'Percentage': [88, 92, 95, 70]}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age',
								'Stream', 'Percentage'])

print("Given Dataframe :\n", df)

print("\nIterating over rows using iterrows() method :\n")

# iterate through each row and select
# 'Name' and 'Age' column respectively.
for index, row in df.iterrows():
	print(row["Name"], row["Age"])


#  Method 5: Using itertuples() method of the Dataframe.   Method 5: Using itertuples() method of the Dataframe. 

# import pandas package as pd
import pandas as pd

# Define a dictionary containing students data
data = {'Name': ['Ankit', 'Amit', 'Aishwarya',
				'Priyanka'],
		'Age': [21, 19, 20, 18],
		'Stream': ['Math', 'Commerce', 'Arts',
				'Biology'],
		'Percentage': [88, 92, 95, 70]}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age',
								'Stream',
								'Percentage'])

print("Given Dataframe :\n", df)

print("\nIterating over rows using itertuples() method :\n")

# iterate through each row and select
# 'Name' and 'Percentage' column respectively.
for row in df.itertuples(index=True, name='Pandas'):
	print(getattr(row, "Name"), getattr(row, "Percentage"))



#  Method 6: Using apply() method of the Dataframe. 
# import pandas package as pd
import pandas as pd

# Define a dictionary containing students data
data = {'Name': ['Ankit', 'Amit', 'Aishwarya',
				'Priyanka'],
		'Age': [21, 19, 20, 18],
		'Stream': ['Math', 'Commerce', 'Arts',
				'Biology'],
		'Percentage': [88, 92, 95, 70]}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age', 'Stream',
								'Percentage'])

print("Given Dataframe :\n", df)

print("\nIterating over rows using apply function :\n")

# iterate through each row and concatenate
# 'Name' and 'Percentage' column respectively.
print(df.apply(lambda row: row["Name"] + " " +
			str(row["Percentage"]), axis=1))



#
