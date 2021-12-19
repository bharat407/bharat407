print("  **************************************************************************************")
print('                               WELCOME To Unit Converter')
print("  **************************************************************************************")
print ("LENGTH CONVERSION :1")
print ("MASS CONVERSION :2")
print ("TEMPERATURE CONVERSION :3")
print ("ANGLES CONVERSION :4")
print ("AREA CONVERSION :5")
print ("DATA CONVERSION :6")
print("  **************************************************************************************")
import Function
choice1=Function.integer(("Enter your choice:"))
# choice1=int(input("Enter your choice:"))

print("    **************************************************************************************")
if choice1==1:
 print("   ************************TOCONVERT************************\n")
 print (" milimeter => centimeter :1")
 print (" centimeter => meter :2")
 print (" meter => kilometer :3")
 print (" kilometer => meter :4")
 print (" meter => centimeter :5")
 print (" centimeter => milimeter :6")
 print("**************************************************************************************")
 choice2=Function.integer(("Enter your choice:"))
 # choice2=int(input("Enter your choice:"))
 print("**************************************************************************************")
 if choice2==1:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**-1)
     print(cal,"centimeters")
 elif choice2==2:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**-2)
     print(cal,"meters")
 elif choice2==3:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**-3)
     print(cal,"kilometers")
 elif choice2==4:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**3)
     print(cal,"meters")
 elif choice2==5:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**2)
     print(cal,"centimeters")
 elif choice2==6:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**1)
     print(cal,"milimeters")
 else:
      print("Wrong Choice!!! , Please select an appropriate option..... ")
      print("**************************************************************************************")
elif choice1==2:
 print("**********************TO CONVERT************************\n")
 print (" miligram => gram :1")
 print (" gram => kilogram :2")
 print (" kilogram => tonne :3")
 print (" tonne => kilogram :4")
 print (" kilogram => gram :5")
 print (" grma => miligram :6")
 print("**************************************************************************************")
 choice2=Function.integer(("Enter your choice:"))
 # choice2=int(input("Enter your choice:"))
 print("**************************************************************************************")
 if choice2==1:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**-3)
     print(cal,"grams")
 elif choice2==2:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**-3)
     print(cal,"kilograms")
 elif choice2==3:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**-3)
     print(cal,"tonne")
 elif choice2==4:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**3)
     print(cal,"kilograms")
 elif choice2==5:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**3)
     print(cal,"grams")
 elif choice2==6:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**3)
     print(cal,"miligram")
 else:
     print("Wrong Choice!!! , Please select an appropriate option..... ")
elif choice1==3:
 print("**********************TO CONVERT************************\n")
 print (" celcius => fahrenhiet :1")
 print (" celcius => kelvin :2")
 print (" kelvin => celcius :3")
 print (" fahrenhiet => celcius :4")
 print("**************************************************************************************")
 choice2=Function.integer(("Enter your choice:"))
 # choice2=int(input("Enter your choice:"))
 print("**************************************************************************************")
 if choice2==1:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(9/5)+32
     print(cal,"fahrenhiet")
 elif choice2==2:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag+273.15
     print(cal,"kelvin")
 elif choice2==3:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag-273.15
     print(cal,"celcius")
 elif choice2==4:
     mag=Function.integer(("Enter the value which you want :"))
     cal=(mag-32)*5/9
     print(cal,"celcius")
 else:
    print("Wrong Choice!!! , Please select an appropriate option..... ")
elif choice1==4:
 print("**********************TO CONVERT************************\n")
 print (" DEGREE => MINUITES :1")
 print (" MINUITES => SECONDS :2")
 print (" SECONDS => MINUITES :3")
 print (" MINUITES => DEGREE :4")
 print("**************************************************************************************")
 choice2=Function.integer(("Enter your choice:"))
 # choice2=int(input("Enter your choice:"))
 print("**************************************************************************************")
 if choice2==1:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*60
     print(cal,"minuites")
 elif choice2==2:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*60
     print(cal,"seconds")
 elif choice2==3:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag/60
     print(cal,"minuites")
 elif choice2==4:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag/60
     print(cal,"degrees")
 else:
    print("Wrong Choice!!! , Please select an appropriate option..... ")
if choice1==5:
 print("**********************TO CONVERT************************\n")
 print (" milimeter^2 => centimeter^2 :1")
 print (" centimeter^2 => meter^2 :2")
 print (" meter^2 => kilometer^2 :3")
 print (" kilometer^2 => meter^2 :4")
 print (" meter^2 => centimeter^2 :5")
 print (" centimeter^2 => milimeter^2 :6")
 print("**************************************************************************************")
 choice2=Function.integer(("Enter your choice:"))
 # choice2=int(input("Enter your choice:"))
 print("**************************************************************************************")
 if choice2==1:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**-2)
     print(cal,"centimeters^2 ")
 elif choice2==2:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**-4)
     print(cal,"meters^2 ")
 elif choice2==3:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**-6)
     print(cal,"kilometers^2 ")
 elif choice2==4:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**6)
     print(cal,"meters^2 ")
 elif choice2==5:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**4)
     print(cal,"centimeters^2 ")
 elif choice2==6:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag*(10**2)
     print(cal,"milimeters^2 ")
     print("**************************************************************************************")
 else:
     print("Wrong Choice!!! , Please select an appropriate option..... ")
if choice1==6:
 print("************************TOCONVERT************************\n")
 print ("BITS => BYTES :1")
 print ("BYTES => KILOBYTES :2")
 print ("KILOBYTES => MEGABYTES :3")
 print ("MEGABYTES => GIGABYTES :4")
 print ("GIGABYTES => TERABYTES :5")
 print ("TERABYTES => ZETABYTES :6")
 print("**************************************************************************************")
 choice2=Function.integer(("Enter your choice:"))
 # choice2=int(input("Enter your choice:"))
 print("**************************************************************************************")
 if choice2==1:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag/(8)
     print(cal,"Bytes")
 elif choice2==2:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag/(1024)
     print(cal,"Kilobytes")
 elif choice2==3:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag/(1024)
     print(cal,"Megabytes")
 elif choice2==4:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag/(1024)
     print(cal,"Gigabytes")
 elif choice2==5:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag/(1024)
     print(cal,"Terabytes")
 elif choice2==6:
     mag=Function.integer(("Enter the value which you want :"))
     cal=mag/(1024)
     print(cal,"Zetabytes")
 else:
    print("Wrong Choice!!! , Please select an appropriate option..... ")
else:
    print("    **************************************************************************************")
