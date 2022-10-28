#Investment Report

#Take input values from the user 
amt = float(input("Enter the deposit amount: "))
years = int(input("Enter the number of years: "))
rate = float(input("Enter the rate in %: "))
#convert rate to a decimal number
rate/=100
totalInterest = 0.0

#start the header of the table
print("%5s%18s%14s%19s" % ("Year", "Starting balance", "Interest", "Ending balance"))

for years in range(1,years + 1):
    interest = amt*rate
    endbalance = amt + interest
    print("%4d%15.2f%16.2f%20.2f" % (years, amt, interest, endbalance))
    amt = endbalance
    totalInterest+= interest
    
print("Total Amount: ", "%1.2f" % endbalance)
print("Total Interest earned: ", "%0.2f" % totalInterest)
