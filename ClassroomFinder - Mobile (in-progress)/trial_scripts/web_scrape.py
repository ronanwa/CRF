##  Ronan Wallace
##  web_scrape.py
##  07/19/19

import random
import requests
import time
from bs4 import BeautifulSoup


def main():
       url = "https://www.macalester.edu/registrar/schedules/2019fall/class-schedule/"
       response = requests.get(url)
       print("Step 1")

       soup = BeautifulSoup(response.text, "html.parser")
       print("Step 2")

       data = str(soup.findAll("td"))
       print("Step 3")

       writeFile(data)
       removeSpaces()
       schedule = buildSchedule()
       print(schedule)
       ## SCHEDULE BUILT & STORED- Now what? ##
       ## Translate into Java? Java Web Scrape? ##

       testSchedule(schedule)

# Creates file with all class information
def writeFile(data):
       file = open("raw_class_data.txt", mode="w")
       string = ""
       delete = False
       spaceCount = 0
       checkComma = False

       for character in data:
              if character == '[':
                     continue
              elif character == '<':
                     spaceCount = 0
                     delete = True
                     continue
              elif delete == True:
                     if character == '>':
                            checkComma = True
                            spaceCount = 0
                            delete = False
                            continue
                     else:
                            continue
              elif character != ',':
                     checkComma = False
                     if character == ' ':
                            spaceCount += 1
                            if spaceCount > 1:
                                   continue
                            else:
                                   string += str(character)
                                   continue
                     else:
                            spaceCount = 0
                            string += str(character)
              else:
                     if checkComma == True:
                            string.rstrip().lstrip()
                            file.write(string + "\n")
                            string = ""
                            checkComma = False
                     else:
                            string += str(character)
       print("Step 4")
       file.close()
       return file

# Deletes all Empty Lines
def removeSpaces():
       file = open("raw_class_data.txt", mode = 'r')
       cleanFile = open("clean_class_data.txt", mode = "w")
       for line in file:
              if line == ' \n':
                     continue
              elif line == '\n':
                     continue
              elif "Avail./Max.:" in line:
                     continue
              elif "*" in line:
                     continue
              elif " Details" in line:
                     cleanFile.write("-\n")
                     continue
              else:
                     cleanFile.write(line)
                     continue
       print("Step 6")
       return 0

# Stores Class Information in Schedule Array
def buildSchedule():
       file = open("clean_class_data.txt", mode="r")
       count = 0
       schedule = []
       classInfo = []

       for line in file:
              if count == 0:
                     classInfo.append(cleanLine(line, count))
                     count += 1
              elif count == 1:
                     classInfo.append(cleanLine(line, count))
                     count += 1
              elif count == 2:
                     classInfo.append(cleanLine(line, count))
                     count += 1
              elif count == 3:
                     classInfo.append(cleanLine(line, count))
                     count += 1
              elif count == 4:
                     classInfo.append(cleanLine(line, count))
                     count += 1
              elif count == 5:
                     classInfo.append(cleanLine(line, count))
                     count += 1
              elif count == 6:
                     count = 0
                     schedule.append(classInfo)
                     classInfo = []
                     continue
              else:
                     count += 1
                     continue

       print("Step 7")
       return schedule

# Cleans Class Info Before Schedule Injection
def cleanLine(line, count):
       final = ""
       if count == 0 or count == 1:
              for i in range(len(line) - 1):
                     final += line[i]
       elif count == 2:
              for i in range(len(line)-6):
                     final+=line[i + 5]
       elif count == 3:
              for i in range(len(line)-6):
                     final+=line[i + 5]
       elif count == 4:
              for i in range(len(line)-6):
                     final+=line[i + 5]
       elif count == 5:
              for i in range(len(line)-12):
                     final+=line[i + 11]
       return final.lstrip().rstrip()


# Tests Schedule Formatting Using Random Sampling
def testSchedule(schedule):
       for i in range(10):
              time.sleep(2)
              print(schedule[random.randint(0,769)])
       print("Step 8")

main()
