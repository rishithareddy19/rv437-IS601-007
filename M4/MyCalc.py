class MyCalc:
    def __init__(self):
        self.ans = 0

    def add(self, a, b):
        #rv437 and 10/16/23 this is an add function
        if isinstance(a, str) and a == "ans":
            a = self.ans
        self.ans = a + b
        return self.ans

    def subtract(self, a, b):
        #rv437 and 10/16/23 this is a subtraction function
        if isinstance(a, str) and a == "ans":
            a = self.ans
        self.ans = a - b
        return self.ans

    def multiply(self, a, b):
        #rv437 and 10/16/23 this is a multiplication function
        if isinstance(a, str) and a == "ans":
            a = self.ans
        self.ans = a * b
        return self.ans

    def divide(self, a, b):
        #rv437 and 10/16/23 this is a division function
        if isinstance(a, str) and a == "ans":
            a = self.ans
        try:
            self.ans = a / b
            return self.ans
        except ZeroDivisionError:
            return "Cannot divide by zero."

# main logic
if __name__ == "__main__":
    calc = MyCalc()

    while True:
        user_input = input("Enter an expression (e.g., 2 * 3) or 'exit' to quit: ")

        if user_input.lower() == 'exit':
            break

        # Handle calculation based on user input
        try:
            if 'ans' in user_input:
                user_input = user_input.replace('ans', str(calc.ans))

            result = eval(user_input)
            calc.ans = result
            print("Result:", result)

        except (ZeroDivisionError, SyntaxError, NameError):
            print("Invalid input or operation. Please try again.")
