0x0B. - Python - Loading Data in Pandas
=======================================

<h1 align="left">Loading DataFrame </h1>

Pandas is a module for working with tabular data, like spreadsheets or databases. With pandas we can do the following
-   Search for particular rows and columns from loaded data
-   Calculate aggregate statistics like averages or standard deviations
-   Combine data from multiple sources

Pandas introduces a new data type the `DataFrame`. Loading data into a `DataFrame` is the first step to using pandas.

**CSV File:**
-   Comma Separated Values
-   CSV file is an easy way to create a `DataFrame`
-   CSV file stores tabular data as text.only file
-   CSV file can be gotten from Excel spreadsheet, SQL database, Google Sheet

**Note:**
-   We first import the pandas module using its alias
-   Then we use the function `pd.read_csv` to turn the CSV file to a DataFrame, the function takes the name of the CSV file as a string like this; pd.read_csv('ransom.csv') assuming the name of the CSV file is `ransom.csv`
-   We save the DataFrame to a variable called `df` like this `df = pd.read_csv('ransom.csv')`

When inspecting a DataFrame, we don't print the entire DataFrame, we just view a few information like the first five lines, in doing this we use the two types of function and we call this function types `method`

-   `.head`; this selects the first five rows of a DataFrame saved to a varaible
-   `.info`; this is useful for DataFrame with many columns that are difficult to display using the `.head` method

**Examples:**
-   Giving a Dataframe, df = pd.read_csv('ransom.csv'), 
	-   the `.head method` will present it as `print(df.head())`
	-   the `.info method` will present it as `print(df.info())`


Exercises
---------

### 0\. Loading a DataFrame

We've obtained credit card records for all four suspects. Perhaps some of them made suspicious purchases before the kidnapping? Write a script that display the first five rows of `credit_records` using the `.head()` method.

The records are in a CSV called `"credit_records.csv"`

**NB:**
-   Import `pandas` module under the alias `pd`
-   Load the CSV `"credit_records.csv"` into a DataFrame called `credit_records`


**Repo:**
-   GitHub repository: `datacamp-data_analyst-science_with_python`
-   Directory: 0x0B-loading_data_in_pandas
-   File: [0-dataframe.py](./0-dataframe.py)
---

### 1\. Inspecting DataFrame

We've loaded the credit card records of our four suspects into a DataFrame called `credit_records`. Let's learn more about the structure of this DataFrame. Write a script displaying how many rows are in `credit_records`?

-   in [0-dataframe.py](./0-dataframe.py)
-   The `pandas` module has been imported under the alias pd. 
-   The DataFrame `credit_records` has already been imported
-   Use the `.info()` method to inspect the DataFrame `credit_records`.

**Repo:**
-   GitHub repository: `datacamp-data_analyst-science_with_python`
-   Directory: 0x0B-loading_data_in_pandas
-   File: [1-dataframe.py](./1-dataframe.py)
---

<h1 align="left">Selecting Columns </h1>

The first way we use data load from a CSV file is by selecting columns. By selecting columns we will be getting all the values from a particular column in a DataFrame

**Essence of Selecting Columns:**
-   Used in calculations
	-   `credit_records.price.sum( )`; this code selects the column `price` and calls the method `.sum` on that column
-   Used as the input of a function e.g plot data
	-   `plt.plot(ransom['letter'], ransom['frequency']`; this will create a plot of the `frequency` of each `letter` in the `ransom` as the data comes from a DataFrame `ransom` with columns `letter and frequency`

**How to Select Columns:**
-   Selecting with a bracket and string notation - `suspects = credit_records['suspect']`
-   Selecting with a dot notation - `price = credit_records.price`

**Note:**
-   Column names with spaces or special characters `(- or ?)` are put in brackets and strings
-   Brackets `[ ]` are not the same as Parenthesis `( )`
-   Parenthesis are used when we want to use the DataFrame as a function

Exercise
--------

### 2\. Two methods for selecting columns

Once again, we've loaded the credit card records of our four suspects into a DataFrame called `credit_records`. Let's examine the items that they've purchased.

-   The `pandas` module has been imported under the alias `pd`.
-   The DataFrame `credit_records` has already been imported.

Write a script that selects from the DataFrame `items`
-   the column `item` from `credit_records` using brackets and string notation and display the column `items`
-   the column `item` from `credit_records` using dot notation and display the column `items`

**Repo:**
-   GitHub repository: `datacamp-data_analyst-science_with_python`
-   Directory: 0x0B-loading_data_in_pandas
-   File: [2-selecting_columns.py](./2-selecting_columns.py)
---

### 3\. Correcting column selection errors

A junior detective tried to access the location columns of `credit_records`, but he made some mistakes. Help correct his code so that we can search for suspicious purchases.

-   In all exercises going forward, `pandas` will be imported as `pd`. 
-   The DataFrame `credit_records` has already been imported.

Correct the code so that it runs without errors.

```
location = credit_records[location]
items = credit_records."item"
```

**Repo:**
-   GitHub repository: `datacamp-data_analyst-science_with_python`
-   Directory: 0x0B-loading_data_in_pandas
-   File: [3-selecting_columns.py](./3-selecting_columns.py)
---

### 4\. More column selection mistakes

Another junior detective is examining a DataFrame of Missing Puppy Reports. He's made some mistakes that cause the code to fail.

-   The `pandas` module has been loaded under the alias `pd`,
-   and the DataFrame is called `mpr`.

**4a:** Inspect the DataFrame `mpr` using `info( )`.

**4b:**
Correct the mistakes in the code so that it runs without errors.

```
name = mpr.Dog Name
is_missing = mpr.Missing?
```

**Repo:**
-   GitHub repository: `datacamp-data_analyst-science_with_python`
-   Directory: 0x0B-loading_data_in_pandas
-   File: [4-selecting_columns.py](./4-selecting_columns.py)
---

<h1 align="left">Selecting Rows </h1>

To select rows we use logical statements. In python, logical statements checks for a relationship between two values, such as equal to `=` or greater than/lesser than `>` / `<` and returns `True` or `False` 

**For Example:** 
```
question = 12 * 8
solution = 96
```

If we compare the variables of `question` and `solution` as below

```
question == solution
True
```

This test if the two variables are the same, in this case they are, so it returns `True`. The `True` python returns is a special data type called `Booleans`

**Booleans** 
-   This is a data type
-   We use it to select rows where the value of a column matches a specific value
-   There are only two booleans, `True` or `False`

**Types of Logic**
-   `>` - greater than
-   `<` - lesser than
-   `==` - equal to
-   `>=` - greater than or equal to 
-   `<=` - lesser than or equal to
-   `!=` - not equal to

**Example 1:**
```
price = 2.25
price > 5.00

False
```

**Example 2:**
```
name = 'bayes'
name !='Bayes"

True
```

In a DataFrame, we can compare one value to all the values in the DataFrame

**Examine The Following:**

**Example 1.** 
-   credit_records[credit_records.price > 20.00]
	-   `credit_records`, is the DataFrame
	-   `[ ]`, is a bracket or square bracket
	-   `credit_records.price > 20.00`, is a logical statement

This means, in all rows of the DataFrame `credit_records` the price is greater than 20.00

**Example 2.** 
-   credit_records[credit_records.suspect == 'Ronald Alymer Fisher']
	-   in the case `credit_records.suspect == 'Ronald Alymer Fisher'` is the logical statement

This means in all rows of the DataFrame, `credit_records` the suspect is equal to Ronald Alymer Fisher

Exercises
---------

### 5\. Logical testing
Let's practice writing logical statements and displaying the output.

Recall that we use the following operators:

-   `==` tests that two values are equal.
-   `!=` tests that two values are not equal.
-   `>` and `<` test that greater than or less than, respectively.
-   `>=` and `<=` test greater than or equal to or less than or equal to, respectively.

Write the following code of logical testing
-   The variable `height_inches` represents the height of a suspect. Is `height_inches` greater than `70` inches?
-   The variable `plate1` represents a license plate number of a suspect. Is it equal to `FRQ123?`
-   The variable `fur_color` represents the color of Bayes' fur. Check that `fur_color` is not equal to `"brown"`.

**Repo:**
-   GitHub repository: `datacamp-data_analyst-science_with_python`
-   Directory: 0x0B-loading_data_in_pandas
-   File: [5-logical_operators.py](./5-logical_operators.py)
---

### 6\. Selecting missing puppies
In our DataFrame of missing puppies, which is loaded as `mpr`. 
Let's write code to the following.

-   Select the dogs where `Age` is greater than `2`.
-   Select the dogs whose `Status` is equal to `Still Missing`.
-   Select all dogs whose `Dog Breed` is not equal to `Poodle`.

**Repo:**
-   GitHub repository: `datacamp-data_analyst-science_with_python`
-   Directory: 0x0B-loading_data_in_pandas
-   File: [6-logical_operators.py](./6-logical_operators.py)
---

### 7\. Narrowing the list of suspects

We'd like to narrow this list down, so we obtained credit card records for each suspect. We'd like to know if any of them recently purchased dog treats to use in the kidnapping. If they did, they would have visited `'Pet Paradise'`.

-   The credit records have been loaded into a DataFrame called `credit_records`.

With a code select rows of `credit_records` such that the column `location` is equal to `'Pet Paradise'`.

**Repo:**
-   GitHub repository: `datacamp-data_analyst-science_with_python`
-   Directory: 0x0B-loading_data_in_pandas
-   File: [7-logical_operators.py](./7-logical_operators.py)
---
