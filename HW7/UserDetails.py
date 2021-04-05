from Product import Product


class UserDetails(Product):
    user_list = [
        {
            "userid": 1001,
            "first_name": "Mohsen",
            "last_name": "Bayat",
        },
        {
            "userid": 1002,
            "first_name": "Sobhan",
            "last_name": "Taghadosi",
        },
        {
            "userid": 1003,
            "first_name": "Javad",
            "last_name": "Jafari",
        },
        {
            "userid": 1004,
            "first_name": "Masoud",
            "last_name": "Hosseini",
        },
        {
            "userid": 1005,
            "first_name": "Hassan",
            "last_name": "Zand",
        },
        {
            "userid": 1006,
            "first_name": "Ali",
            "last_name": "Ebadi",
        }
    ]

    def __init__(self, product_type, userid=None):
        super().__init__(product_type)
        self.userid = userid

    def get_user_details(self):
        self.user_details = {'first_name': '', 'last_name': ''} if self.userid is None else None
        for details in self.user_list:
            if details["userid"] == self.userid:
                details.pop("userid")
                self.user_details = details

        return self.user_details
