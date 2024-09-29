employeeName = str(input("Employee's Name: "))
numberOfShifts = float(input("Number of Shifts: "))
numberOfTransactions = float(input("Number of Transactions: "))
transactionDollarValue = float(input("Transaction Dollar Value: "))

productivityScore = int((transactionDollarValue / numberOfTransactions) / numberOfShifts)

employeeBonus = float()

if int(productivityScore) <= 30:
    employeeBonus = 50.00
elif int(productivityScore) (31 <= 69) :
    employeeBonus = 75.00
elif int(productivityScore) ( 70<= 199) :
    employeeBonus = 100.00
elif int(productivityScore) >= 200 :
    employeeBonus = 200.00

print("Employee Name: " + str(employeeName))
print("Employee Bonus: $" + str(employeeBonus))