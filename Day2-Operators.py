#!/bin/python3

import math
import os
import random
import re
import sys
meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
# Complete the solve function below.
tip = meal_cost * tip_percent / 100
tax = meal_cost * tax_percent / 100
total_cost = round(meal_cost + tip + tax)
print(total_cost)
