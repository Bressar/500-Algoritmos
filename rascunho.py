def dis(price, discount):
    price_discount = price - ((price * discount) / 100)
    return round(price_discount, 2)
		
		
print(dis(1500, 50))
print(dis(89, 20))
print(dis(100, 75))

print('--' * 25)

def dis(price, discount):
	discount = discount / 100
	newPrice = price - (price * discount)
	return round(newPrice,2)


print(dis(1500, 50))
print(dis(89, 20))
print(dis(100, 75))
