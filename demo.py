# python program swap between 3 number

userinput = int(input("enter 1st number : "))
userinput1 = int(input("enter 2nd number : "))
userinput2 = int(input("enter 3rd number : "))

print('you enter : ', userinput, ",", userinput1, ",", userinput2)

userinput, userinput1, userinput2 = userinput1, userinput2, userinput

print('after swapping  : ', userinput1, ',', userinput2, ',', userinput)
