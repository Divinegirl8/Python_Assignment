from cornflakes.e_store.card_type import CardType


class CreditCardInformation:
    def __int__(self):
        self.__card_cvv = 0
        self.__card_expiration_year = 0
        self.__card_expiration_month = 0
        self.__credit_card_number = 0
        self.__name_on_card = None
        self.__card_type = CardType
