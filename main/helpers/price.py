

def convert_price(price):
    price = price.replace("\n", "")
    price = price.replace("\t", "")
    price = price.replace("R$", '')
    price = price.replace(" ", '')
    [num, dec] = price.split(",")
    num = int(num.replace(".", ""))
    dec = (int(dec)/100)
    return float(num + dec)
