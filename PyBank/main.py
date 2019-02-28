import os
import csv

rawdata=os.path.join('budget_data.csv')

totalmonths = 0
profit_loss = 0
#totalmonths = int(x[0])
#profit_loss = int(x[1])

with open(rawdata, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

   
   #print(f"total months: {str(totalmonths)}")
    
    #print(f"profit winLoss: {str(profit_loss)}")
  
    for row in csvreader : 
        totalmonths += 1
        profit_loss += int(row[1])

print("total months:", totalmonths)
print("profit total:",profit_loss)
print("avearge total",profit_loss/totalmonths)
        

        




   
       







    #loop_increase = int(row[1])
    #increase = loop_increase - greatest_increase


 