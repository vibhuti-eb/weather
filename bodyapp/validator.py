import re

class Validator:

    def cityParamValidator(cityName):
        if cityName == None or len(cityName) == 0 or len(cityName) == 1 :
            return True   

        city_regex = re.compile(r"^(?=[a-zA-Z0-9\s\.\-\'].*[a-zA-Z])[a-zA-Z0-9\s\.\-\']{1,100}$", re.IGNORECASE)
        
        if city_regex.search(cityName):
            print("Valid City name")
            return False
        
        print("Invalid City name")
        return True
