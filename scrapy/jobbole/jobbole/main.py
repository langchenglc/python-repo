# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
import sys
import os

current_file = os.path.abspath(__file__)
current_path = os.path.dirname(current_file)

print("current_file:",current_file)
sys.path.append(current_path)
execute(["scrapy","crawl","jobbole"])
