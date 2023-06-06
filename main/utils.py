from django.forms import ValidationError

def valid_price(price):
    if int(price) <= 0:
        raise ValidationError("price dont minus")
    
    if not price.isdigit():
        raise ValidationError("Prise is int")
    
    num = "0123456789"
    for i in price:
        if i not in num:
            raise ValidationError("Prise is not int")
        