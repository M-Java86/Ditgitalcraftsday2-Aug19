#Using a while loop, print out the numbers between 1 and 10 inclusive, one on a line. Example output:
#python 1_to_10.py
#n = 0
#while n <= 10:
    #print(n)
    #n += 1

 #python n_to_m.py
#Start from: 2
#End on: 8
#num1 = int(input (" Name a number:"))
#num2 = int(input("Name another number"))

#n = num1
#while n <= num2:
    #print(n)
    #n +=1

#Print each odd number between 1 and 10 inclusive. Example output:

  #python odd_numbers.py 
#n = 0
#while n <= 10:
    #if n % 2 == 1:
        #print(n)
    #n += 1


x = True
i = 0 
while x:   
    print ("you have" + str(i) + "coins.")
    answer = str(input("do you want another?"))
    if answer == "yes":
           i = i + 1
    else:
           print("Bye") 
           x = False  