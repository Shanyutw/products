products = []
while  True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')    
	products.append([name, price])    #建立二維清單(小清單)並放入大清單
print(products)			

for p in products:
	print(p[0], '得價格是', p[1])