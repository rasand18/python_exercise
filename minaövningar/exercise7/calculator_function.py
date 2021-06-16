def my_calculator(f_number,operator,s_number):
    if operator == "/" and s_number==0:
        
        return "You cant devide by 0"
    else:   
        if operator == "*":
            suM = f_number*s_number
            return suM
        elif operator == "/":
            suM = f_number/s_number
            return suM
        elif operator == "-":
            suM = f_number-s_number
            return suM
        elif operator == "+":
            suM = f_number+s_number
            return suM
        else:
            return "You have entered a non numeric number or chosen an operator that dosent exist"



f_number = int(input("Enter a number: "))
operator = input("Which operator would you like to use *, / , - or + ?: ")
s_number = int(input("Now enter your second number: "))
suM = 0

print(my_calculator(f_number,operator,s_number))


