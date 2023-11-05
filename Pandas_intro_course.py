#### 1. INTRODUCTION

## 1.1. INSTALLING PANDAS

# In order to work with pandas, we need to ensure that pandas library has been installed in our python environment
# If you get this error message: ModuleNotFoundError: No module named 'pandas', it means you need to install pandas in python:
# In the terminal open python (by simply writing python and hitting enter) and then write the following command:

# pip install pandas

# This step needs to be done only one time - once you have isntalled pandas to your python environment, all you have to do if you want to 
#work with it is import it into your script (if you are writing one) or in the terminal (if you are coding on the go, directly from the terminal).

#####


## 1.2. IMPORTING PANDAS

# The best practice is to import all the libraries your code needs at the beginning of the script.
# Most of the libraries have some abbreviation which makes it easier and faster to use it in the code. For example, we can import pandas in two ways:
import pandas   #or:
import pandas as pd
# In the first case, each time we want to use some of the built in functions of pandas, we need to write padnas.DataFrame, pandas.merge(), pandas.melt() etc.
# If we import pandas as pd, we can instead write pd.DataFrame, pd.merge(), pd.melt() etc.
# Both ways are correct and you can choose your preference.

#####

## 1.3. PANDAS SERIES

# In order to work with the data, we first need to store it in one of the data objects that pandas library works with. If we only have a table with one column
# (so basically just a list of data), we call this a pandas Series. 
# The official definition of pandas Series can be found in the pandas documentation and it looks like this:
# pandas.Series(data=None, index=None, dtype=None, name=None, copy=None, fastpath=False)
    # from everything listed in the parenthesis, you will most likely only need to change or define the following:
    # data => contains data stored in Series
    # index => array-like list of index labels - if we don't define it, the indices will be generated automatically for our data as 0,1,2,3,..
    # dtype => with this you can define what type of data your pandas series will contain - if we don't specify this, data type will be inferred from data (usually the best option :) )
    # name => the name we wish to give to our Series (optional)
# Below is an example of how to store some data in pandas Series:

doses_batch1 = [1, 5, 6, 8, 10]    # to define series from a list of numbers 

series1 = pd.Series(data = doses_batch1)
print(series1)
series2 = pd.Series(data = doses_batch1, index = ['a', 'b', 'c', 'd', 'e'])
print(series2)

doses = {'sample1' : 1, 'sample2': 5, 'sample3': 6, 'sample4': 8, 'sample5': 10} # to define series from a dictionary
series3 = pd.Series(data = doses)
print(series3)
series4 = pd.Series(data = doses, index = ['a', 'b', 'c', 'd', 'e'])
print(series4)  # The keys of the dictionary match with the Index values, hence the Index values have no effect - by changing the indices, we end up rewriting our Series and get NaN values



#####

## 1.4. PANDAS DATAFRAME

# In case our data has more than one column, we need to store it in pandas DataFrame. As its name already indicates, pandas DataFrame is a table in which each column has a name and each row
# has an index (indices can also be thought of as names of the rows).
# The official definition of pandas DataFrame can be found in the pandas documentation and it looks like this:
# pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
# the only new varible that we need to define here is "columns" => names of the columns are crucial for working with pd.DataFrame - pandas library was somehow made to manipulate the 
# data from the tabular representation, sort of like a high level excel - when we work with excel, sometimes we want to sum all the values in a certain column, sort the values in a column,
# delete or insert a column, change the name of the column, count the number of values in each column, etc. Pandas enables us to do all that and much more much faster, but knowing the names 
# of the columns when working with pandas is very important and it makes your life easier :). Sometimes you have no idea what are the column names of your table, but don't worry, we will 
# learn how to quickly get to know the data you are working with in just a bit. 
# First we will show how to define a DataFrame by yourself and then in the next section (READING DATA FROM A FILE) we will talk more about defining the columns. 

# defining a DataFrame from a dictionary:
medicine = {'ibuprofen': [1, 5, 6, 8, 10], 'naproxen': [0.5, 0, 0.5, 1, 1.5]}   # dict keys are column names, lists indicate values in each column

df1 = pd.DataFrame(data = medicine)
print(df1)
df2 = pd.DataFrame(data = medicine, index = ['sample1', 'sample2', 'sample3', 'sample4', 'sample5'])
print(df2)

# defining a DataFrame from pandas Series:
df3 = pd.DataFrame(series3)
# Notice how we automatically got a header row with the column labels and, since we didn't specifically define what we want our column labels to be, they are automatically assigned names
# that correspond to their indices (first column is names '0', second column '1', etc.)

# If I'm only interested in the first 3 samples:
df4 = pd.DataFrame(series3, index = ['sample1', 'sample2', 'sample3'])

#####

## 1.5. READING DATA FROM A FILE

# Usually, our data is already stored in some form of a .txt, .csv (= comma separated values), .tsv (= tab separated values) or .xlsx file. In those cases, we can simply input 
# the data in our script by uploading the file to pandas DataFrame. We do this by using a function .read_csv().
# The official definition of a .read_csv() funciton can be found in the pandas documentation and since it includes many variables that can be defined when calling the function, 
# we will not show it here in it's entirety, but rather comment only on the most commonly used variables:
# pd.read_csv(filepath, sep, header, names, index_col, usecols, skiprows):
    # filepath => this is simply a path to the file we want to upload to a dataframe (if our python script is in the same folder as this file, we can just write the name of the file)
    # sep => this is a very important variable that tells the function which separator was used to separate values in different columns (for example, we might have in our file values
        # that are separated by a white space (a b c d), or a comma (a,b,c,d), or a tab (a  b   c   d)). The 'sep' variable would be defined as sep = ' ', sep = ',', sep = '\t', respectivelly
    # header = the row number that contains the names of the columns (or column labels). If we don't pass anything, the first row will be considered as column labels, if we pass header=None, 
        # then the column names are generated automatically as '0', '1', '2', etc. We can change the column labels later on. 
    # names => a sequence of column labels we want to apply - if the file we are uploading already has some column labels, we need to define header = 0 so that the names variable can overwrite
        # those lables with the ones we define
    # index_col = name of the column to use as indices. For example, if we already have a column in our table that's called "sample number", we might pass that column as index_col. If
        # we pass index_col = None, the indices will be generated automatically as 0, 1, 2, etc.
    # usecols => sometimes we might need only a fraction of the data from our file. In that case we can upload only certain and specific columns to our DataFrame, for example:
        # usecols = ['name', 'age', 'weight', 'height']
    # skiprows => if we already know that we want to skip certain rows and we know their index, we can upload the whole table without them: for e.g skiprows = [1,5] will skip the 
        # second and the sixth row (indices start from 0). Keep in mind that the indices will change as a result of removing two rows!

# As promised, let's now look a bit closer to the 3 possible scenarios regarding the column names: 1. our data is already organized in columns with defined names, 
# 2. the columns don't have the names yet, but we know how we want to name them, 3. we have no idea what our column contain and what names to give them. 
# All three scenarios have a solution, as shown below:

    # 1. column names already exist
patient_data = pd.read_csv('patient_data.csv', sep = ',', index_col = None, header = 0)
patient_data.head(10)


    # 2. column names known, but don't exist in the current table
cols = ['identification', 'age', 'gender', 'height', 'weight', 'BMI']
patient_data_cols = pd.read_csv('patient_data_no_columns.csv', sep = ',', index_col = None, header = None, names = cols) # It's important to define the header as None otherwise we will
                                                                                                                        # loose the first data point as the first row will be considered as column labels
                                    # in case our file contains column labels, but we want to change them, the command would look like this: 
                                    # patient_data_cols = pd.read_csv('patient_data.csv', sep = ',', index_col = None, header = 0, names = cols)
patient_data_cols.head(10)



    # 3. column names unknown and don't exist in the current table
patient_data_no_cols = pd.read_csv('patient_data_no_columns.csv', sep = ',', index_col = None, header = None) # here it is important to pass header = None, otherwise the first row will be taken as column labels
                                                                                                        # and we will lose one data point!
patient_data_no_cols.head(10)

# We can add the column names at some point later on, like this:
patient_data_no_cols.columns = cols
patient_data_no_cols.head(10)

#####

## 1.6. VIEWING DATA --> head, tail, shape, info, list column names

# Usually, our dataframes are very big and if we try printing them out in our terminal with the print function, only the first few and the last few rows and columns will appear as the 
# whole dataframe is too big to be printed out as a whole. For these purporses, we can use the built-in functions .head() and .tail(), which enable us to see a specified number 
# of rows. This comes in handy if we just want to quickly check the data we have in the table, or if some change that we made has been successfully applied to the dataframe. 
# Furthermore, sometimes, we might not know the size of our dataframe, what columns it contains, what are the names of these columns etc and instead of having to open the file physically
# each time to check those things, we can use some of the built-in functions of the pandas library to quickly find out this information.

# Using .head() and tail() to print the data
patient_data.head() # if we don't specify the number of rows we want to see, the .head() function by default prints the first 5 rows
patient_data.head(10)

patient_data.tail() # if we don't specify the number of rows we want to see, the .tail() function by default prints the last 5 rows
patient_data.tail(10)

# .shape function enables us to check how many rows and columns our dataframe consists of:
patient_data.shape    # the output is given as a pair of values, for example (2,3) in which the first value stands for the number of rows and the second value for the number of columns in 
                        # our dataframe. In case there is only one column, the shape will be (2,)

# .info() function allows us to see some additional information such as data type of values in each column, the number of NaNs in each column, etc. 
patient_data.info(verbose = True) # gives us the information of all columns
patient_data.info(verbose = False) # gives us the summary of coluns count and its dtypes, but not per column information

# .columns.tolist() and list(DataFrame) enable us to get a list of all column labels - this is also an important step in getting to know your data!
patient_data.columns.tollist()
list(patient_data)

#####

## 1.7. OUTPUTTING FILES

# Once we have done some changes to our data, or maybe even have created a new dataframe, we usually want to store it in some type of a file. To do this, we need to output the created 
# dataframe into a .csv, .tsv or .txt file using the function .to_csv().
# This function also has several variables that we can define when calling it and they can be found on the official documentation page of pandas. For our purposes, we will go over only the
# most commonly used variables:
# df.to_csv(path, sep, columns, header, index, index_label, encoding):
    # path => the name of the output file we want to create, or the full path if we want to store it somewhere other than the folder where our script is located. The name of the file must contain 
        # either .csv, .tsv or .txt
    # sep => we need to define the separator of the values when writing out our dataframe to a file, just like when uploading data to a DataFrame. If our output file is .csv, the separator is usually
        # ',', for the .tsv file the separator is a tab '\t', and if the output file is a .txt, the separator is usually a whitespace or a tab (' ', '\t')
    # columns => if we want to write only specific columns into a file, rather than the whole dataframe, this is where we can define their names. For example columsn = ['identification','age', 'gender']
        # will only output those 3 columns from our patient_data dataframe
    # header => if we pass header = False, the column labels will not be written in the output file, otherwise, by default, header = True and the column labels will be written in the output file
    # index => if index = True (which is the default), the row indices will be written in the output file, otherwise they won't be written out in the output file
    # index_label => if we are printing out the index column, we might want to name it as for example "index" instead of having a blank space in our output file. This is where we can pass the desired
        # name for the index column
    # encoding => the most commonly used encoding is 'utf-8' (encoding = 'utf-8')

patient_data.to_csv('Patient_data_new.csv', sep = ',', index = False, encoding = 'utf-8')


#### 2. DATA CLEANING:

# In this section, we will cover some basic functions for handling our data. We will see how to look for missing values in our data and what to do with them, how to check for duplicates,
# how to rename, add and remove columns and how to use strip function to clean string variables from the columns.

## 2.1. Missing values (check, count, remove, fill)

# Often times, our data will have certain values missing - maybe we forgot to input data in all columns, or some information about our sample i snot available to us. Either way, we need to 
# acknowledge those missing values (also called NaN values) and decide what to do with them, because they are going to cause us problems later if we decide to perform some mathematical operations on our data 
# (e.g. finding averge value or standard deviation etc). The way we handle missing values depends on the type of data we are missing (are we missing numbers or words - for example we could be missing the age 
# of some patient or their date of birth or their country of residence) and how many values are missing. FYI: Keeping the missing values in mind is also very important when performing some of the standard 
# statistical tests on our data or if we are going to input our data in some machine learning algorithm. Generally, missing values are the first thing to look into and decide what to do with them -> we can either 
# remove the data points that have some missing values, or we can fill in the missing values (for example we can calculate the average of the whole column and replace all NaNs with this average).

# FINDING NAN VALUES:
# Just to visualize the NaN values in the dataframe, we can quickly look at it like this:
patient_data.head(10)
# There are a few ways to check for NaN values in your data.
# First way will give us a dataframe just like the one with our original data, but the actual values of our data are replaced with a boolean variable - True if the value is NaN or False if the value is no NaN:
patient_data.isnull()

# A more summarized way is to check whether any of our columns contains at least one NaN value:
patient_data.isnull().any() # This outputs the names of all columns and next it a boolean variable - True if there is at least one NaN value in that column and False otherwise

# If we are interested in the total number of missing values in each column, we can check with:
patient_data.isnull().sum()

# Now that we have the information which columns contain NaN values and how many NaN values there are, we might want to look at the exact rows (or data points) that are missing these values:
nan_rows = patient_data[patient_data['gender'].isnull()]  # instead of 'gender', you can write whatever is the name of the column you wish to inspect
nan_rows

# REMOVING NAN VALUES:
# Once we know where the NaN values are and how many of them do we have to deal with, we can decide what to do with them. In case you decide to delete them (for example if there is a certain data point 
# that has missing values in multiple columns, or if there is a small number of datapoints with NaN values compared to the total number of datapoints you have for the analysis), this is how you do it:
no_nans = patient_data.dropna(axis = 0) # axis = 0 means we want to delete rows, if we wrote dropna(axis =1), this would remove all columns that have at least one NaN value
# We can now again check whether all NaNs have been removed:
no_nans.isnull().any()  # we should see False for every column now!

# REPLACE THE MISSING VALUES
# Another option is to fill the missing values with some arbitrary value - an average/a zero or some chosen word if we are missing a value in the column with strings:
# first let'sprint out the first few rows of our original data again just to have it for the reference
patient_data.head(10)
# Now let's fill all the NaNs with a zero (0):
nan_to_zero = patient_data.fillna(0)
# Check how the dataframe looks now:
nan_to_zero.head(10)
# Check if there are any NaNs left:
nan_to_zero.isna().any()
# In this example we can see that adding a zero could work for all columns but the "gender" column, where we are missing a word (female/male). We can fox this by separately filling the NaN values
# of the columns with integers (numbers) and those with strings (words). This time, we will fill it with a mean value instead of with a zero:
nan_to_mean = patient_data.fillna(patient_data.mean(numeric_only = True))
nan_to_mean.head(10)
nan_to_mean.isnull().any()
# We still have to fill in the missing gender of one data point. We will do this by using a df.mode() function, which looks at our original dataframe (patient_data) and for each column that's missing
# a string value, it checks which string occurs the most in each column and fills the NaN values with those strings: 
finally_no_nan = nan_to_mean.fillna(patient_data.mode().iloc[0])
finally_no_nan.head(10)
finally_no_nan.isnull().any()


## 2.2. Duplicates
# Before doing any kind of further analysis with our data, we also need to check whether we have the same data point enter more than once. This can happen if you forgot that you've already added this
# data point to your table, if you are working with someone else and you both enter the same data point or, in case we are working with the questionnaries, one patient by mistake filled our questionnaire
# twice.
# First let's check if there's any duplicates in the first few rows of our dataframe:
finally_no_nan.head(10)
finally_no_nan.shape
# We can spot two duplicates right away. Now to remove those duplicates, we can simply say:
finally_no_nan.drop_duplicates(inplace = True)
finally_no_nan.shape
# The inplace = True variable tells the drop_duplicates function to do it on our original finally_no_nan dataframe and not to create a new dataframe with 
# these changes. If we don't specify inplace = True, the finally_no_duplicates dataframe will not be changed and in that case we need to save the changes in the new dataframe, for example like this:
# new_df = finally_no_nan.drop_duplicates(). Many functions in pandas have the inplace variable which can be called and set to True when using these functions, but it's important to first check in the
# official pandas ocumentation of the specific function we wish to use whether it's possible to do the changes inplace, or do we always need to define a new variable (create a new dataframe) where the 
# changes will then be saved. Both choices have some pros and cons - if we are always making changes in place, we need to be very careful because once the changes are made, we can't undo it because our
# original variable has been changed. On th eother hand, creating a new variable for every change that we make takes up a lot of memory of the computer and of ourselves - it's hard to keep track of all the
# variables and the differences between them. The best practice is to create copies of your dataframe every now and then and before making big changes to the data, so that even if we realize we messed something 
# up, we don't have to go all the way back to the beginning, but rather start from just a few steps back.


## 2.3. Rename columns
# Sometimes we might not like the column name and wish to change it. We can do this simply like this:
finally_no_nan.rename(columns={'identification': 'patient_id', 'gender': 'sex'}, inplace = True)  # This allows us to rename one or multiple columns. Note that we are again using the inplace = True variable


## 2.4. Add/remove columns and/or rows (drop, apply, iloc, loc)
# Sometimes, we might realize there is a column in our data that is not really useful for us for anything and we can remove it from our dataframe. We would do hat like this:
finally_no_nan = finally_no_nan.drop(columns = 'input_number')      ## THIS IS CALLED THE LOC METHOD, because we are LOCATING the column by its name (LOCATION = .loc())
finally_no_nan.head(10)
# If our columns don't have names, but we know the index of the column we wish to remove (the first column has index 0, the second 1 and so on), we can do it like this:
#!!!! finally_no_nan = finally_no_nan.drop(finally_no_nan.columns[6], axis = 1)  --> I counted that the 'input_number' is the seventh column, which means its index number is 6.
        # THIS IS CALLED THE ILOC METHOD, because we are LOCATING the column by its INDEX (INDEX + LOCATION = I + LOC = .iloc())


# Sometimes we might want to remove or add some data point (rows). When removing rows, we need to know their index, which in pandas starts from 0 (so the first row has index 0, the second row index is 1 etc.).
# Let's say we want to remove the last row from our dataframe, we can do that like this:
finally_no_nan.tail(10)
finally_no_nan = finally_no_nan.drop(finally_no_nan.index[-1]) # the last element of a table (the last row/column) or of a list can be assessed with x[-1]
finally_no_nan.tail(10)


# In other cases, we might want to add an additional column. For example, in our dataframe we have a column named BMI and we could add an additional column where we would indicate for each patient whether 
# she/he is overweight (BMI > 25) or not. This is how we can do it:
finally_no_nan['overweight'] = finally_no_nan['BMI'].apply(lambda x: 'Yes' if x > 0.54 else 'No') # The apply function in pandas is used when we want to iterate over each data point in our dataframe and 
# use it in some function. For example, here we used it with a simple if statement, saying if the current value from the 'BMI' column is larger than 25.0, write 'Yes' in the newly formed column 'overweight',
# otherwise, write 'No'. In general, when we want to add a new column to our dataframe, we do it by saying dataframe['column name'] - if the column with that name doesn't exist, this function will create it.
finally_no_nan.head(10)

# We can also add a new row to our dataframe. In order to do that, we need to know the values for all columns of the new data point and we need to represent it in the form of a dictionary:
new_datapoint = {'patient_id': '05_001', 'age': 76, 'sex': 'female', 'height': 170, 'weight': 60, 'BMI': 0.33, 'retired': 'No', 'Address': '123 Middle Earth',  'overweight': 'No'}
finally_no_nan = finally_no_nan.append(new_datapoint, ignore_index=True)
finally_no_nan.tail(10)


## 2.5. Strip function (lstrip,rstrip)
# While inspecting the strings in our dataframe, we might notice that some of the strings have some typos, as shown in a few examples in our data:
finally_no_nan.head(10)
# We can fix these strings so that they are all in the same format by removing typos and/or replacing words. We will touch upon the replace function in a little bit, and we will now focus only on the strip 
# function. The .strip() function can be applied to the whole dataframe, or to a specific column. You will almost always want to do column by column because removing for example '-' from one column might 
# cause errors and we might not actually want that. Additionally, in order to be more specific, we can also define whether we want the .strip() function to strip some characters from the beginning of our strings
# or the end. We do this by using .lstrip() to strip from the beginning (left side of the string) or .rstrip() to strip from the end of the string (right side of the string).
finally_no_nan['sex'] = finally_no_nan['sex'].str.lstrip("...")
finally_no_nan.head(10)
finally_no_nan['sex'] = finally_no_nan['sex'].str.lstrip("/")
finally_no_nan.head(10)
finally_no_nan['sex'] = finally_no_nan['sex'].str.rstrip("/")
finally_no_nan.head(10)


#### 3. DATA MANIPULATION
# Now that we have taken care of our data - we know the columns that we have, we got rid of some columns that were not needed and maybe added a new column with 
# some important information, we took care of the missiung values and corrected the typos in or string variables; we can finally start working with the data!
# Sometimes in your analysis you might want to work with just one isolated column, or you might want to split one column into two, or transofrm the data from
# one or multiple columns, replace some values with some other, group all the data based on values in one column etc. That's exactly what we are going to briefly
# cover in this section (we will just scratch the surface! :) )

## 3.1. Selection operation ([],iloc,loc)
## Selection operation is something you are going to need often and after a while you won't even notice you are using it. Selection function is almost always used in combination with another function, because, 
# once you've selected the part of the dataframe you want to work with, you will usually start working with it right away! Pandas has this super cool feature that a lot of the code can be written in one line 
# because functions are executed one by one. All you need to take good care about in case you write one-line code is the parenthesis - they can make a huge difference! So when using the selection function, you will 
# usually use it in the same line with some other function, as we will show below.

# Now, there are several ways to select the part of the dataframe and we are going to cover all of them:
        # a) accessing one or multiple columns using []
        # b) accessing rows and columns by location using iloc
        # c) accessing rows and columns by location using loc
        # d) accessing rows and columns by conditions

# a) using []:
# Let's say we are interested into the average hight among our patients. calculate that, we can say:
height = finally_no_nan['height']
height
height.mean()
height.max()
type(height)
# Importantly, the newly made variable height is pandas Series! Sometimes you might by mistake define a certain variable as a pandas series and then try and apply some of the dataframe functions on it. This will 
# result in an error and you'll have to transform the series into a dataframe. If you want to isolate one column from your dataframe and store it as a new dataframe (instead of as a pandas series), this is how you do it:
height_df = finally_no_nan[['height']]
type(height_df)
# If you want to select multiple columns at the same time, the only way to do it is by storing it in a new dataframe, so you can't make the mistake described above :) 
height_and_weight = finally_no_nan[['height', 'weight']]
height_and_weight
type(height_and_weight)
# If you want to check the mean weight and/or height, you can do it as in the first example above

# b) and c) using .loc and .iloc
# Let's suppose you don't know the names of the column you need, or the columns don't have names or labels. In such cases, the only way to tell pandas which columns to select is by locationg them by their indices.
# As was already described above, the indices of rows and columns start from 0. Let's say we want to select the first row and first and third column:
finally_no_nan.iloc[0,[0,2]] # if you want, you can also store this in a separate variable by writing variable_name = and then the selection function
#While .iloc enables us to locate parts of the dataframe based on the indices of columns, the .loc function will locate the columns based on their labels or names:
finally_no_nan.loc[0,['patient_id', 'sex']] 
# If we want all the rows of the selected columns, we would just write:
finally_no_nan.iloc[:,[0,2]] # the ':' means every row
# if we want all collumns from just rows 0-5
finally_no_nan.iloc[0:6,:] # in pandas when we want a counter to go up to a certan number N, we need to write N+1 because the counter will go up until that number but not including that number
# similarly, we can use the .loc function to get the ranges of columns and/or rows:
finally_no_nan.loc[5:10, 'patient_id':'height'] # this will give us the rows 5, 6, 7, 8 and 9 and columns from identification to height

# d) using conditions:
# let's say we want to look at all the female patients:
only_female = finally_no_nan[finally_no_nan['sex'] == 'female']
only_female
# now let's say we only want female patients older than 70 years old:
older_female = finally_no_nan[(finally_no_nan['sex'] == 'female')&(finally_no_nan['age'] > 70)]
older_female

## 3.2. Standardizing/formatting column values using replace:
# If we look at the current column 'retired', we can see that there are different inputs for words yes and no:
finally_no_nan['retired']
# In such cases, it's better to standardize all the inputs to the same format, using the replace function:
finally_no_nan ['retired'] = finally_no_nan['retired'].str.replace('Yes','Y')
finally_no_nan ['retired'] = finally_no_nan['retired'].str.replace('YES','Y')
finally_no_nan ['retired'] = finally_no_nan['retired'].str.replace('yes','Y')
finally_no_nan ['retired'] = finally_no_nan['retired'].str.replace('No','N')
finally_no_nan ['retired'] = finally_no_nan['retired'].str.replace('NO','N')
finally_no_nan ['retired'] = finally_no_nan['retired'].str.replace('no','N')
finally_no_nan['retired']

## 3.3. Standardizing/formatting column values using apply:
# This is something we have already done in one of our exercises: we added a new column 'overweight' to our dataframe,
# where we stored either Yes or No if the BMI value of each patient was >25 or <=25 respectively. With 'apply' we are 
# applying the function defined within the brackets of the .apply() function to every row of the desired column.
# Another example of how we can you the .apply() function is directly on the values of some column, which will then 
# change them. For example, let's say we want to change our patient ids so that all ids that start with 01- are turned 
# into 1, those with 02- to 2, 03- to 3, 04- to 4 and 05- to 5:
finally_no_nan['patient_id'] = finally_no_nan['patient_id'].apply(lambda x: x.split('-')[0][1]) # here we are simply saying
# take one row value of the column patient id at a time, store it in the variable x, split the string value stored in x 
# by the character '-', so that everything before this character is the first element of the string (remember that the first
# element has index 0!) and everything after '-' is the second element of the string (for example 01-001 will be split into
# 01 and 001). Lastly, by adding a [0] to x.split('-')[0], we are taking only the first element (indexed as 0!). 
# The first element in our example is 01, and it further consists of two characters: 0 and 1. By putting a [1] at the end 
# of x.split('-')[0][1], we are saying give me just the second character (in our case 1) and change the row value into this character.
# The changed dataframe now looks like this:
finally_no_nan.head(10)

## 3.4. Splitting columns:
## DISCLAIMER! The Address data used in this example was taken from here: https://github.com/AlexTheAnalyst/PandasYouTubeSeries/blob/main/Customer%20Call%20List.xlsx
# Next, we are going to look at our column 'Address':
finally_no_nan['Address']
# We can see that in some cases we have just the street name, sometimes we have the name of the city and sometimes we have the name 
# of the state. Let's say we want to standardize this so that in one column we only have the names of the streets, in another one the
# names of the city and in the last one state names. Luckily, all three of those names are separated by a comma, which means we can 
# again use the .split() function to split the string variables in each column. First let's see what happens if we specify to the split 
# function to just look at the first comma:
finally_no_nan['Address'].str.split(',', 1 , expand = True)
# You can notice that the names of the streets are now put into a separate column from the names of the city and states. Now let's try 
# splitting by the first 2 commas:
finally_no_nan['Address'].str.split(',', 2, expand = True)
# Lastly, we want those three columns to now be added to the dataframe, and we want to give them names:
finally_no_nan[['Strees_address','State','Zip_code']] = finally_no_nan['Address'].str.split(',', 2, expand = True)
finally_no_nan.head(10)

## 3.5. Filtering down rows of data
# Let's now suppose that we are only interested in the patients that are not overweight and we want to look at them separately.
# In order to remove all data point (a.k.a. all rows) that belong to patients that are overweight, we are going to formulate 
# a simple for loop and iterate over all rows based on their indices (so using the .loc()) and removing any row that does not
# satisfy the condition 'overweight' = No:
for x in finally_no_nan.index:
    if finally_no_nan.loc[x, 'overweight'] == 'Yes':
        finally_no_nan.drop(x, inplace = True)
finally_no_nan
# We can see in the resulting dataframe that there are some indices missing, because those rows have been removed as their value in the column 
# 'overweight' was 'Yes.

## 3.6. Groupby function
# As a last exercise in this section on data manipulation, let's say we want to separately look at male and female patients.
# In order to separate the dataframe so that it first shows as all male patients and then all female, we are going to use the .groupby() function:
grouped_df = finally_no_nan.groupby('sex').reset_index()
grouped_df
# The reset_index() function is used to reset the index of a grouped DataFrame, creating a new DataFrame with a default integer index. If we don't
# write the reset_index() function, the output of grouped_df would not a be a formed dataframe, but will rahter look like this: 
# <pandas.core.groupby.generic.DataFrameGroupBy - it would just store the type of object of variable grouped_df

#### 4. WORKING WITH MULTIPLE DATAFRAMES:
# Often times in our work we need to work with multiple dataframes. It can happen that the data was collected on two separate computers ad now you want
# to create a single dataframe which will contain all the data, or it an happen that you were collecting different information in two separate tables
# and now you want to merge them so that you add the additional information of each patient from the second table to their data from the first table.
# Since this step is usually done at the beggining before you do any other data manipulation, we are going to reupload our patients' data. However, for
# the purpose of showing the .concatanate() function, we have previously manually separated the patients' data into two files: general_data_1.csv and 
# general_data_2.csv. We will uppload both of those to separate variables and we will also upload a different table called clinical_data.csv to a 
# separate dataframe to demonstrate the use of the .merge() function.

## 4.1. Merging dataframes by a mutual column:
# First, we are going to show how to merge two dataframes based on a column that is mutual to both tables. Let's reuse the patients data uploaded at the 
# beginning into a dataframe patient_data_cols and upload the clinical data to a separate dataframe:
clinical_data = pd.read_csv('clinical_data.csv', sep = ',', index_col = None, header = 0)
# Let's quickly check the two dataframes:
patient_data_cols.head(10)
clinical_data.head(10)
# We can also check their column labels by:
patient_data_cols.columns()
clinical_data.columns()
# We can see that there are some columns mutual to both dataframes (indentification and gender), which makes it possible for us to merge those two dataframes into one.
# The .merge() function basically takes one dataframe and pastes it to the left or right to the other dataframe - so we are adding new columns. Later we will work with 
# the function .concat(), which does the oposite: it takes one dataframe and pastes it below the other one, thereby adding new rows to the same dataframe.
# Now let's merge the two daatframes based on their mutual column 'identification':
merged_df = pd.merge(patient_data_cols, clinical_data, on='identiication', how='inner')
# The variable 'how' gives us a very cool option: because of this variable, we don't need to have the same number of rows and all identification strings in both dataframes.
# Under 'how=' we can write several options:
            # Inner join keeps only the matching rows from both DataFrames.
            # Outer join keeps all rows and fills in missing values with NaN.
            # Left join keeps all rows from the left DataFrame and adds matching rows from the right DataFrame.
            # Right join keeps all rows from the right DataFrame and adds matching rows from the left DataFrame.

# The merged_df looks like this:
merged_df

## 4.2. Concatanating dataframes:
# Let's first upload the two dataframes that we want to concatanate one on top of the other:
general_data_1 = pd.read_csv('general_data_1.csv', sep = ',', index_col = None, header = 0)
general_data_2 = pd.read_csv('general_data_2.csv', sep = ',', index_col = None, header = 0)
# Let's quickly check the two dataframes:
general_data_1.head(10)
general_data_2.head(10)
# By this brief inspection, we can see that the number of columns, their labels and the content in the two dataframes is equivalent and we could "copy and paste"
# one on top of the other. That's exactly what the .concat() function does. In order to be able to check if the concatanation was successfull, we are going to 
# check the shapes of each dataframe and compare it to the shape of the final, concatanated dataframe (the number of rows should be equal to the sum of rows
# from the first and the second dataframe):
general_data_1.shape
general_data_2.shape
# Now let's concatanate them:
concatenated_df = pd.concat([general_data_1, general_data_2], ignore_index=True)
# The .concat() function already has a built in feature that takes care of your headers so that the header of the second dataframe is removed and only the one 
# at the very beginning remains in the concatanated dataframe. The .reset_index() creates new indices for the new concatanated dataframe. Let's visually inspect
# the concatanated_df and check its shape:
concatenated_df.head(15)
concatenated_df.shape
# We can see now that the two dataframes have been successfully added one on top of the other! :)

##############################################################################################
##############################################################################################
##############################################################################################

# Pandas is a very cool library, it was written specifically for data handling and therefore has the biggest number of built in functions for working with tables. 
# Trust me, if there is something you need to do with your table, there is a way to do it with pandas! Since with this short lecture we have only scratched the surface, 
# I would highly encourage you to expand your knowledge and learn a few more tricks with pandas. There is a very nice page called leetcode.com with a huge database of 
# programming tasks, ranging from easy to medium to hard. You can create an account there and search specifically for the tasks that require you to work with pandas. The
# cool thing about leetcode is that they already have the test cases incorporated to the page so your solution is tested right away. Additionally, since it is a community
# based page, people post their solutions to every programming task in the database, so you can learn from others as well :) I have personally done their 30 days pandas 
# challenge with 30 tasks and would highly recommend for you to try it: https://leetcode.com/studyplan/30-days-of-pandas/. In case for whatever reason you can't see the 
# challenge, send me an email to desika.kolaric@gmail.com and I can send you the print out of all the task descriptions and my solutions. ;)

# Another tip for your future programming: whenever you don't know how to solve something, try searching the internet. Stack overflow (https://stackoverflow.com/) is another
# huge platform where anyone can ask a specific question regarding their problem and others will propose a solution. In my experience, this is by far the most useful page 
# to search for ideas on how to solve your problem. Recently with the whole ChatGPT era, it has become pretty convenient to also describe your problem very specifically 
# to ChatGPT, which then gives you a "ready-to-use" solution code. However, I would caution you not to trust it completely - ChatGPT actually can make a lot of mistakes when
# coding and if you just blindly copy and paste everything it offers you as a solution to your code, you might end up going in circles with the same error. This has happened
# to most of us and sometimes you just need to learn it the hard way :D In my opinion, ChatGPT can be a great resource for you to quickly and in one place find out about the
# funcitons that you could possibly use to solve your problem and to get the general idea of how to approach it - should I use the loop, the matrices, the list, how can I 
# output the result etc. Therefore, the best approach is to ask " What functions can I use to solve (insert your problem description)" and once it gives you a solution, try 
# to really understand the code before you use it, because sometimes you will notice the potential errors right away and save yourself some precious time (and pain and misery (: ).
# In short, use it as a starting point, but never use it as ground truth.

# Good luck and don't give up! It can get hard for all of us and even for the best ones out there :)! Cheers!

