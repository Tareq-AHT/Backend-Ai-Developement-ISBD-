# write a paython script, find compound interest of an amount. 
# deposite amount, interest rate, year

principal = float(input("Principal amount (in BDT): "))             # Main amount
interest_rate = float(input("Interest rate (in percentage): "))     
year = int(input("Year: "))                                         # for how many years
compound_frequency = int(input("For how many times per year: "))       # for how many times the interest will be compound

expo = compound_frequency*year
divide = (interest_rate/(100*compound_frequency))
calculation = (1 + (interest_rate/(100*compound_frequency)))**expo

compound_amount = principal * calculation                      # A = p*(1 + (r/(100*n))**(n*t))
print(f"Your compound amount is {compound_amount:.2f} BDT")

compound_interest = compound_amount - principal
print(f"You have received {compound_interest:.2f} BDT as interest")



