#example for numeric datatype
quantity_of_shirts=23
price_of_shirts=1999.0
price=1999.0+2j
print("original price:",price.real)
print("discount price",price.imag)
final_price=price.real-price.imag
print("shirts:",quantity_of_shirts)
print("price of shirts before discount:",price_of_shirts)
print(final_price)

#Example:Online shopping cart for integer datatype
quantity_of_shirts=34
quantity_of_pants=23
quantity_of_whiteshirts=55
total_items=quantity_of_shirts+quantity_of_pants+quantity_of_whiteshirts
print("total items in cart:",total_items)

#Eample:Product pricing for float datatype
price_of_shirts=299.0
price_of_pants=199.0
price_of_kurtis=499.0
product_price=price_of_shirts+price_of_pants+price_of_kurtis
print(product_price)

#Example:cart with discount for complex datatype
price=100+20j
#here 100=real part and it is original price,20j=imaginary part and it is discount price
print("original price:$",price.real)
print("discount price:$",price.imag)
final_price=price.real-price.imag
print(final_price)
