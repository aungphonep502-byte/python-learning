'''# custom exception
class NegativeNumberError(Exception):
    pass
def check_number():
    number = float(input("Type a number"))
    if number < 0:
        raise NegativeNumberError(
            "Error: Number must not be negative"
        )
    return 10 / number
try:
    new_number = check_number()
    print("Result",new_number)
except ValueError as e:
    print("Error",e)
except NegativeNumberError as e:
    print("Error",e)
except ZeroDivisionError as e:
    print("Error",e)

# part2
# Module?
import calculator 
print(calculator.add(1,2))

# import module
# math is built-in module, so i can use its functions
import math 
print(math.sqrt(2))
print(math.pi)

# from module import name
from math import sqrt
print(sqrt(20))
# import multiple things
from math import sqrt,pi
print(sqrt(25))
print(pi)

# import module as alias
import math as m 
print(m.sqrt(25))
print(m. pi)

# from module import *
from math import * 
print(sqrt(49))
print(pi)

# Built-in Module: math
import math
print(math.sqrt(64))
print(math.ceil(4.3))
print(math.floor(3.1))
print(math.pow(2,8))
print(math.pi)

# Built-in Module: random
import random
print(random.randint(1,20))
# Random choice:
import random 
fruits = ["apple","strawberry","grape"]
print(random.choice(fruits))

# Built-in Module: DateTime
import datetime
now = datetime.datetime.now()
print(now)

# Buit-in Module: os
# getcwd = Get Current Working Directory
import os 
print(os.getcwd())
# listdir = List Directory 
# os.listdir() = List files in a folder
import os 
print(os.listdir())

# sys.version → Python version
import sys
print(sys.version)
# Command-line arguments
import sys
print(sys.argv)

# dir()
# shows everythins inside a module
import math 
print(dir(math))

# help()
# show documentation
import math 
help(math.sqrt) 

import random
help(random.randint) 

# Practice 1
import math 
number = 3
print(math.sqrt(number))
print(math.pow(number,3))

# Practice 2
import random 
for i in range(5):
    print(random.randint(1,10))

# Practice 3
import datetime
today = datetime.datetime.today()
print("Today",today)

# Practice 4
import os 
print("Current Folder")
print(os.getcwd())

print("Files")
print(os.listdir())

# Mini challenge
import random 
guess= int(input("Guess a nnumber"))
correct = random.randint(1,10)
if guess == correct:
    print("Correct")
else:
    print("Wrong")
    print("Correct anser is",correct)

# On terminal, i wrote / pip install requests 
import requests
response = requests.get("http://google.com")
print(response.status_code)'''

# pip list
# Shows all installed packages.
# useage 
# Check what tools are installed
# Debug problems
# Share project with others

# pip freeze
# pip freeze
#     ↓
# requirements.txt file
#     ↓
# Send project to others
#     ↓
# They run:
# pip install -r requirements.txt
#     ↓
# Same packages installed

# Save dependencies
# if i want to save as file -->

# ===============================
# pip freeze > requirements.txt
# ===============================
# ===========================================================================


# Virtual Environment
#================ Without virtual environments:============

# Computer Python
# └── requests

# ==============With virtual environments:================

# WeatherApp
# └── venv
#     └── requests 2.0

# AIChatbot
# └── venv
#     └── requests 3.0
# ===========================================================================

# 1.  create a virtual enviroment
# Inside your project folder:
# ==================python -m venv venv======================
# Python creates:
# project/
#     venv/

# 2.  Activate Virtual Enviroment
# Window --> ====================Set-ExecutionPolicy RemoteSigned -Scope CurrentUser=============

# =======Type==========
# =======.\venv\Scripts\Activate.ps1=============

# =========appear like this mean I am in Virtual Enviroment=========
# (venv) PS C:\Users\ASUS\Music\python-day1>
# =========================================================================================

# 3. Install packages inside the venv
# in bash --> pip install requests

# 4. Deactivate 
# when finished i must use iter
# =======deactivate=========

'''# Use module
import helper
helper.greet("APP")

result = helper.add(3,4)
print("Result",result)

# import specific functions
from helper import greet
greet("Aung")

# import as Alias
import helper as hp
result = hp.add(1,2)
print(result)

# __name__
import test
print(test.square(4))

import calculator

from datetime import datetime
now = datetime.now()

# strftime is string format time
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%H:%M:%S"))

# Time Delta, Delta means difference
from datetime import datetime,timedelta
now = datetime.now()
future = now + timedelta(minutes=50)
print(future)

from datetime import datetime,timedelta
now = datetime.now()
future = now + timedelta(days = 5)
print(future)

from datetime import datetime, timedelta
now = datetime.now()
future = now + timedelta(hours = 5)
print(future)

# os module
import os
print(os.getcwd())

# list files
import os 
print(os.listdir())

# check if file exists
import os 
print(os.path.exists("day11.py"))

import requests 
response = requests.get(
    "https://official-joke-api.appspot.com/random_joke"
)
data = response.json()
print("Setup")
print(data["setup"])

print("\nPunchline")
print(data["punchline"])

# to know website is html or json, 
# if html file cannot change into json from API
import requests
response = requests.get(
    "https://chatgpt.com/c/6a395d52-5eb4-83ec-82bd-01ace27b5043"
)
print(response.text)

# with exceptions
import requests
try:
    response = requests.get(
        "https://official-joke-api.appspot.com/random_joke"
    )
    data = response.json()
    print("Setup")
    print(data["setup"])
    print("\nPunchline")
    print(data["punchline"])
except requests.exceptions.RequestException:
    print("Could not connect API")'''

# Mini Challenge 
import random 
phones = ["Samsung","iPhone","Oppo"]

print("Random phone-->",random.choice(phones))

from datetime import datetime
now = datetime.now()
print(now.strftime("%H:%M:%S"))

from math import sqrt
square_root = sqrt(81)
print("Square root of 81:",square_root)
























    

    


















































    






    


