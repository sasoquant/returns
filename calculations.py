def price_change(start_price, end_price):
    return end_price - start_price


def return_value(start_price, end_price):
    difference = price_change(start_price, end_price)
    return difference / start_price
