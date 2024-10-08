from tkinter import *
import logging

from memory import *
from calculations import  calculate

# logging.INFO => nie wyświetla
# logging.DEBUG => wyświetla
logging.basicConfig(level=logging.DEBUG)

root = Tk()
root.title('Calculator')

# Background color
root.configure(bg='#333438')

input_ = Entry(root, width=15, borderwidth=5, font=('Arial 24'))
input_.grid(row=0, column=0, columnspan=6, padx=30, pady=30)



# Buttons
plus_button = Button(root, text='+', padx=32.5, pady=30, bg='#909090', activebackground='#909090',
                     command=lambda: get_values_from_input('+'))
plus_button.grid(column=3, row=3)

substract_button = Button(root, text='- ', padx=32.5, pady=30, bg='#909090', activebackground='#909090',
                          command=lambda: get_values_from_input('-'))
substract_button.grid(column=3, row=2)

is_equal = Button(root, text='= ', padx=30.4, pady=30, bg='#909090', activebackground='#909090',
                  command=lambda: (calculate_and_display()))
is_equal.grid(column=4, row=4)

zero_button = Button(root, text='0', padx=66.7, pady=30, fg='black', bg='#696969', activebackground='#696969',
                     command=lambda: numbers('0'))
zero_button.grid(column=0,columnspan=2, row=4)

clear_button = Button(root, text='C', padx=32.5, pady=30, bg = '#b22222', activebackground='#8b0000',
                      command=lambda: (clear_input(), clear_memory()))
clear_button.grid(column=3, row=1)

mulitplay_button = Button(root, text='x', padx=31, pady=30, bg='#909090', activebackground='#909090',
                          command=lambda: get_values_from_input('*'))
mulitplay_button.grid(column=2, row=4)

divison_button = Button(root, text='/ ', padx=33.4, pady=30, bg='#909090', activebackground='#909090',
                        command=lambda: get_values_from_input('/'))
divison_button.grid(column=3, row=4)

del_button = Button(root, text='DEL', padx=24.5, pady=30, bg='#909090', activebackground='#909090',
                             command=lambda:  get_values_from_input('DEL'))
del_button.grid(column=4, row=1)

bracket_button_right = Button(root, text=' (', padx=31.5, pady=30, bg='#909090', activebackground='#909090',
                              command=lambda: get_values_from_input('('))
bracket_button_right.grid(column=4, row=2)

#plus_minus_button = Button(root, text = '+/-',padx=26, pady=30,
                           #command=lambda: get_values_from_input(''))

#plus_minus_button.grid(column=4,row=3)

bracket_button_right = Button(root, text=' )', padx=31.5, pady=30,  bg='#909090', activebackground='#909090',
                              command=lambda: get_values_from_input(')'))
bracket_button_right.grid(column=4,row=3)




# From 1 to 9
buttons = []
    
for i in range(1, 10):
    button = Button(root, text=str(i), padx=30, pady=30, fg='black', bg='#696969', activebackground='#696969',
                    command=lambda i=i: numbers(i))
    buttons.append(button)

# Placing buttons
for i, button in enumerate(buttons):
    button.grid(row=i // 3 + 1, column=i % 3)


#Display number in input
def numbers(number):
    current = input_.get()
    input_.insert(len(current) + 1, number)
    

#Gather numbers from input
def get_values_from_input(operator):
    current_text = input_.get()

    if operator == 'DEL':
        if current_text:  
            input_.delete(len(current_text) - 1)  
        return None

    # If current_text is empty
    if current_text == "":
        if operator == '(':
            add_to_memory(operator)
            clear_input()
        return None

    # Handle the case of closing parenthesis ')'
    if operator == ')':
        # Count the number of opening and closing parentheses in memory
        open_parentheses = memory.count('(')
        close_parentheses = memory.count(')')
        
        # Only add a closing parenthesis if there's an unmatched opening one
        if open_parentheses > close_parentheses:
            add_to_memory(current_text,operator)
            
            clear_input()
        return None

    # Ensure that we are not allowing operators to be followed by closing parentheses or invalid sequences
    if operator in ['+', '-', '*', '/']:
        if current_text != '' and current_text not in ['(', ')']:
            add_to_memory(current_text)
            add_to_memory(operator)
            clear_input()
        return None

    # Add number or opening parenthesis to memory
    add_to_memory(current_text)
    add_to_memory(operator)
    clear_input()
    return None


def calculate_and_display():
    get_values_from_input('=')  
    result = calculate(memory)

    if result == 0:
        input_.insert(0,str('N/A'))
    
    input_.insert(0,str(result[0]))
    clear_memory()
    
    add_to_memory(result[0])

def clear_input():
    input_.delete(0,END)

root.mainloop()
