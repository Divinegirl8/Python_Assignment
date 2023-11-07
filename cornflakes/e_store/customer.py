
from cornflakes.e_store.billing_information import BillingInformation
from cornflakes.e_store.shopping_cart import ShoppingCart
from cornflakes.e_store.users import User


class Customers(User):
    def __int__(self):
        super().__int__()
        self.__billing_information = BillingInformation
        self.__shopping_cart = ShoppingCart
