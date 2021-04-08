from Discount import Discount
from UserDetails import UserDetails


class FinalResult(Discount):

    def __init__(self, product_type, count, userid=None):
        super().__init__(product_type, count, userid)

    def get_result(self):
        self.get_product_details()
        self.get_discount()
        self.user_info = UserDetails(self.get_type_of_products(), self.userid)
        return {'product_name': self.get_name(),
                'total_price': self.total_price,
                'total_with_commission': self.total_with_discount,
                'discount': self.discount,
                'username': self.user_info.get_user_details()}

    def __str__(self):
        return f"markup : {self.get_markup()} percent\n" + str(self.get_result())


d = FinalResult("3", 10, 1006)
print(d)
