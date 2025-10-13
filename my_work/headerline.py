import csv

FILENAME= "data.csv"
DATADIR = r'C:\Users\fmtie\OneDrive\Desktop\programming_for_da\PFDA-courseware\code\data\\'

#with open (DATADIR + FILENAME, "rt") as fp: 
#    reader = csv.reader(fp, delimiter=",")
 #   linecount = 0 # here you set the linecount variable to 0
  #  for line in reader: # then you loop through each line in the file
   #     if linecount != 0: # the first time the loop runs, linecount is 0, so it skips the print statement
    #        print (line)
     #   linecount += 1 # however, you add one to linecount at the end of each loop
                        # so the next time the loop runs, linecount is 1, and it prints the line

# this way the header line is ignored
# below you are moving on to calculating the average age

with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if linecount != 0:
            total += int(reader[1])
    linecount += 1

#average_age = total / (linecount - 1) # calculate the average age, subtracting 1 from linecount to account for the header line
#print (f"The average age is {average_age}")    

print(linecount)
print(total)