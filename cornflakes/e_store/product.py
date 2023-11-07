from cornflakes.e_store.product_category import ProductCategory


class Product:
    def __int__(self):
        self.__product_id = None
        self.__product_name = None
        self.__price = 0
        self.__product_description = None
        self.__product_category = ProductCategory
