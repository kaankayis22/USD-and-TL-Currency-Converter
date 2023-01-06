from forex_python.converter import CurrencyRates

c = CurrencyRates()
noChoice = True

print("Welcome. Please select from the options below")
print("[1]USD to TL")
print("[2]TL to USD")
print("[3]View Rates")
num = int(input("Enter your choice:"))
rate = c.get_rate('USD', 'TRY') 

if(num==1):
  
  USD = int(input("Enter amount of USD:$"))
  result = USD * rate
  print("That would make " + str(result) + " Lira!")
  
elif(num==2):
  TL = int(input("Enter amount of TL: "))
  result = TL / rate
  print("That would make " + str(result) + " USD!")
elif(num==3):
  
  print("Currently, one USD is " + str(rate)) 
else:
   print("That is not a supported option :(")
