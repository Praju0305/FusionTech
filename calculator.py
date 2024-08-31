def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"


def main():
    print("Welcome to the Basic Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()

'''
import tkinter as tk

class Calculator:
    def _init_(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        # Create the display
        self.display = tk.Entry(root, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
        self.display.grid(row=0, column=0, columnspan=4)
        
        # Define buttons and their layout
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        for button in self.buttons:
            tk.Button(root, text=button, font=('Arial', 18), command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Initialize variables
        self.current_expression = ""
        self.result = None

    def on_button_click(self, button_text):
        if button_text in '0123456789.':
            self.current_expression += button_text
            self.update_display()
        elif button_text in '+-*/':
            if self.current_expression:
                self.current_expression += button_text
                self.update_display()
        elif button_text == '=':
            try:
                self.result = eval(self.current_expression)
                self.current_expression = str(self.result)
            except Exception as e:
                self.current_expression = "Error"
            self.update_display()
        else:
            self.current_expression = ""
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_expression)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "_main_":
    main()

'''

def calculator():
    """A simple command-line calculator."""

    while True:
        print("Enter an expression (e.g., 2+3, 5-1, 4*2, 6/3):")
        expression = input()

        try:
            result = eval(expression)
            print("Result:", result)
        except (SyntaxError, NameError, ZeroDivisionError) as e:
            print("Error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)

        if input("Do you want to continue? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    calculator()