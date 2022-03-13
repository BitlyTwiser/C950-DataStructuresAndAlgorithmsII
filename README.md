# C950-DataStructuresAndAlgorithmsII
 - C950 Package Delivery System

## Overview:
- The objective is to sucessfully deliver 40 packages in under 140 miles.
- This application is setup as a basic CLI application using argparse. 
- All time values are expected to be in miliary time in HH:MM format.
## General Usage:
- To view the commands on can utilize the following:
```python3 main.py -h```
- This command displays the help menu for interacting with the application.


## List all packages:
- One can display ALL packages by using the ```python3 main.py -a``` command

## See specific package details at specific time:
- One can view a specific package, at a specific time using the commands ```-p``` and ```-t```
- For package ID and timestamp. 
- Example: ```python3 main.py -p 1 -t "08:00"```
-

## List all packages at a given time:
- We can view where all the packages are within a given time range using the the flags ```-tr``` for time range.
- Time is expected to be in format: ```HH:MM-HH:MM```
- ```python3 main.py -tr "09:00-10:00"```