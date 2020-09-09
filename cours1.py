class Stylo:
    """ docstring for Stylo
    ink_color = String
    cap = Boolean
    head = feather or ball
    """
    def __init__(self, ink_color, cap, head):
        self.ink_color = ink_color
        self.cap = cap
        self.head = head

    def __str__(self):
        if self.cap == True:
            cap = " avec un bouchon "
        else:
            cap = " sans bouchon "
        return "je suis un stylo " + str(self.head) + " de couleur " + str(self.ink_color) + str(cap)
    
s1 = Stylo("bleue", True, "bille")
s2 = Stylo("noire", False, "plume")
print(s1)
print(s2)

