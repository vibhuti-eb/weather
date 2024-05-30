import re

class Validator:

    def cityParamValidator(cityName):
        city_regex = re.compile(r"^[a-zA-Z0-9\s\.\-\']{1,100}$", re.IGNORECASE)
        
        if city_regex.search(cityName):
            print("Valid City name")
            return False
        
        print("Invalid City name")
        return True
