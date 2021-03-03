class cal():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
obj = cal(a, b)
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Subs")
    print("3. Mul")
    print("4. Div")
    choice = int(input("Entr choice: "))
    if choice == 1:
        print("Rslt: ", obj.add())
    elif choice == 2:
        print("Rslt: ", obj.sub())
    elif choice == 3:
        print("Rslt: ", obj.mul())
    elif choice == 4:
        print("Rslt: ", round(obj.div(), 2))
    elif choice == 0:
        print("no operation")
    else:
        print("Invalid choice")

#print()