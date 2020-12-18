cont = moreT = total = price_l = price_e = 0

print('-'*30)
print('Shop'.center(30))
print('-'*30)

while True:
    # Insert informations
    name =  str(input('Product name: '))
    price =  float(input('Product price: $'))

    # Adding values
    cont += 1
    total += price

    price_e = price
    price_l = price
    name_e = name
    name_l = name
    

    # Checks
    if price > 1000:
        moreT += 1

    if price < price_l:
        price_l = price
        name_l = name

    if price > price_e:
        price_e = price
        name_e = name


    # Finish
    Continue = ' '
    while Continue not in 'YN':
        Continue = str(input('Continue?')).strip().upper()[0]
    if Continue == 'N':
        break

print('-'*30)
print('Results')

print('~'*30)

# Print informations

print('Items: {}'.format(cont))
print('Most expensive: {}: ${}'.format(name_e,round(price_e,3)))
print('Lowest price: {}: ${}'.format(name_l,round(price_l,3)))
print('There is {} items with price biggest than $1000'.format(moreT))

print('~'*30)