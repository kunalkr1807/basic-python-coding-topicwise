

# reading csv file using loop
import csv
 
# opening the CSV file, mention the path to select a file
with open('D:\\documents\\iris.csv', mode ='r')as file:
   
    # reading the CSV file
    csvFile = csv.reader(file)

    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)
















