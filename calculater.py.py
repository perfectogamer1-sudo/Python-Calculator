import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Calculator")
        self.root.geometry("320x500")
        self.root.configure(bg="#2c3e50")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Display Screen
        input_frame = tk.Frame(self.root, width=312, height=50, bd=0, bg="#ecf0f1")
        input_frame.pack(side=tk.TOP, pady=10)
        
        input_field = tk.Entry(
            input_frame, 
            font=('arial', 28, 'bold'), 
            textvariable=self.input_text, 
            width=50, 
            bg="#ecf0f1", 
            bd=0, 
            justify='right',
            fg="#2c3e50"
        )
        input_field.grid(row=0, column=0, ipady=15)

        # Buttons Frame
        buttons_frame = tk.Frame(self.root, width=312, height=322.5, bg="#2c3e50")
        buttons_frame.pack(pady=10)

        # Button Layout: (Text, Row, Column, BG_Color)
        buttons = [
            ('C', 0, 0, '#e74c3c'), ('/', 0, 1, '#f39c12'), ('*', 0, 2, '#f39c12'), ('-', 0, 3, '#f39c12'),
            ('7', 1, 0, '#ecf0f1'), ('8', 1, 1, '#ecf0f1'), ('9', 1, 2, '#ecf0f1'), ('+', 1, 3, '#f39c12'),
            ('4', 2, 0, '#ecf0f1'), ('5', 2, 1, '#ecf0f1'), ('6', 2, 2, '#ecf0f1'), ('=', 2, 3, '#2ecc71'),
            ('1', 3, 0, '#ecf0f1'), ('2', 3, 1, '#ecf0f1'), ('3', 3, 2, '#ecf0f1'), ('.', 3, 3, '#ecf0f1'),
            ('0', 4, 0, '#ecf0f1'), ('00', 4, 1, '#ecf0f1'), ('DEL', 4, 2, '#e74c3c'), ('=', 4, 3, '#2ecc71'),
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            color = btn[3]

            tk.Button(
                buttons_frame, 
                text=text, 
                fg="black" if text not in ['C', '/', '*', '-', '+', '=', 'DEL'] else "white",
                width=7, 
                height=2, 
                bd=0, 
                bg=color,
                cursor="hand2",
                activebackground="#bdc3c7",
                font=('arial', 14, 'bold'),
                command=lambda t=text: self.btn_click(t)
            ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Configure grid weights
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

    def btn_click(self, item):
        """Handle button clicks."""
        if item == 'C':
            self.expression = ""
            self.input_text.set("")
        elif item == 'DEL':
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif item == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except ZeroDivisionError:
                self.input_text.set("Error")
                self.expression = ""
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        else:
            if self.expression == "Error":
                self.expression = ""
            self.expression += str(item)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()