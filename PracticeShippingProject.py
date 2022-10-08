#Guided(ish) Python Shipping Project, 10/7/2022
#Beginner

#Ground Shipping
def GroundShipping(weight):
  if weight <= 2:
    price_per_pound = 1.50
    flat_rate = 20.00
    premium_rate = 125.00
    cost = (price_per_pound * weight) +       flat_rate
    premium_cost = cost + premium_rate 
    print("Ground Shipping Total Cost: " + "{:.2f}".format(cost))
    print("Ground Shipping Premium Cost: " + "{:.2f}".format(premium_cost))

  elif weight > 2 and weight <= 6:
    price_per_pound = 3.00
    flat_rate = 20.00
    premium_rate = 125.00
    cost = (price_per_pound * weight) + flat_rate
    premium_cost = cost + premium_rate 
    print("Ground Shipping Total Cost: " + "{:.2f}".format(cost))
    print("Ground Shipping Premium Cost: " + "{:.2f}".format(premium_cost))

  elif weight > 6 and weight <= 10:
    price_per_pound = 4.00
    flat_rate = 20.00
    premium_rate = 125.00
    cost = (price_per_pound * weight) +   flat_rate
    premium_cost = cost + premium_rate 
    print("Ground Shipping Total Cost: " + "{:.2f}".format(cost))
    print("Ground Shipping Premium Cost: " + "{:.2f}".format(premium_cost))

  elif weight > 10:
    price_per_pound = 4.75
    flat_rate = 20.00
    premium_rate = 125.00
    cost = (price_per_pound * weight) + flat_rate
    premium_cost = cost + premium_rate 
    print("Ground Shipping Total Cost: " + "{:.2f}".format(cost))
    print("Ground Shipping Premium Cost: " + "{:.2f}".format(premium_cost))

#Drone Shipping
def DroneShipping(weight):
  if weight <= 2:
    price_per_pound = 4.50
    flat_rate = 0.00
    cost = (weight * price_per_pound) + flat_rate
    print("Drone Shipping Total Cost: " + "{:.2f}".format(cost))

  elif weight > 2 and weight <= 6:
    price_per_pound = 9.00
    flat_rate = 0.00
    cost = (weight * price_per_pound) + flat_rate
    print("Drone Shipping Total Cost: " + "{:.2f}".format(cost))

  elif weight > 6 and weight <= 10:
    price_per_pound = 12.00
    falt_rate = 0.00
    cost = (weight * price_per_pound) + flat_rate
    print("Drone Shipping Total Cost: " + "{:.2f}".format(cost))

  elif weight > 10:
    price_per_pound = 14.25
    flat_rate = 0.00
    cost = (weight * price_per_pound) + flat_rate
    print("Drone Shipping Total Cost: " + "{:.2f}".format(cost))

GroundShipping(41.5)
DroneShipping(41.5)


