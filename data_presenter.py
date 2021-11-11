invoices = open('CupcakeInvoices.csv')

for invoice in invoices:
    print(invoice)

invoices.close()

invoices = open('CupcakeInvoices.csv')
    
for invoice in invoices:    
    columns = invoice.split(',')
    print(columns[2])

invoices.close()

invoices = open('CupcakeInvoices.csv')

for invoice in invoices:
    columns = invoice.split(',')
    print(round(float(columns[3]) * float(columns[4]), 2))

invoices.close()

invoices = open('CupcakeInvoices.csv')

sum = 0
for invoice in invoices:
    columns = invoice.split(',')
    sum += float(columns[3]) * float(columns[4])
print(round(sum, 2))

invoices.close()

invoices = open('CupcakeInvoices.csv')
flavor = ['Chocolate', 'Vanilla', 'Strawberry']
total = [0, 0, 0]
for invoice in invoices:
    columns = invoice.split(',')
    if columns[2] == 'Chocolate':
        total[0] += round(float(columns[3]) * float(columns[4]), 2)
    elif columns[2] == 'Vanilla':
        total[1] += round(float(columns[3]) * float(columns[4]), 2)
    elif columns[2] == 'Strawberry':
        total[2] += round(float(columns[3]) * float(columns[4]), 2)


import matplotlib.pyplot as plt

plt.bar(flavor,total)
plt.title('Total sales by flavor')
plt.xlabel('Flavor')
plt.ylabel('Total in $')
plt.show()

invoices.close()