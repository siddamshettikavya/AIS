def discount(price, category):
    if category == "student":
        return price * (0.90 if price > 1000 else 0.95)

    if price > 2000:
        return price * 0.85

    return price
print(discount(1200, "student"))  
print(discount(900, "student"))   
print(discount(2500, "regular"))  
print(discount(1500, "regular")) 


