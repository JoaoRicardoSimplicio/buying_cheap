

def convert_price(price):
    price = price.replace("\n", "")
    price = price.replace("\t", "")
    price = price.replace("R$", '')
    price = price.replace(" ", '')
    try:
        [num, dec] = price.split(",")
    except Exception:
        return float(price)
    num = int(num.replace(".", ""))
    dec = (int(dec)/100)
    return float(num + dec)
