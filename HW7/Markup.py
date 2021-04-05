from Product import Product


class Markup(Product):
    markup_list = [
        {
            "product_type": "1",
            "lower_cost": 10,
            "upper_cost": 20,
            "unit": "percent",
            "lower_count": 10
        },
        {
            "product_type": "2",
            "lower_cost": 15,
            "upper_cost": 20,
            "unit": "percent",
            "lower_count": 10
        },
        {
            "product_type": "3",
            "lower_cost": 10,
            "upper_cost": 15,
            "unit": "percent",
            "lower_count": 5
        },
        {
            "product_type": "4",
            "lower_cost": 10,
            "upper_cost": 30,
            "unit": "percent",
            "lower_count": 20
        },
    ]

    def __init__(self, product_type, count):
        super().__init__(product_type)
        self.count = count

    def get_markup(self):
        markup_details = dict()
        for markup in self.markup_list:
            if self.get_product_details()['type_of_products'] == markup['product_type']:
                markup_details.update(markup)
                break
        # y = mx + b
        m = (markup_details['upper_cost'] - markup_details['lower_cost']) \
            / (1 - markup_details['lower_count'])
        y_intercept = markup_details['upper_cost'] - (m * 1)
        markup = (m * self.count) + y_intercept \
            if 1 <= self.count < markup_details['lower_count'] \
            else markup_details['lower_cost']
        return markup
