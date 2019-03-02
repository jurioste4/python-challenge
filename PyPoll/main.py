import os
import csv

rawdata=os.path.join('election_data.csv')

candidates = []
total_candidates=[]
candidates_perc = []
candidates_total = []
#summaries = ([] for i in range(5))

with open(rawdata, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    #sortedlist = sorted(data, key=operator.itemgetter(0))
   
    header = next(csvreader)
    num_rows = 0
    
    for row in csvreader : 
        total_candidates.append(row[2])
        num_rows += 1
       
       # data = (('khan','Li'),('Correy', "O'Tooley"))
    #unique_items = set(data)
   # keys = [[entry[0]for entrys in unique_items]]
    #for key in set(keys):



 #print("Candidate '{}' total {} votes". format(key, key.count(key)))
print("Total Votes:", num_rows)






#test = os.path.join("pybanktest.txt")

#with open(test, 'w' , newline= '') as csvfile:

    #csvwriter = csv.writer(csvfile, delimiter=',')

    #csvwriter.writerow(["total Months:",totalmonths])
    #csvwriter.writerow(["Profit total:",profit_loss])
    