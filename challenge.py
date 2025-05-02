#Celsius -------> Farenhiet
'''
c=input('Celsius: ')
c=float(c)
f=(c*9/5) + 32
print('Fahrenheit: ',f)


# Farenhiet-------> Celsius
f=input('Fahrenheit: ')
f=float(f)
c=(f-32)*5/9
print('Celsius: ',c)
'''

#Simple Interest calculator
#Eq prt/100
p = input('principal: ')
r = input('rate: ')
t = input('time: ')
p = int(p)
r = float(r)
t = float(t)
SI = (p*r*t)/100
print('Simple Interest: ',SI)