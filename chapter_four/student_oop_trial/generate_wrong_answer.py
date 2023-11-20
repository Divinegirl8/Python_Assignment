class Generator2:
    def __init__(self):
        self.__response1 = 'No. Please try again.'
        self.__response2 = 'Wrong. Try once more.'
        self.__response3 = 'No. Keep trying.'

    def get_response1(self):
        return self.__response1

    def get_response2(self):
        return self.__response2

    def get_response3(self):
        return self.__response3

    def generate_response(self, number):
        result = ""
        match number:
            case 1 : result = self.__response1
            case 2: result = self.__response2
            case 3: result = self.__response3
        return result

