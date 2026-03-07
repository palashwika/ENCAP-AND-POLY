#Class 1
class India():
    def capital(self):
        print("New Delhi is the capital of INdia")

    def language(self):
        print("Hindi is the language of India")

    def type(self):
        print("India is a developing country")

#Class 2
class USA():
    def capital(self):
        print("Washington D.C. is capital of USA")

    def language(self):
        print("English is lang. of USA")
    
    def type(self):
        print("USA is a developed country")\

#Common interface
obj_ind=India()
obj_usa=USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language
    country.type()
