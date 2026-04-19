class CustomerManager:
    def __init__(self):
        self.customers = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.discount_threshold = 500

    def add_customer(self, name, purchases):
        if name in self.customers.keys():
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchase(self, name, purchase):
        self.add_customer(name, [purchase])

    def add_purchases(self, name, purchases):
        self.add_customer(name, purchases)

    def generate_report(self):
        for y, x in self.customers.items():
            a = 0
            for z in x:
                if z['price'] > self.tax_threshold:
                    taxed_price = z['price'] * (1 + self.tax_rate)
                    a += taxed_price
                else:
                    a += z['price']
            print(y)
            if a > self.discount_threshold:
                print("Eligible for discount")
            else:
                if a > 300:
                    print("Potential future discount customer")
                else:
                    print("No discount")
            if a > 1000:
                print("VIP Customer!")
            else:
                if a > 800:
                    print("Priority Customer")

    def calculate_shipping_fee(self, purchases):
        heavy_item = False
        for purchase in purchases:
            if purchase.get('weight', 0) > 20:
                heavy_item = True
                break
        if heavy_item:
            return 50
        else:
            return 20

def calculate_shipping_fee_for_heavy_items(purchases):
    for purchase in purchases:
        if purchase.get('weight', 0) > 20:
            return 50
    return 20

def calculate_shipping_fee_for_fragile_items(purchases):
    fragile_item = False
    for purchase in purchases:
        if purchase.get('fragile', False):
            fragile_item = True
            break
    if fragile_item:
        return 60
    else:
        return 25

flat_tax = 0.2