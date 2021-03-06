import os	# operating system

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue	#繼續(跳過，跳到下一迴)
			name, price = line.strip().split(',')	#split切割  用逗點做分割
			products.append([name, price])
	return products			

#讓使用者輸入
def user_input(products):
	while  True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')    
		products.append([name, price])    #建立二維清單(小清單)並放入大清單
	print(products)
	return products			

def print_products(products):
	# 印出所有購買紀錄
	for p in products:
		print(p[0], '的價格是', p[1])

def write_file(filename, products):
	# 寫入檔案
	with open(filename, 'w', encoding = 'utf-8') as f:	#w = 寫入模式	r = 讀取模式	 .csv電腦常用儲存資料的檔案格式(尤其是有多種不同屬性) #寫入編碼解決亂碼問題
		f.write('商品,價格\n')																						#若Excel仍是亂碼 可從內部調整	
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')	#f.write = 寫入


def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yes')
		products = read_file(filename)
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()
