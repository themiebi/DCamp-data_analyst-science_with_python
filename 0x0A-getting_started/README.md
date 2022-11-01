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

-   GitHub repository: `datacamp-data_analyst_with_python`
-   Directory: `0x0A-getting_started`
-   File: `0-importing_modules.py`
---------------------------

### 1\. Importing modules with an alias

Use an `import` statement to `import` `seaborn` using an alias.

**Repo:**

-   GitHub repository: `datacamp-data_analyst_with_python`
-   Directory: `0x00-getting_started`
-   File: `1-importing_modules.py`
---------------------------

### 2\. Importing a package or library from a module using an alias

Use an `import` statement to `import` `pyplot` from `matplotlib` using an alias

**Repo:**

-   GitHub repository: `datacamp-data_analyst_with_python`
-   Directory: `0x0A-getting_started`
-   File: `2-importing_modules.py`
---------------------------

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

-   GitHub repository: `datacamp-data_analyst_with_python`
-   Directory: `0x0A-getting_started`
-   File: `3-creating_variables.py`
---

### 4\. Creating a float

Write a script to displays the variable `bayes_age`.

**Repo:**

-   GitHub repository: `datacamp-data_analyst_with_python`
-   Directory: `0x0A-getting_started`
-   File: `4-creating_variables.py`
---

### 5\. Creating strings

Write a script to define a variable called `favorite_toy whose value is `Mr Squeaky`.

**Repo:**

-   GitHub repository: `datacamp-data_analyst_with_python`
-   Directory: `0x0A-getting_started`
-   File: `5-creating_variables.py`
---

### 6\. Creating strings

Correct the mistakes in the following code so that it runs without producing syntax errors.

```
birthday = '2017-07-14"
case id = "DATACAMP!123-456?'
```

**Repo:**

-   GitHub repository: `datacamp-data_analyst_with_python`
-   Directory: `0x0A-getting_started`
-   File: `[6-creating_variables.py](./2-importing_modules.py)`
---

