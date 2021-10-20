try:
    cost = float(input('Enter the bikes price in Rs'))
except ValueError as error:
    print('Entered invalid price', error)
else:
    if cost > 100000:
        #15% road tax
        taxRate = 15/100
    elif cost > 50000 and cost<=100000:
        taxRate = 10/100
    elif cost <= 50000:
        taxRate = 5/100
    print("Your tax amount is {} rands".format(taxRate*cost))

