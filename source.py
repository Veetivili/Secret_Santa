
class participant:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    # override conversion from participant class to to string
    def __str__(self):
        return self.name + "(" + self.id + ")"
    
    name = ""
    id = ""

# Secret santa stores information of gift giver, gifts and gift receivers.
class secret_santa:
    def __init__(self, giver, present, receiver):
        self.giver = giver
        self.present = present
        self.receiver = receiver
    def __str__(self):
        return self.giver + self.present + self.receiver

    giver = ""
    present = ""
    receiver = ""




