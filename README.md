# USTraffic2015
US Traffic 2015 dataset

Written by: Shashank Srivastava, PhD

<h3>Overview</h3>

main_notebook.ipynb is a Python notebook containing codes, results and analysis of US Traffic 2015 dataset (https://www.kaggle.com/jboysen/us-traffic-2015).
This notebook has been written with Python 3.7 and is forward compatible. The following native Python libraries and packages with version number have used in this code:

os
time
warnings
pandas 1.0.0
numpy 1.18.5
matplotlib 3.2.2

The raw data set has been read from a local path and which must be modified to re-run the code on a different system.
![image](https://user-images.githubusercontent.com/35698903/133014279-1baa9e07-892a-437a-85c2-f4205d2e7e5f.png)

<h3>Features</h3>

The notebook readily contains data visualization in form of printing the pandas DataFrame head, printing column names and multiple plots on features selected such as time_of_day, day_of_week and traffic volumne counted between hours to name some.

A function read_raw_date is defined to read and clean the data.txt files from a specified path and export it as a pandas DataFrame.

Insights drawn from each analysis is presented after each code-block. For example:
![image](https://user-images.githubusercontent.com/35698903/133014706-c9988423-9688-48c1-bad0-d34feeedce50.png)

The variables used have meaningful names and local varibles in code-blocks are deleted after use. Code-cells have comments that describe the logic and working of code where necessary.
