from inventory import Inventory
from interface import Interface

def main():
    inventory = Inventory()
    interface = Interface(inventory)
    interface.run()

if __name__ == "__main__":
    main()
