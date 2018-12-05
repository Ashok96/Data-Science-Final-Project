"""
Filename: README.md
Authors: Kymberlee Hill, Swarnim Bhandari
"""

CSCI 473 Applied Data Science
Instructor: Gedare Bloom
Final Project (200 points)

# Part 1 (40 points): Using an API
We’ll use data obtained from the National Agricultural Statistics Service API. First, request an API key via https://quickstats.nass.usda.gov/api

API Documentation is located on the same page under “Usage”

Create an API request to return data for all TURKEYS described as "TURKEYS, YOUNG, SLAUGHTER, FI - SLAUGHTERED, MEASURED IN HEAD" in Virginia for each month for each year available 1989 - 2018. Save this data in a format that you can reuse.

Include the API command you used in your project report

# Part 2 (40 points): Describing and Visualizing Data
(a) Create a line plot of the Value for each month of your data set from 1989-2002 and
2009-2018. Include the plot in your report. Note: There is a gap in your data between
2002 and 2009.
(b) Report any Structure you find, and any hypotheses you have about that structure.
(c) Report mean and median of the Value grouped by year

# Part 3 (40 points): Fitting Data
(a) For just the data from 2017, fit a linear regression to your data for the months January
– October
(b) Using your linear fit, predict the value of turkeys as described for November
(c) Compute the absolute error between your predicted value and the actual value of
turkeys slaughtered in Virginia in Nov 2017
(d) Compute the coefficient of determination, or R^2 value, to determine how well your
model fits your data.
(e) Plot a line plot of Values from 2017 along with the linear fit.
Report on (a)-(e).
