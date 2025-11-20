expenses=[]
def add_expense():
    amount=int(input("Amount: "))
    category=input("Category: ")
    note=input("Note: ")
    expenses.append({"amount":amount,"category":category,"note":note})
    print("Expense added!")
def view_expenses():
    if not expenses:
        print("No expenses yet.")
        return
    print("All Expenses")
    for i,exp in enumerate(expenses,1):
         print(i,"₹", exp["amount"],"|amount:",str(exp["amount"]),"|",exp["category"],"|",exp["note"])
def total_spent():
    total=sum(exp["amount"] for exp in expenses)
    print("Total spent:",total)
while True:
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Total Spent")
    print("4.Exit")
    c=input("Enter choice:")
    if c=="1":
        add_expense()
    elif c=="2":
        view_expenses()
    elif c=="3":
        total_spent()
    elif c=="4":
        print("Bye!")
        break
    else:
        print("Invalid choice")

