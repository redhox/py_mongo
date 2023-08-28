from conection import MongoAccess
from data import Element
import pprint


def main() :
    MongoAccess.connexion()

    pprint.pprint(MongoAccess.get_element("Rogue"))

    nouveau = Element({"nom":"Rubeus", "prénom":"Agrid"})
    nouveau.set_titre("Gardien des clés et des lieux")

    MongoAccess.set_element(nouveau)

    tous = MongoAccess.get_elements()

    for element in tous :
        pprint.pprint(element)

    MongoAccess.deconnexion()

if __name__ == "__main__":
    main()