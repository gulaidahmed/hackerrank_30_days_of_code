#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N % 2 > 0:
        print('Weird')
    elif N <= 5:
        print('Not Weird')
    elif N < 21:
        print('Weird')
    else:
        print('Not Weird')
