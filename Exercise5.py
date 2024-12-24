Runner1 = input("Runner 1:\nName:")
Time1 = input("Time (in seconds):")
Runner2 = input("Runner 1:\nName:")
Time2 = input("Time (in seconds):")
if float(Time1) == float(Time2):
   print(""+Runner1+" and "+Runner2+" have the same time")
else: 
    if Tmax(float(Time2),float(Time1))==Time1:
         print("The faster runner is "+ Runner1)
    else:
         print("The faster runner is "+ Runner2)

