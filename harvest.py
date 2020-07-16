############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller 
        self.name = name

        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code #overriding

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    #order = code, name, first_harvest, color, is_seedless, is_bestseller

    musk = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    cas.add_pairing('strawberries', 'mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)


    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print(f'-{pairing}')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    
    melons_by_id = {}
    #keys are codes as strings 
    #values are melon type instance 

    for melon in melon_types: 
        if melon.code not in melons_by_id: 
            melons_by_id[melon.code] = melon
    return melons_by_id

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field_harvest, michael_harvest):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_harvest = field_harvest
        self.michael_harvest = michael_harvest

    def is_sellable(self):
        if self.shape_rating >= 5 and self.color_rating >= 5 and self.field_harvest != 3:
            return True 
        else: 
            return False 

    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []
    melons_by_id = make_melon_type_lookup(melon_types)


    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melons.extend(melon1, melon_2, melon_3, melon_4, 
        melon_5, melon_6, melon_7, mleon_8, melon_9)

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 




















