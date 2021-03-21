# CWM Cohort 1 Python Hello Word
# RJ Carrier
# 2021
# adaptation of https://www.geeksforgeeks.org/working-csv-files-python/
# Learning Goals: Get used to using a debugger. Learn to search for answers. Exposure to csv file IO (input/Output). 
import csv 



# TODO 1: What is this line? (line 7)
def main():
    # TODO 2: Google how main() works in python files
    # TODO 4: update this filename variable below

    filename = "data/UpdateFileNameHere.csv"
    print(fileName)
    # TODO 5: run this code. There should be an error. Let's debug! (google run python code in vscode or find here under "Run Hello World": https://code.visualstudio.com/docs/python/python-tutorial)
    # TODO 6: if you haven't already... go look at your data! Under the data file you'll see a csv file. Always good to know your data :)
    readFileFromCsv(filename)

    

def readFileFromCsv(filename):
    # initializing rows list
    rows = [] 
    
    # reading csv file 
    with open(filename, 'r') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
        
        # extracting field names through first row 
        fields = next(csvreader) 
    
        # extracting each data row one by one 
        for row in csvreader: 
            # TODO 6: "append" each row in this loop to our "rows" list
            rows.append(row) 
    
    #  printing first 5 rows 
    print('\nFirst 5 rows are:\n') 
    for row in rows[:5]: 
        # parsing each column of a row 
        for col in row: 
            print("%10s"%col), 
        print('\n') 

    # TODO extra: If you're feeling fancy, following the link on line 4 and try to add in the pieces that allow you to print the field names in the csv file



if __name__ == "__main__":
    main()