# Name: Hasini Jayasekara
# Student ID : 165513235

#defining variables
tax_income = input(" Enter your gross income")
dependent_count = input(" Enter number of dependents")

gross_income = float(tax_income)
dependent = float(dependent_count)
standard_deduction = 10000
dependent_deduction_amount = 2000
dependent_deduction = dependent * float(dependent_deduction_amount)

taxable_income = gross_income - (standard_deduction + dependent_deduction)

if(taxable_income < 32000 ):
  tax_rate1 = 0.1
  result = taxable_income*tax_rate1
  if(result <0):

   print("The total tax is zero")
  else:
   print(" The total tax is "+str(result))
 

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
 

