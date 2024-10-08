class Calculator:
    def __init__(self, input_array: list):
        self.input_array = input_array

    def search_for_brackets(input_array):
        brackets_dict = {}
        stack = []  

        for index, char in enumerate(input_array):
            if char == '(':  
                stack.append(index)  
            elif char == ')':  
                if stack:  
                    open_bracket_index = stack.pop()  
                    brackets_dict[open_bracket_index] = '('
                    brackets_dict[index] = ')'

                    return brackets_dict
         
    def multiplication(self,index):
            result = float(self.input_array[index-1]) * float(self.input_array[index+1])
            if result.is_integer():
                result = int(result)
            self.input_array[index-1:index+2] = [str(result)]
            return self.input_array

    def division(self,index):
        try:
            result = float(self.input_array[index-1]) / float(self.input_array[index+1])
            if result.is_integer():
                result = int(result)
            self.input_array[index-1:index+2] = [str(result)]
        except ZeroDivisionError:
            return 0
        except ValueError:
            return 0
        return self.input_array
    
    def addition(self,index):

        result = float(self.input_array[index-1]) + float(self.input_array[index+1])
        if result.is_integer():
            result = int(result)
        self.input_array[index-1:index+2] = [str(result)]
 
        return self.input_array
    
    def subtraction(self,index):

        result = float(self.input_array[index-1]) - float(self.input_array[index+1])
        if result.is_integer():
            result = int(result)
        self.input_array[index-1:index+2] = [str(result)]

        return self.input_array

    def mul_and_div(self):
        print(self.input_array)
        index = 1
        while len(self.input_array) > 2:
            if self.input_array[index] == '*':
                self.multiplication(int(index))
                index = 1
            
            elif self.input_array[index] == '/':
                result = self.division(int(index))
                if result == 0:
                    return 0
                index = 1
            else:
                index += 1
            if self.input_array[index] == '=':
                return self.input_array

    def add_and_sub(self, result):
        index = 1
        while index < len(result):
            if result[index] == '+':
                self.addition(index)
                index = 1  # Reset to 1 to re-evaluate the list from the beginning
            elif result[index] == '-':
                self.subtraction(index)
                index = 1  # Reset to 1 after subtraction
            else:
                index += 1  # Move to the next element

            # Stop processing if the '=' operator is encountered
            if index < len(result) and result[index] == '=':
                return result  # Return the result once '=' is found

def calculate(memory: list):
    print(memory)
    calc = Calculator(memory)
    sub_array = calc.mul_and_div()
    #If tried divide by 0
    if sub_array == 0:
        return 0
    #If
    if len(sub_array) == 2:
        return sub_array
    result = calc.add_and_sub(sub_array)

    return result
