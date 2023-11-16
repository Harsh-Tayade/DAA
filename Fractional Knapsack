# fractional knapsack

#calculates profit/weight ratio for sorting Object array
def calculate_ratio(item):
    return item[1] / item[2]
    
n=int(input("Enter total number of items: "))
cap=int(input("Enter total capacity of the knapsack: "))
pw=[]
knapsack=[]
obj=[[]for _ in range(3)]
net_val=0

#initially remaining weight will be the same as the total capacity
rem_wt=cap 

#building object array having info about each object
for i in range(n):
    for j in range(3):
        if(j==0):
            obj[i].append(input("\nObject Name: "))
        elif(j==1):
            obj[i].append(float(input("Object Value: ")))
        elif(j==2):
            obj[i].append(float(input("Object Weight: ")))
            pw.append(calculate_ratio(obj[i]))

#Sort Object list as per their Profit/Weight ratio
obj.sort(key=calculate_ratio, reverse=True)

for i in range(n):
    if(rem_wt<obj[i][2]):
        obj[i][1]=pw[i]*rem_wt
        obj[i][2]=rem_wt
        rem_wt=rem_wt-obj[i][2]
        net_val+=obj[i][1]
        knapsack.append(obj[i])
        
    elif(rem_wt>=obj[i][2]):
        rem_wt=rem_wt-obj[i][2]
        net_val+=obj[i][1]
        knapsack.append(obj[i])

#Printing the knapsack inventory
print("------KNAPSACK------\n")
print("Name\tValue\tWeight\n")
for i in range(n):
    print(knapsack[i][0],"\t", knapsack[i][1],"\t", knapsack[i][2])

print("\nTotal Profit = ",net_val)
