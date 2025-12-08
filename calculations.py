def price_change(p0, p1):
    return p1 - p0


def return_value(start_price, end_price):
    difference = price_change(start_price, end_price)
    return difference / start_price
