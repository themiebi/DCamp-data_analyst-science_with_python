0x00. Python - Getting Started in Python
========================================

<h1 align="left">Importing Modules </h1>

Modules helps group together related tools in python, thereby making it easy to know where to look for a particular tool, examples of modules are
 
-   `matplotlib`, create charts
-   `pandas`, loads tabular data
-   `scikit-learn`, performs machine learning
-   `scipy`, contains statistics functions
-   `nltk`, works with text data

**alias or as**
-   `seaborn as sns`
-   `statsmodels as sm`
-   `pyplot as plt`
-   `pandas as pd`
-   `numpy as np`

**NB:** 
-   To use modules you have to import them by using `import` before the module name
-   Aliasing a module is simply to shorten the module name, when doing that we us `as`

Exercises
---------

### 0\. Importing modules without an alias

Use an `import` statement to `import` `statmodels` without using an alias.

**Repo:**

-   GitHub repository: `datacamp-data_analyst_science_with_python`
-   Directory: `0x0A-getting_started`
-   File: [0-importing_modules.py](./0-importing_modules.py)
---

### 1\. Importing modules with an alias

Use an `import` statement to `import` `seaborn` using an alias.

**Repo:**

-   GitHub repository: `datacamp-data_analyst_science_with_python`
-   Directory: `0x00-getting_started`
-   File: [1-importing_modules.py](./1-importing_modules.py)
---

### 2\. Importing a package or library from a module using an alias

Use an `import` statement to `import` `pyplot` from `matplotlib` using an alias

**Repo:**

-   GitHub repository: `datacamp-data_analyst_science_with_python`
-   Directory: `0x0A-getting_started`
-   File: [2-importing_modules.py](./2-importing_modules.py)
---

<h1 align="left">Creating Variables </h1>

Variables helps us reference a piece of data for later use, giving us an easy to use short cut, and they are defined by the equal sign `(=)`

**some variables**
-   `name` = "Bayes"
-   `height` = 24
-   `weight` = 75.5

**NB:Rules for Defining Variables**
-   Must start with a letter (usually lowercase)
-   After the first letter variables can use letter, numbers, underscores
-   No spaces or special characters
-   Case sensitive [`my_var` is different from `MY_VAR`]
-   When displaying a variable, we use `print` with the variable name in a parenthesis `()` like this `print(height)`, the display the value assigned to `height`


**Valid Variables**
-   bayes_weight
-   b
-   bayes 42

**Invalid Variables**
-   bayes-height
-   bayes!
-   42bayes

**Flavours of Variables**
-   Floats; represent integers or decimal numbers for example `height = 24`; `weight = 75.5`

-   Strings; represents text, can contain letters, numbers, spaces and special characters, usually defined by either a single quotation mark `'..'` or with a double quotation mark `".."` uniformly for example `name = "Bayes"`; `breed = 'Golden Retriever'`

Exercises
---

### 3\. Creating a float

With a script define a variable called `bayes_age` and set it to `4.0`

**Repo:**

-   GitHub repository: `datacamp-data_analyst_science_with_python`
-   Directory: `0x0A-getting_started`
-   File: [3-creating_variables.py](./3-creating_variables.py)
---

### 4\. Creating a float

Write a script to displays the variable `bayes_age`.

**Repo:**

-   GitHub repository: `datacamp-data_analyst_science_with_python`
-   Directory: `0x0A-getting_started`
-   File: [4-creating_variables.py](./4-creating_variables.py)
---

### 5\. Creating strings

Write a script to define a variable called `favorite_toy` whose value is `Mr Squeaky`.

**Repo:**

-   GitHub repository: `datacamp-data_analyst_science_with_python`
-   Directory: `0x0A-getting_started`
-   File: [5-creating_variables.py](./5-creating_variables.py)
---

### 6\. Creating strings

Correct the mistakes in the following code so that it runs without producing syntax errors.

```
birthday = '2017-07-14"
case id = "DATACAMP!123-456?'
```

**Repo:**

-   GitHub repository: `datacamp-data_analyst_science_with_python`
-   Directory: `0x0A-getting_started`
-   File: [6-creating_variables.py](./6-creating_variables.py)
---

<h1 align="left">Functions </h1>

A function is an action, it turns input into output

**For Example:**
-   pd.read_csv( ); turns a csv file into a table in python
-   plt.plot( ); turns data into line plot
-   plt.show( ); displays plot in a new window

**Anatomy of a Function**
`plt.plot(df.letter_index, df.frequency, label = 'Ransom')`

-   `plt.plot`; is the Function
-   `df.letter_index, df.frequency,`; are Positional Argument
-   `label = 'Ransom'`; is a Keyword Argument

**NB:**
-   Functions begin with the module the function lives in 
	-   e.g `plt` as in `plt.plot` or `plt.show`
	-   also `pd` as in `pd.read_csv`
	-   where `plt` and `pd` are alias for modules plotly and pandas
-   Then followed by the name of the function e.g `plot`; `show`; `read_csv`
-   And these functions are always put in parenthesis `( )`

**Types of Input In Function**
-   Positional Argument; they tell the function how to do its job
	-   e.g `df.letter_index`, `df.frequency` as in `plt.plot(df.letter_index, df.frequency, label = 'Ransom')`
-   Keyword Argument; this states the name of the argument, and the argument its self, then an equals sign `(=)`
	-   e.g `label`; is the name of the argument
	-   also `'Ransom'`; is the argument

Exercises
---------

### 7\. Using a Function

The file `ransom.csv` represents the frequency of each letter in a ransom note, write a script using a function to load data into a `DataFrame` from the `CSV` file, then display the DataFrame, after saving it to a variable called `r`

-   Remember to use a module you have to first `import` it
-   `CSV`; means comma-separated value
-   Each scrpit should be in a new line

**Repo:**

-   GitHub repository: `datacamp-data_analyst_science_with_python`
-   Directory: `0x0A-getting_started`
-   File: [7-using_functions.py](./7-using_functions.py)
---

### 8\. Using a Function

Having already loaded the data into the DataFrame, using a function, write a script that plots a graph of `x_values` vs `y_values`, and displays the graph.

-   Remember to use a module you have to first `import` it

**Repo:**

-   GitHub repository: `datacamp-data_analyst_science_with_python`
-   Directory: `0x0A-getting_started`
-   File: [8-using_functions.py](./8-using_functions.py)

