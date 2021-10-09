from store import Store

market = Store("Bargain Market")
market.add_product("Eggs")
market.add_product("Steak")
market.add_product("Pork Chop")
market.sell_product(1)
# market.products[0].print_info()
market.inflation(.2)
market.clearance(.2, "Butcher")