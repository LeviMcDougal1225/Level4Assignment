
# Create a list to store expenses

lstExpenses = []    

# Collect and validate expense input 

while True:    

    flExpense = float(input("Enter an expense or 0 to finish: "))

    if flExpense == 0:
        break

    if flExpense < 0:
        print("Expense cannot be negative.")
        continue

    lstExpenses.append(flExpense)

# Count expenses by category 

small = 0 

moderate = 0

large = 0 

for flExpense in lstExpenses: 

    if flExpense < 25:
        small += 1

    elif flExpense <= 100:
        moderate += 1

    else:
        large += 1

# Calculate and display the expense summary

iTotalExpenses = len(lstExpenses)

fTotalNum = sum(lstExpenses)

if len(lstExpenses) > 0:

    fAverage = sum(lstExpenses) / len(lstExpenses)

    fSmallExp = min(lstExpenses)

    fLargeExp = max(lstExpenses)

    print("Number of expenses: " + str(iTotalExpenses))

    print(f"Total: ${fTotalNum:,.2f}")
    
    print(f"Average: ${fAverage:,.2f}")

    print(f"Smallest Expense: ${fSmallExp:,.2f}")

    print(f"Largest expense: ${fLargeExp:,.2f}")

    print("Small expenses: " + str(small))

    print("Moderate expenses: " + str(moderate))
    
    print("Large expenses: " + str(large))

else:
    print("No expenses were entered.")




























