file = open("../expenseReport.txt", "r")
expenses = []
for x in file:
    expenses.append(x[:-1])
print(expenses)
for x in expenses:
    for y in expenses:
        if (int(x) + int(y) == 2020):
            print(int(x) * int(y))
            break
