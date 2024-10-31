import math
import tkinter as tk
from tkinter import messagebox

# Calculator Constants
CALCULATOR_NAME = "GX 999 SUPREME +"
CALCULATOR_VERSION = "v1.0"
CALCULATOR_BACKGROUND_COLOR = "black"
CALCULATOR_FOREGROUND_COLOR = "gray"
CALCULATOR_FONT = "Arial"
CALCULATOR_FONT_SIZE = 20
SCREEN_WIDTH = 420
SCREEN_HEIGHT = 630
CALCULATOR_PADDING = 5
CONSOLE_LOGGING = True

# Expression Box Constants
EXPRESSION_BOX_COLOR = "white"
EXPRESSION = ""
ANS = 0
EVALUATION_STRING = ""

# SHIFT & ALPHA CONSTANTS
SHIFT = False
ALPHA = False

# Button Constants
BUTTON_BACKGROUND_COLOR = "blue"
BUTTON_FOREGROUND_COLOR = "white"
TOP_BUTTON_BACKGROUND_COLOR_NORMAL = "cyan"
TOP_BUTTON_BACKGROUND_COLOR_SHIFT = "yellow"
TOP_BUTTON_BACKGROUND_COLOR_ALPHA = "pink"
TOP_BUTTON_FOREGROUND_COLOR = "black"
TOP_BUTTON_STATE = 0
BUTTON_FONT = "Arial"
BUTTON_FONT_SIZE = 16
BUTTON_HEIGHT = 1
BOTTOM_BUTTON_WIDTH = 4
TOP_BUTTON_WIDTH = 4
CONTROL_BUTTONS = ["ABOUT", "SHIFT", "ALPHA", "MODE", "SETTINGS", "EXIT"]
CONTROL_BUTTONS_BACKGROUND_COLOR = "white"

# Buttons List Constants
TOP_BUTTONS = [
    [["(-)", "±", ""], ["√x", "³√x", ""], ["X²", "X³", "BIN"], ["Xⁿ", "ⁿ√x", "OCT"], ["logₐn", "10ⁿ", "DEC"], ["ln", "eⁿ", "HEX"]],
    [["sinh", "1/sinh", ""], ["cosh", "1/cosh", ""], ["tanh", "1/tanh", ""], ["sin", "cosec", "1/sin"], ["cos", "sec", "1/cos"], ["tan", "cot", "1/tan"]],
    [["Const", "π", "e"], ["Conv", "RAD", "DEG"], ["%", "x!", ""], ["° ' \"", "nPr", "nCr"], ["(", "{", "["], [")", "}", "]"]]
]    
BOTTOM_BUTTONS = [
    ["7", "8", "9", "DEL", "AC"],
    ["4", "5", "6", "*", "/"],
    ["1", "2", "3", "+", "-"],
    [".", "0", "*10", "Ans", "="]
]
TOP_BUTTON_COMMON_PARAMETERS = {
    "font": (BUTTON_FONT, BUTTON_FONT_SIZE),
    "width": TOP_BUTTON_WIDTH,
    "height": BUTTON_HEIGHT,
    "bg": TOP_BUTTON_BACKGROUND_COLOR_NORMAL,
    "fg": TOP_BUTTON_FOREGROUND_COLOR,
    "bd": 0,
    "cursor": "hand2"
}

# Button Type Constants
CONSTANTS = []
CONVERSION = []
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
OPERATORS = ["+", "-", "*", "/", "%", "*10"]
BRACKETS = ["[", "{", "(", ")", "}", "]"]
RIGHT_BRACKET = ["sin", "cos", "tan", "cosec", "sec", "cot", "1/sin" ,"1/cos",
                "1/tan", "sinh", "cosh", "tanh", "1/sinh", "1/cosh", "1/tanh"]
POWER_LOGARITHM = ["X²", "X³", "Xⁿ", "10ⁿ", "√x", "³√x", "ⁿ√x", "logₐn", "ln", "eⁿ"]
CALCULATION_OPERATORS = ["Ans", "=", "DEL", "AC"]
MISCELLANEOUS = ["(-)", "±", "° ' \"", "π", "e", "x!", "RAD", "DEG", "nPr", "nCr"]
NUMBER_BASES = ["BIN", "OCT", "DEC", "HEX"]

# Calculator Class
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(CALCULATOR_NAME)
        self.window.resizable(0, 0)  # Disable window resizing
        self.window.configure(bg=CALCULATOR_BACKGROUND_COLOR, padx=CALCULATOR_PADDING, pady=CALCULATOR_PADDING)
        self.window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        if CONSOLE_LOGGING:
            print("Calculator Initialized Successfully!")
        self.create_gui()
    
    def create_gui(self):
        self.calculator_label()
        self.expression_box()
        self.control_buttons()
        self.top_buttons()
        self.bottom_buttons()
        if CONSOLE_LOGGING:
            print("Calculator GUI Created Successfully!")
    
    def calculator_label(self):
        self.name_label = tk.Label(self.window, text=CALCULATOR_NAME, font=(CALCULATOR_FONT, 20), bg=CALCULATOR_BACKGROUND_COLOR, fg="aqua")
        self.name_label.pack(side=tk.TOP, fill=tk.X, padx=CALCULATOR_PADDING, pady=CALCULATOR_PADDING)
    
    def expression_box(self):
        self.expression_field = tk.Entry(self.window, justify=tk.RIGHT, font=(CALCULATOR_FONT, CALCULATOR_FONT_SIZE), bg=CALCULATOR_FOREGROUND_COLOR, fg=EXPRESSION_BOX_COLOR)
        self.expression_field.pack(side=tk.TOP, fill=tk.X, ipady= 25, padx=CALCULATOR_PADDING, pady=CALCULATOR_PADDING)
    
    def control_buttons(self):
        global CONTROL_BUTTONS
        
        self.control_frame = tk.Frame(self.window, bg=CALCULATOR_BACKGROUND_COLOR)
        self.control_frame.pack(side=tk.TOP, fill=tk.X, padx=CALCULATOR_PADDING, pady=CALCULATOR_PADDING, ipady=2)
        
        for btn in CONTROL_BUTTONS:
            self.btn = tk.Button(self.control_frame, text=btn, font=(CALCULATOR_FONT, 8, "bold"), width=7, height=1, bg=CONTROL_BUTTONS_BACKGROUND_COLOR, fg="black", bd=0, cursor="hand2", command=lambda x=btn: self.control_button_click(x))
            self.btn.pack(side=tk.LEFT, fill=tk.X, padx=8, pady=7)
    
    def top_buttons(self):
        self.top_button = [["r1", "r1b1", "r1b2", "r1b3", "r1b4", "r1b5", "r1b6"],
                           ["r2", "r2b1", "r2b2", "r2b3", "r2b4", "r2b5", "r2b6"],
                           ["r3", "r3b1", "r3b2", "r3b3", "r3b4", "r3b5", "r3b6"]]
        
        for i in range(3):
            self.top_button[i][0] = tk.Frame(self.window, bg=CALCULATOR_BACKGROUND_COLOR)
            self.top_button[i][0].pack(side=tk.TOP, fill=tk.X, padx=CALCULATOR_PADDING, pady=(CALCULATOR_PADDING/3))
            for j in range(6):
                self.top_button[i][j+1] = tk.Button(self.top_button[i][0], text=TOP_BUTTONS[i][j][0], **TOP_BUTTON_COMMON_PARAMETERS, command=lambda x=TOP_BUTTONS[i][j]: self.top_button_click(x))
                self.top_button[i][j+1].pack(side=tk.LEFT, fill=tk.X, padx=CALCULATOR_PADDING+2, pady=CALCULATOR_PADDING)
    
    def bottom_buttons(self):
        global BOTTOM_BUTTONS
        
        for row in BOTTOM_BUTTONS:
            self.row = tk.Frame(self.window, bg=CALCULATOR_BACKGROUND_COLOR)
            self.row.pack(side=tk.TOP, fill=tk.X, padx=CALCULATOR_PADDING, pady=(CALCULATOR_PADDING/3))
            
            for btn in row:
                self.btn = tk.Button(self.row, text=btn, font=(CALCULATOR_FONT, CALCULATOR_FONT_SIZE), width=BOTTOM_BUTTON_WIDTH, height=BUTTON_HEIGHT, bg=f"{'blue' if btn in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] else 'red' if btn in ['+', '-', '*', '/', '.', '*10'] else 'green'}", fg="white", bd=0, cursor="hand2", command=lambda x=btn: self.bottom_button_click(x))
                self.btn.pack(side=tk.LEFT, fill=tk.X, padx=CALCULATOR_PADDING, pady=CALCULATOR_PADDING)
    
    def control_button_click(self, btn):
        if btn == "ABOUT":
            messagebox.showinfo("ABOUT INFO", f"{CALCULATOR_NAME}\n\nDeveloped by: UHN406\n\nVersion: {CALCULATOR_VERSION}\n\nCopyrights Reserved.")
        
        elif btn == "EXIT":
            check = messagebox.askquestion("EXIT", "Do you want to exit?")
            if check == "yes":
                self.window.destroy()
        
        elif btn == "MODE":
            messagebox.showinfo("Coming Soon!", "Developer is working day-night to add new features.\n\nSTAY TUNED FOR UPDATES!")
        
        elif btn == "SETTINGS":
            messagebox.showinfo("Coming Soon!", "Developer is working day-night to add new features.\n\nSTAY TUNED FOR UPDATES!")
        
        elif btn == "SHIFT":
            global SHIFT
            if SHIFT:
                SHIFT = False
                self.shift()
            else:
                SHIFT = True
                self.shift()
        
        elif btn == "ALPHA":
            global ALPHA
            
            if ALPHA:
                ALPHA = False
                self.alpha()
            else:
                ALPHA = True
                self.alpha()
        
        if CONSOLE_LOGGING:
            print("Control Button Clicked: ",btn)
    
    def set_top_buttons(self, mode):
        global TOP_BUTTONS
        if mode == "normal":
            X=0
            bgcolor = TOP_BUTTON_BACKGROUND_COLOR_NORMAL
        elif mode == "shift":
            X=1
            bgcolor = TOP_BUTTON_BACKGROUND_COLOR_SHIFT
        elif mode == "alpha":
            X=2
            bgcolor = TOP_BUTTON_BACKGROUND_COLOR_ALPHA
        
        for i in range(3):
            for j in range(6):
                self.top_button[i][j+1].config(text=TOP_BUTTONS[i][j][X], bg=bgcolor)
        
    def shift(self):
        global ALPHA
        ALPHA = False
        global SHIFT
        if SHIFT:
            self.set_top_buttons("shift")
        else:
            self.set_top_buttons("normal")
            
    
    def alpha(self):
        global SHIFT
        SHIFT = False
        global ALPHA
        if ALPHA:
            self.set_top_buttons("alpha")
        else:
            self.set_top_buttons("normal")
    
    def top_button_click(self, btn):
        global TOP_BUTTON_STATE
        if (ALPHA == False) and (SHIFT == False):
            TOP_BUTTON_STATE = 0
        elif (SHIFT == True) and (ALPHA == False):
            TOP_BUTTON_STATE = 1
        elif (ALPHA == True) and (SHIFT == False):
            TOP_BUTTON_STATE = 2
        
        global TOP_BUTTONS
        self.button_clicked(btn[TOP_BUTTON_STATE])
    
    def bottom_button_click(self, btn):
        self.button_clicked(btn)
    
    def button_clicked(self, btn):
        global EXPRESSION
        
        # NUMBERS
        if btn in NUMBERS:
            if (EXPRESSION != ""):
                if (EXPRESSION[-1] in [")", "}", "]"]):
                    EXPRESSION += "*"
                    self.expression_field.insert(tk.END, "*")
            EXPRESSION += btn
            self.expression_field.insert(tk.END, btn)
        
        # OPERATORS
        elif btn in OPERATORS:
            if EXPRESSION[-1] not in OPERATORS:
                EXPRESSION += btn
                self.expression_field.insert(tk.END, btn)
        
        # BRACKETS
        elif btn in BRACKETS:
            if (EXPRESSION != ""):
                if ((EXPRESSION[-1] not in NUMBERS) and (EXPRESSION[-1] not in BRACKETS) and (EXPRESSION[-1] not in OPERATORS)):
                    EXPRESSION += "*"
                    self.expression_field.insert(tk.END, "*")
            EXPRESSION += btn
            self.expression_field.insert(tk.END, btn)
        
        # RIGHT_BRACKET
        elif btn in RIGHT_BRACKET:
            if (EXPRESSION != ""):
                if (EXPRESSION[-1] not in OPERATORS):
                    EXPRESSION += "*"
                    self.expression_field.insert(tk.END, "*")            
            to_add = btn + "("
            EXPRESSION += to_add
            self.expression_field.insert(tk.END, to_add)
        
        # Power & Logarithm
        elif btn in POWER_LOGARITHM:
            if btn == "X²":
                EXPRESSION += "**2"
                self.expression_field.insert(tk.END, "**2")
            
            if btn == "X³":
                EXPRESSION += "**3"
                self.expression_field.insert(tk.END, "**3")
            
            if btn == "Xⁿ":
                EXPRESSION += "**"
                self.expression_field.insert(tk.END, "**")
            
            if btn == "10ⁿ":
                EXPRESSION += "10**"
                self.expression_field.insert(tk.END, "10**")
            
            if btn == "eⁿ":
                EXPRESSION += "2.718**"
                self.expression_field.insert(tk.END, "e**")
            
            if btn == "√x":
                EXPRESSION += "²√("
                self.expression_field.insert(tk.END, "²√(")
            
            if btn == "³√x":
                EXPRESSION += "³√("
                self.expression_field.insert(tk.END, "³√(")
            
            if btn == "ⁿ√x":
                EXPRESSION += "ⁿ√("
                self.expression_field.insert(tk.END, "ⁿ√(")
            
            if btn == "logₐn":
                EXPRESSION += "log("
                self.expression_field.insert(tk.END, "log(")
            
            if btn == "ln":
                EXPRESSION += "ln("
                self.expression_field.insert(tk.END, "ln(")
        
        # Calculation Operations
        elif btn in CALCULATION_OPERATORS:
            
            if btn == "=":
                try:
                    expr = EXPRESSION
                    EXPRESSION = ""
                    self.expression_field.delete(0, tk.END)
                    evaluated = self.evaluate(expr)
                    EXPRESSION = str(evaluated)
                    global ANS
                    ANS = int(evaluated)
                    self.expression_field.insert(tk.END, evaluated)
                except:
                    EXPRESSION = "Error"
                    self.expression_field.delete(0, tk.END)
                    self.expression_field.insert(tk.END, EXPRESSION)
            
            elif btn == "Ans":
                self.expression_field.insert(tk.END, f"{ANS}")
            
            elif btn == "DEL":
                EXPRESSION = EXPRESSION[:-1]
                self.expression_field.delete(len(EXPRESSION), tk.END)
            
            elif btn == "AC":
                EXPRESSION = ""
                self.expression_field.delete(0, tk.END)
        
        # MISCELLANEOUS
        elif btn in MISCELLANEOUS:
            if btn == "(-)":
                EXPRESSION += "-"
                self.expression_field.insert(tk.END, "-")
            
            elif btn == "±":
                EXPRESSION += "-"
                self.expression_field.insert(tk.END, "-")
            
            elif btn == "° ' \"":
                EXPRESSION += "°"
                self.expression_field.insert(tk.END, "°")
            
            elif btn == "π":
                if EXPRESSION[-1] not in OPERATORS:
                    EXPRESSION += "*"
                    self.expression_field.insert(tk.END, "*")
                EXPRESSION += "3.1415"
                self.expression_field.insert(tk.END, btn)
            
            elif btn == "e":
                if EXPRESSION[-1] not in OPERATORS:
                    EXPRESSION += "*"
                    self.expression_field.insert(tk.END, "*")
                EXPRESSION += "2.7182"
                self.expression_field.insert(tk.END, btn)
            
            elif btn == "x!":
                EXPRESSION += "!"
                self.expression_field.insert(tk.END, "!")
            
            elif btn == "RAD":
                EXPRESSION += "RAD("
                self.expression_field.insert(tk.END, "RAD(")
            
            elif btn == "DEG":
                EXPRESSION += "DEG("
                self.expression_field.insert(tk.END, "DEG(")
            
            elif btn == "nPr":
                EXPRESSION += "P"
                self.expression_field.insert(tk.END, "P")
            
            elif btn == "nCr":
                EXPRESSION += "C"
                self.expression_field.insert(tk.END, "C")
        
        # Base N
        elif btn in NUMBER_BASES:
            if btn == "BIN":
                EXPRESSION += "bx"
                self.expression_field.insert(tk.END, "bx")
            
            elif btn == "OCT":
                EXPRESSION += "ox"
                self.expression_field.insert(tk.END, "ox")
            
            elif btn == "DEC":
                EXPRESSION += "dx"
                self.expression_field.insert(tk.END, "dx")
            
            elif btn == "HEX":
                EXPRESSION += "hx"
                self.expression_field.insert(tk.END, "hx")
        
        elif btn == "Const":
            global CONSTANTS
            messagebox.showinfo("Coming Soon!", "Developer is working day-night to add new features.\n\nSTAY TUNED FOR UPDATES!")
        
        elif btn == "Conv":
            global CONVERSION
            messagebox.showinfo("Coming Soon!", "Developer is working day-night to add new features.\n\nSTAY TUNED FOR UPDATES!")
        
        else:
            messagebox.showerror("BUTTON ERROR!", "Sorry, we could not get the button.\n\nPlease try again later!")
        
        global SHIFT, ALPHA
        if SHIFT:
            SHIFT = False
            self.shift()
        if ALPHA:
            ALPHA = False
            self.alpha()
        
        if CONSOLE_LOGGING:
            print("Button Clicked: ",btn)
    
    def make_evaluatable(self, str):
        I = 0
        L = int(len(str))
        ready = ""
        
        while(I<L):
            J = I
            number = ""
            right_bracket = ["²√(", "³√(", "log(", "ln(", "RAD(", "DEG(", "sin(", "cos(", "tan(", "cosec(", "sec(", "cot(", "1/sin(", "1/cos(", "1/tan(", "sinh(", "cosh(", "tanh(", "1/sinh(", "1/cosh(", "1/tanh("]
            base_n = ["bx", "ox", "dx", "hx"]
            
            if ((str[I] in NUMBERS) or (str[I] in OPERATORS) or (str[I] == ".")):
                ready += f"{str[I]}"
                I+=1
            
            elif str[I] in ["(", "{", "["]:
                ready += "("
                I+=1
            
            elif str[I] in [")", "}", "]"]:
                ready += ")"
                I+=1
            
            elif ((str[I:I+3] in ["²√(", "³√(", "ln("]) or (str[I:I+4] in ["sin(", "cos(", "tan(", "sec(", "cot(", "log(", "RAD(", "DEG("]) or (str[I:I+5] in ["sinh(", "cosh(", "tanh("]) or (str[I:I+6] in ["cosec(", "1/sin(", "1/cos(", "1/tan("]) or (str[I:I+7] in ["1/sinh(", "1/cosh(", "1/tanh("])):
                for exp in right_bracket:
                    if str[I:I+len(exp)] == exp:
                        J=I+len(exp)
                        while (str[J] != ")"):
                            number += str[J]
                            J+=1
                        print(number)
                        if (exp == "sin("): ready += f"{self.sine(int(number))}"
                        elif (exp == "cos("): ready += f"{self.cosine(int(number))}"
                        elif (exp == "tan("): ready += f"{self.tangent(int(number))}"
                        elif (exp == "cosec("): ready += f"{self.cosecant(int(number))}"
                        elif (exp == "sec("): ready += f"{self.secant(int(number))}"
                        elif (exp == "cot("): ready += f"{self.cotangent(int(number))}"
                        elif (exp == "1/sin("): ready += f"{self.sin_inverse(int(number))}"
                        elif (exp == "1/cos("): ready += f"{self.cos_inverse(int(number))}"
                        elif (exp == "1/tan("): ready += f"{self.tan_inverse(int(number))}"
                        elif (exp == "sinh("): ready += f"{self.sinh(int(number))}"
                        elif (exp == "cosh("): ready += f"{self.cosh(int(number))}"
                        elif (exp == "tanh("): ready += f"{self.tanh(int(number))}"
                        elif (exp == "1/sinh("): ready += f"{self.sinh_inverse(int(number))}"
                        elif (exp == "1/cosh("): ready += f"{self.cosh_inverse(int(number))}"
                        elif (exp == "1/tanh("): ready += f"{self.tan_inverse(int(number))}"
                        elif (exp == "²√("): ready += f"{self.root(2,int(number))}"
                        elif (exp == "³√("): ready += f"{self.root(3,int(number))}"
                        elif (exp == "log("): ready += f"{self.logarithm(int(number))}"
                        elif (exp == "ln("): ready += f"{self.natural_logarithm(int(number))}"
                        elif (exp == "RAD("): ready += f"{self.radian(int(number))}"
                        elif (exp == "DEG("): ready += f"{self.degree(int(number))}"
                        I = J+1
                        break
            
            elif str[I:I+3] == "ⁿ√(":
                J=I-1
                base = ""
                while((str[J] not in OPERATORS) and (str[J] not in BRACKETS)):
                    base = (str[J] + base)
                    J-=1
                J=I+3
                while(str[J] != ")"):
                    number += str[J]
                    J+=1
                ready += f"{self.root(int(base),int(number))}"
                I = J+1
            
            elif str[I] == "!":
                J=I-1
                while((str[J] not in OPERATORS) and (str[J] not in BRACKETS)):
                    number = (str[J] + number)
                    J-=1
                ready += f"{self.factorial(int(number))}"
                I += 1
            
            elif str[I] in ["P", "C"]:
                before=I-1
                after=I+1
                n1=0
                n2=0
                while((str[after] not in OPERATORS) and (str[after] not in BRACKETS)):
                    n2 += str[after]
                    after+=1
                while((str[before] not in OPERATORS) and (str[before] not in BRACKETS)):
                    n1 = (str[before] + n1)
                    before-=1
                if str[I] == "P": ready += f"{self.nPr(int(before),int(after))}"
                elif str[I] == "C": ready += f"{self.nCr(int(before),int(after))}"
                I = after
            
            elif str[I:I+2] in base_n:
                J=I+2
                while((str[J] not in OPERATORS) and (str[J] not in BRACKETS)):
                    number += str[J]
                    J+=1
                if str[I:I+2] == "bx": ready += f"{self.binary_to_decimal(int(number))}"
                elif str[I:I+2] == "ox": ready += f"{self.octal_to_decimal(int(number))}"
                elif str[I:I+2] == "dx": ready += f"{self.decimal_to_hexadecimal(int(number))}"
                elif str[I:I+2] == "hx": ready += f"{self.hexadecimal_to_decimal(number)}"
                I = J
            
            else:
                I+=1
            
            if CONSOLE_LOGGING:
                print(f"Making Evaluatable at index {I}: {ready}")
        
        if CONSOLE_LOGGING:
            print("Evaluatable String Ready: ", ready)
        return ready
    
    def sine(self, n): return math.sin(math.radians(n))
    def cosine(self, n): return math.cos(math.radians(n))
    def tangent(self, n): return math.tan(math.radians(n))
    def cosecant(self, n): return 1/(math.sin(math.radians(n)))
    def secant(self, n): return 1/(math.cos(math.radians(n)))
    def cotangent(self, n): return 1/(math.tan(math.radians(n)))
    def sin_inverse(self, n): return math.degrees(math.asin(n))
    def cos_inverse(self, n): return math.degrees(math.acos(n))
    def tan_inverse(self, n): return math.degrees(math.atan(n))
    def sinh(self, n): return math.sinh(math.radians(n))
    def cosh(self, n): return math.cosh(math.radians(n))
    def tanh(self, n): return math.tanh(math.radians(n))
    def sinh_inverse(self, n): return 1 / math.sinh(math.radians(n))
    def cosh_inverse(self, n): return 1 / math.cosh(math.radians(n))
    def tanh_inverse(self, n): return 1 / math.tanh(math.radians(n))
    def root(self,base,n): return math.pow(base,1/n)
    def logarithm(self,n): return math.log(n)
    def natural_logarithm(self,n): return math.log(n,math.e)
    def factorial(self, n): return math.factorial(n)
    def radian(self, n): return math.radians(n)
    def degree(self, n): return math.degrees(n)
    def nPr(self, before, after): return math.factorial(before) / math.factorial(before - after)
    def nCr(self, before, after): return math.factorial(before) / (math.factorial(after) * math.factorial(before - after))
    def binary_to_decimal(self, binary): return int(binary, 2)
    def decimal_to_binary(self, decimal): return bin(decimal)[2:]
    def binary_to_octal(self, binary): return oct(self.binary_to_decimal(binary))[2:]
    def octal_to_binary(self, octal): return self.decimal_to_binary(int(octal, 8))
    def binary_to_hexadecimal(self, binary): return hex(self.binary_to_decimal(binary))[2:]
    def hexadecimal_to_binary(self, hexadecimal): return self.decimal_to_binary(int(hexadecimal, 16))
    def decimal_to_octal(self, decimal): return oct(decimal)[2:]
    def octal_to_decimal(self, octal): return int(octal, 8)
    def decimal_to_hexadecimal(self, decimal): return hex(decimal)[2:]
    def hexadecimal_to_decimal(self, hexadecimal): return int(hexadecimal, 16)
    def evaluate(self, str):
        if CONSOLE_LOGGING:
            print("Evaluating: ",str)
        ready = self.make_evaluatable(str)
        done = eval(ready)
        if CONSOLE_LOGGING:
            print("Evaluated: ", done)
        return done
    
    def run(self):
        self.window.mainloop()
        if CONSOLE_LOGGING:
            print("Exiting Calculator.")

if __name__ == "__main__":
    app = Calculator()
    app.run()