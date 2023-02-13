'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open("employee_data.csv", "r")
reader = csv.reader(infile)


#create an empty dictionary and list
employee_dict = {}
employee_list = []

#use a loop to iterate through the csv file and append to list
for row in reader:
    employee_list.append(row)

#loop through list to add specific keys and values to dictionary
for i in range(0, len(employee_list)):
    #check if the employee fits the search criteria
    if employee_list[i][3] == "Marketing" and employee_list[i][4] == "CSR":
        employee_dict[f"{employee_list[i][1] + ' ' + employee_list[i][2]}"] = employee_list[i][5]

#prints out the dictionary before salary increase
print()    

for k, v in employee_dict.items():
    print(f"Manager Name: {k} Current Salary: ${round(float(v), 2):,}")

print()
print('=========================================')
print()

#prints out the dictionary post salary increase
for k, v in employee_dict.items():
    print(f"Manager Name: {k} Current Salary: ${round(float(v) * 1.10, 2):,}")

print()

#close file
infile.close()

          
        

        
    
