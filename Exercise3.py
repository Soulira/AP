weekdays = {"Monday","Tuesday", "Wednesday", "Thursday", "Friday" }
weekends = {"Saturday", "Sunday"}
amount = input("Total amount:")

nb_item = input("Number of items: ")

Day = input("Day of the week:").strip().title()
if Day in weekdays or Day in weekends :
        if Day in weekdays :
            if int(nb_item) > 5 :
               price = float(amount) - (float(amount) * (15/100))
            else :
                 price = float(amount) - (float(amount) * (10/100))   
        else:
            if int(nb_item) > 5 :
               price = float(amount) - (float(amount) * (25/100))
            else :
                price = float(amount) - (float(amount) * (20/100))   
else :
        print("Enter a valid Day of week please")            

print("Total price after discount:",price)


