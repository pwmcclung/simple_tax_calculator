""" A very simple tax calculator based on  US tax Laws for year 2020"""

# Declare the variables

max10 = 9875
max12 = 40125
max22 = 85525
max24 = 163300
max32 = 207350
max35 = 518400

tier10_tax = max10 * 0.1
tier12_tax = tier10_tax + ((max12 - max10) * 0.12)
tier22_tax = tier12_tax + ((max22 - max12) * 0.22)
tier24_tax = tier22_tax + ((max24 - max22) * 0.24)
tier32_tax = tier24_tax + ((max32 - max24) * 0.32)
tier35_tax = tier32_tax + ((max35 - max32) * 0.35)

# Define user input
gross_inc = input('Enter your gross income for your W-2 for 2020: ')
num_dep = input('How many dependants are you claiming? ')


# Convert the input values to numbers
gross_inc_float = float(gross_inc)
num_dep_int = int(num_dep)


# Calculate the taxable income
tax_income = gross_inc_float - 12220 - (2000 * num_dep_int)


if tax_income <= 0:
    tax_due = 0
elif tax_income <= max10:
    tax_due = tax_income * 0.1
elif tax_income <= max12:
    tax_due = tier10_tax + ((tax_income - max10) * 0.12)
elif tax_income <= max22:
    tax_due = tier12_tax + ((tax_income - max12) * 0.22)
elif tax_income <= max24:
    tax_due = tier22_tax + ((tax_income - max22) * 0.24)
elif tax_income <= max32:
    tax_due = tier24_tax + ((tax_income - max24) * 0.32)
elif tax_income <= max35:
    tax_due = tier32_tax + ((tax_income - max32) * 0.35)
elif tax_income > max35:
    tax_due = tier35_tax + ((tax_income - max35) * 0.37)

# report the results to the user
print("You gross income is $" + gross_inc + ".")
print("You have " + num_dep + " dependants.")
print("Your taxable income is $ " + str(tax_income) + ".")
print("Your tax due in $ " + str(int(tax_due)) + ".")
