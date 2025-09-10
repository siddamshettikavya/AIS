def discount(price, category):
    if category == "student":
        if price > 1000:
            return price * 0.9  
        else:
            return price * 0.95  
    else:
        if price > 2000:
            return price * 0.85  
        else:
            return price
print(discount(1200, "student"))  
print(discount(900, "student"))   
print(discount(2500, "regular"))  
print(discount(1500, "regular"))