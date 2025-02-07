import re


class CreditCard(object):
    """A CreditCard represents a credit card.

    There's some sweet logic in here to make sure that the type of card
    you passed is valid. 
    """
    def __init__(self, number='', expiration='', cvv='', zip=''):
        self.name = ''
        self.number = str(number).strip()
        self.card_type = self.find_type()
        self.expiration = str(expiration).strip()
        self.cvv = str(cvv).strip()
        self.zip = str(zip).strip()
        if not self.validate():
            raise Exception("Invalid Card.")

    def __repr__(self):
        return "Credit Card with last four #{}".format(self.number[-4:])

    def validate(self):
        is_valid = self.number.isdigit() and len(self.number) == 16 and self.card_type != "" and len(self.expiration) == 4 and self.expiration.isdigit()
        is_valid &= len(self.cvv) == 3 and self.cvv.isdigit()
        is_valid &= 5 <= len(self.zip) >= 6
        return is_valid

    def find_type(self):
        patterns = {'VISA': r'^4[0-9]{12}(?:[0-9]{3})?$',
                    'MASTERCARD': r'^5[1-5][0-9]{14}$',
                    'AMEX': r'^3[47][0-9]{13}$',
                    'DINERS': r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
                    'DISCOVER': r'^6(?:011|5[0-9]{2})[0-9]{12}$',
                    'JCB': r'^(?:2131|1800|35\d{3})\d{11}$',
                    'ENROUTE': r'^(?:2014|2149)\d{11}$'}
        return next((card_type for card_type, pattern in list(patterns.items())
                     if re.match(pattern, self.number)), '')