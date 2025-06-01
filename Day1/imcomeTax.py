from AllTax import nandedTax
import AllTax

# Tax of market
tax1 = AllTax.nandedTax.market.jewelryShop["Total tax"]
tax2 = AllTax.nandedTax.market.FruitsShop["Total tax"]
tax3 = AllTax.nandedTax.market.GroceryShop["Total tax"]


# Tax of vehical
tax4 = AllTax.nandedTax.vehicle.fourWheel["Total tax"]
tax5 = AllTax.nandedTax.vehicle.threeWhile["Total tax"]
tax6 = AllTax.nandedTax.vehicle.twoWheels["Total tax"]


# Network of market
tax7 = AllTax.nandedTax.market.jewelryShop["Total Month Income"]
tax8 = AllTax.nandedTax.market.FruitsShop["Total Month Income"]
tax9 = AllTax.nandedTax.market.GroceryShop["Total Month Income"]


# Network of vehical
tax10 = AllTax.nandedTax.vehicle.fourWheel["Total Month Income"]
tax11 = AllTax.nandedTax.vehicle.threeWhile["Total Month Income"]
tax12 = AllTax.nandedTax.vehicle.twoWheels["Total Month Income"]


natwork1 = [tax7, tax8, tax9]

network2 = [tax10, tax11, tax12]

marketTax = [tax1, tax2, tax3]

vehical = [tax4, tax5, tax6]


def totalTax():
    TotalTax = tax1+tax2+tax3+tax4+tax5+tax6
    print("The Total Tax of Of Nande Is :", TotalTax)
    print("-"*10)


def totalNetwork():
    TotalNetwork = tax7+tax8+tax9+tax10+tax11+tax12
    print("The total Network of nanded is ",TotalNetwork)
    print("-"*10)


totalNetwork()
totalTax()


print("The Network 1 Is :",natwork1)
print("-"*10)
print("The Network 2 Is :",network2)
print("-"*10)
print("The Total Tax market is :",marketTax)
print("-"*10)
print("The Total tax of vehical is :",vehical)
print("-"*10)
