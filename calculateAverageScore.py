# loop through the files in this directory looking for the string Accepted

import os
import re
import datetime

# get the current directory
current_dir = os.getcwd()

# get the list of files in the current directory
files = os.listdir(current_dir)

avgMs = []
avgRuntime = []
avgMemory = []

# loop through the files in the current directory
for file in files:
    # if the file is a python file
    if file.endswith(".py"):
        # open the file
        with open(file, "r") as f:
            # read the file
            lines = f.readlines()
            # loop through the lines in the file
            for line in lines:
                # if the line contains the string Accepted
                if "cases passed" in line:
                    # get the number of cases passed, in between the string "cases passed (" and " ms)"
                    ms_match = re.search(r"cases passed \((\d+) ms\)", line)
                    avgMs.append(int(ms_match.group(1))) if ms_match else None
                elif "runtime beats" in line:
                    # get the runtime, in between the string "runtime beats " and " %"
                    runtime_match = re.search(r"runtime beats (\d+\.\d+)", line)
                    avgRuntime.append(float(runtime_match.group(1))) if runtime_match else None
                elif "memory usage beats" in line:
                    # get the memory usage, in between the string "memory usage beats " and " %"
                    memory_match = re.search(r"memory usage beats (\d+\.\d+)", line)
                    avgMemory.append(float(memory_match.group(1))) if memory_match else None

# calculate the average ms
avgMs = sum(avgMs) / len(avgMs)
# calculate the average runtime
avgRuntime = sum(avgRuntime) / len(avgRuntime)
# calculate the average memory usage
avgMemory = sum(avgMemory) / len(avgMemory)

# print the average ms
print("Average ms per problem: " + str(int(avgMs)) + " ms")
# print the average runtime
print("Runtime average better than: " + str(round(avgRuntime, 2)) + "%")
# print the average memory usage
print("Memory average better than: " + str(round(avgMemory, 2)) + "%")
print()

print("On average, you are better than " + str(round((avgRuntime+avgMemory)/2, 2)) + "%" + " of all users.")

# Write this information to this file
with open("README.md", "w") as f:
    f.write("# LeetCode\n\n")
    f.write("## Average Stats\n\n")
    f.write("Average ms per problem: " + str(int(avgMs)) + " ms\n\n")
    f.write("Runtime average better than: " + str(round(avgRuntime, 2)) + "%\n\n")
    f.write("Memory average better than: " + str(round(avgMemory, 2)) + "%\n\n")
    f.write("On average, Jensen is better than " + str(round((avgRuntime+avgMemory)/2, 2)) + "%" + " of all users.\n\n")
    #Write the date as month/day/year
    f.write("Last updated: " + datetime.datetime.now().strftime("%m/%d/%Y"))
    #This code was written automatically by a python script.  If you want to update the stats, run the script again.
    f.write("\n\nThis code was written automatically by a python script.  If you want to update the stats, run calculateAverageScore.py again.")
