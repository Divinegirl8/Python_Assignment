class Generator:
    def __init__(self):
        self.__response_1 = 'Very good!'
        self.__response_2 = 'Nice work!'
        self.__response_3 = 'Keep up the good work!'

    def get_response_1(self):
        return self.__response_1

    def get_response_2(self):
        return self.__response_2

    def get_response_3(self):
        return self.__response_3

    def generate_response(self, number):
        result = ""
        match number:
            case 1: result = self.get_response_1()
            case 2: result = self.get_response_2()
            case 3: result = self.get_response_3()
        return result


if __name__ == "__main__":
    response = Generator()
    value = response.generate_response(2)
    print(value)



