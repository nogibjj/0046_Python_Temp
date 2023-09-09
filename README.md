[![Python_Temp_Demo](https://github.com/nogibjj/oo46_Python_Temp/actions/workflows/actions.yml/badge.svg)][def]

## Template for Python projects

The current implementation of the Mini-project can be executed as follows:

1. All dependencies needed for execution can be found in the requirement.txt file
2. These dependencies will be installed  by github actions(please see yml file for further details)for now.
3. Please refer the requirements.txt for manual intallations. 

Mini-project deliverables:
1. The myapp/main.py file can be thought of as the main app entry in the current implementation
2. It imports pandas and reads a csv file from the dsets folder and performs the following:
    - displays a descriptive analysis of the input file by calling my_stats() with the input file as arguement
    - applys mpg_cat() function on mpg col of the input file and the result is added into a new col named Fuel Efficiency
    - It then displays some selected records from the updated dataframe

Testing...
1. A simple unit test implementation is provided in myapp/test_main.py as follows:
    - test_col_exist function --> test if a new column exist after calling mpg_cat function on a dataframe
    - test_my_stats --> uses pandas's assert_frame_equal testing feature to confirm the quality of two dataframes
2. This test wll also be executed by github actions


[def]: https://github.com/nogibjj/oo46_Python_Temp/actions/workflows/actions.yml
