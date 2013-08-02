# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

#逗号没有消除换行
print('These items are:'),
for item in shoplist:
    print(item),

print('\nI also have to buy rice')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('MY shopping list is now', shoplist)

#'ab' is short for 'a'ddress'b'ook
ab = {	'Swaroop'	: 'Swaroop@python.info',
	'Larry'		: 'larry@wall.org'
}
print('address is %s' % ab['Swaroop'])
ab['Guido'] = 'guido@pyrhon.org'
del ab['Larry']

for name, address in ab.items():
    print('Contact %s at %s' %  (name ,address))
