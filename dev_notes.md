# Development Notes

## June 30

Completed:

- Created folder structure
- Installed VS Code
- Created GitHub repository

Learned:

- Difference between Jupyter and VS Code
- What a README is
- Why we separate code into modules

Questions:

- How should the loader validate CSV files?
- What's the best way to structure the analytics module?

Next Sprint:

- Build the CSV loader
#


## July 3

Completed: 

- Installed the different python tools i'd need for the project ((numpy, pandas, etc..))


Learned:

- Why we create environments with .venv
- dependancy management with pip
- how to send which package versions we'd need for a project using requirments.txt
- The subpackages that are in included in installed packages are what make the main ones run efficiently.


Next Sprint:
- Make initial Git Commit
- Create data/raw/sample_sales.csv
- add docs/ folder with empty markdown files



## July 7

Completed: 

- created a loader function that takes in a csv file, tests to see if there are any problems, and is usable for other projects

Learned:

- how to creat a loader function
- how to use Path and import pathlib
- use .exists(), .infile(), and .suffix (suffixes) to check for problems with loading a csv file
- understand what try and except commands do to run a test and do something if it doesn work (and the difference between try and if statements)
- creating different files for different tasks i.e. the loader.py folder is just to test and load a csv file that we can import into other files and projects.

Continue:
- run tests to see if the csv file will load if it has data and review the error messages and discover what__init__.py actually does for a file

## July 11
Completed:
- Finished the loader program and function in test_loader and loader files. Created tests to ensure the loader is loading a correct and working file into the program. 

Learned:
-  A reusable module
- Type hints
- Docstrings
- Path validation
- Exception handling
- Custom exceptions
- Manual testing
- Automated tests
- Read and interpreted a real pytest failure report
- purpose of keeping files together in a function rather than universal and at the top
- how (python -m) works in the terminal and how its another way of running your code rather than using the run button.
- why its good to have several smaller projects in an overall project rather than just doing one giant thing -- easier to fix one section of code than search through a big thing to find the problem

Continue:
- start Sprint 2 which is used to clean data from a csv file and Build a reusable data cleaning module that transforms messy CSV data into a consistent, analysis-ready DataFrame.