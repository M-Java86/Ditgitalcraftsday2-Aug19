#day = int(input('Day(0-6)? '))
#if day == 0: print("Sunday")
#if day == 1: print("Monday")
#if day == 2: print("Tuesday")
#if day == 3: print("Wednesday")
#if day == 4: print("Thursday")
#if day == 5: print("Friday")
#if day == 6: print("Saturday")
#if day == 6 or day == 0:
   #print ("Sleep in")
#else:
   #print ("Go to work")



amt_of_bill = float(input("Total bill amount? "))
rank_service = input("Good, Fair, or Bad Service? ")
split_amt = int(input("Split how many ways? "))
def tip(rank_service):
   if rank_service == "Good":
       return amt_of_bill * .2
   elif rank_service == "Fair":
       return amt_of_bill * .15
   elif rank_service == "Bad":
       return amt_of_bill * .10
print ("Tip Amount: " + str(tip(rank_service)))
total = tip(rank_service) + amt_of_bill
print ("Total amount: " + str(total))
print ("Amount per person: " + str(total/split_amt))







