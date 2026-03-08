



class Passenger:
    def __init__(self, name, passport_number, age, sex):
        self._name = name
        self._passport_number = passport_number
        self._age = age
        self._sex = sex
        
    def set_name(self, name):
        self._name = name 
    
    def get_name(self):    
        return self._name
            
    def set_passport_number(self, passport):
        self._passport_number = passport

    def get_passport_number(self):
        return self._passport_number

    def set_age(self, age):
        self._age = age
    
    def get_age(self):
        return self._age

    def set_sex(self, sex):
        self._sex = sex

    def get_sex(self):
        return self._sex

    def display_passenger(self):
        return f"Name: {self._name}, Passport number: {self._passport_number}, Age: {self._age}, Sex: {self._sex}"
        

