import csv
import time
from random import randint
while True:
    with open('test.csv', 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow([time.time(), randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1)])
    time.sleep(5)
