class Product:
    product_list = [
        {
            "type_of_products": "1",
            "name": "shirt",
            "price": 30,
            "unit": "Dollar",
            "commission_groups": ["A", "B"]
        },
        {
            "type_of_products": "2",
            "name": "pants",
            "price": 50,
            "unit": "Dollar",
            "commission_groups": ["A", "C"]
        },
        {
            "type_of_products": "3",
            "name": "shoes",
            "price": 80,
            "unit": "Dollar",
            "commission_groups": ["B"]
        },
        {
            "type_of_products": "4",
            "name": "hat",
            "price": 20,
            "unit": "Dollar",
            "commission_groups": []
        }
    ]

    def __init__(self, product_type):
        self.product_type = product_type

    def get_product_details(self):
        for product in self.product_list:
            if product["type_of_products"] == self.product_type:
                self.details = product
            else:
                continue
        return self.details

    def get_name(self):
        return self.details['name']

    def get_type_of_products(self):
        return self.details['type_of_products']

    def get_price(self):
        return self.details['price']

    def get_unit(self):
        return self.details['unit']

    def get_commission_groups(self):
        return self.details['commission_groups']
