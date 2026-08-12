def calculate_checkout(cart_total, shipping_speed):

    if shipping_speed == "express":
        shipping_cost = 20.00
    elif shipping_speed == "overnight":
        shipping_cost = 35.00
    elif shipping_speed == "standard" and cart_total >= 100.00:
        shipping_cost = 0.00
    elif shipping_speed == "standard":
        shipping_cost = 10.00
    else:
        print("Invalid shipping speed. Please choose 'express', 'overnight', or 'standard'.")
        shipping_cost = 0.00

    total_cost = cart_total + shipping_cost
    return total_cost

#example function call
print("total checkout cost is:", calculate_checkout(100.00, "standard"))

