def integer(msg):
 while(True):
  try:
     a=float(input(msg))    
     return a
  except ValueError as E:print("Pls input Integer Only....")