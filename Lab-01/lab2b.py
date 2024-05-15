# Name: Hasini Jayasekara
# Student ID : 165513235

#defining variables
tax_income = input(" Enter your gross income")
dependent_count = input(" Enter number of dependents")


gross_income = float(tax_income)                                    #converting the variables in to float values
dependent = float(dependent_count)                                  #converting the variables in to float values
standard_deduction = 10000                                          #defining standard deduction amount
dependent_deduction_amount = 2000                                   #defining deduction amount for dependent
dependent_deduction = dependent * float(dependent_deduction_amount) #calculation for the dependent deduction

taxable_income = gross_income - (standard_deduction + dependent_deduction) # calculation for the taxable income

if(taxable_income < 32000 ):                                        #checks the taxable income is less than 32000
  tax_rate1 = 0.1                                                   #define the tax rate 
  result = taxable_income*tax_rate1                                 #calculating the tax income
  if(result <0):                                                    #check if the result is a negative value

   print("The total tax is zero")      #print statement
  else:
   print(" The total tax is "+str(result))                          #if result value is not a negative value then it prints the total tax amount
 

elif(taxable_income >= 32000) and (taxable_income < 64000):
  tax_rate2 =0.15
  result = taxable_income*tax_rate2
  if(result <0):
   print("The total tax is zero")
  else:
   print(" The total tax is "+str(result))

elif(taxable_income>=64000):
 tax_rate3 =0.25
 result = taxable_income*tax_rate3
 if(result <0):
   print("The total tax is zero")
 else:
   print(" The total tax is "+str(result))

else:
  print(" End")
 

