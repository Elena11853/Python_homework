class User:
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def sayfirst_last_name(self):
        print('Моё имя и фамилия: ', self.first_name, self.last_name)
    def sayfirst_name(self):
        print('Моё имя: ', self.first_name )
    def saylast_name(self):
        print('Моя фамилия: ', self.last_name)