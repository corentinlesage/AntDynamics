class Supply:
    """
    Supply is a consumable for Animal to survive

    element : Element
    quantity : positive real number
    type : -1 water or 1 food
    """
    element = None
    quantity = None
    type = None

    def __init__(self, element, quantity, type):
        """
        Constructor
        """
        self.element = element

        if element is not None:
            self.element.list_supply.append(self)

        self.quantity = quantity
        self.type = type

    def __delete__(self):
        """
        Destructor
        """
        if self.element is not None:
            self.element.list_supply.remove(self)

    def decomposition(self):
        "Food decay over time"
        if self.type == 1:
            self.quantity -= 0.01

            if self.quantity <= 0:
                del self

    def post(self):
        """
        Print of a Supply
        """
        self.element.post()

        temp = ""

        if self.type == -1:
            temp = "Water"
        else:
            temp = "Food"

        print(temp, ":  ", self.quantity)
