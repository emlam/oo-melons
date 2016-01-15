

class AbstractMelonOrder(object):
    """ You fill in the rest """
    
    def __init__(self, species, qty, order_type, tax, country_code = None):
        """Initializing a melon order"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.base_price = 5
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code
        

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total



class DomesticMelonOrder(AbstractMelonOrder):
    """ You fill in the rest """

    def __init__(self, species, qty):
        super(DomesticMelonOrder,self).__init__(species,qty, "domestic", .08)


class InternationalMelonOrder(AbstractMelonOrder):
    """ You fill in the rest """   

        
    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder,self).__init__(species, qty, "international", .17, country_code)
        

    def get_country_code(self):
        """Return the country code."""
        return self.country_code