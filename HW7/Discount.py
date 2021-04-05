from Markup import Markup


class Discount(Markup):
    discount_list = [
        {
            "group_name": "A",
            "cost": 5,
            "unit": "percent",
            "users": [1001, 1002, 1003, 1005]
        },
        {
            "group_name": "B",
            "cost": 3,
            "unit": "Dollar",
            "users": [1001, 1003, 1006]
        },
        {
            "group_name": "C",
            "cost": 7,
            "unit": "percent",
            "users": [1001, 1002, 1004]
        }
    ]

    def __init__(self, product_type, count, userid=None):
        super().__init__(product_type, count)
        self.userid = userid

    def get_discount(self):
        self.get_product_details()
        self.total_price = (self.count * self.get_price()) + (
                (self.get_markup() / 100) * (self.count * self.get_price()))
        self.list_of_discount = list()
        for discount in self.discount_list:
            if discount["group_name"] in self.get_commission_groups() and self.userid in discount["users"] and discount[
                    "unit"] == "percent":
                self.list_of_discount.append(self.total_price * (discount["cost"] / 100))
                continue
            if discount["group_name"] in self.get_commission_groups() and self.userid in discount["users"] and discount[
                    "unit"] == "Dollar":
                self.list_of_discount.append((discount["cost"] * self.count))
                continue
            continue
        if len(self.list_of_discount) != 0:
            self.discount = min(self.list_of_discount)
        else:
            self.discount = 0
        self.total_with_discount = self.total_price - self.discount
        return self.discount
