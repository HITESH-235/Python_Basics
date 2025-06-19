class MenuItem:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
        Restaurant.menu.append(self)

class Restaurant:
    menu = []
    def __init__(self):
        self.orders = {}

    def show_menu_byCat(self,category):
        print(f"\n{category.capitalize()}s:")
        for item in self.menu:
            if item.category == category:
                print(f"{item.name} : {item.price}/-")
    
    def take_order(self, name, count):
        for x in self.menu:
            if x.name == name:
                self.orders[x] = self.orders.get(x,count)
                return
        print(f"{name} not available!")

    def display_bill(self):
        bill = 0
        print("\nYour Order:")
        for x, count in self.orders.items():
            bill+= x.price*count
            print(f"{count}x {x.name} : {(x.price)*count}")
        print(f"Total amount: {bill}/-")

Rest = Restaurant()
i1 = MenuItem("A1",50,'starter')
i2 = MenuItem("A2",53,'starter')
i3 = MenuItem("A3",54,'starter')
i4 = MenuItem("A4",55,'starter')
i5 = MenuItem("B1",60,'maincourse')
i6 = MenuItem("B2",63,'maincourse')
i7 = MenuItem("B3",66,'maincourse')
i8 = MenuItem("B4",69,'maincourse')
i9 = MenuItem("B5",60,'maincourse')
i10 = MenuItem("C1",22,'dessert')
i11 = MenuItem("C2",25,'dessert')
i12 = MenuItem("C3",29,'dessert')

Rest.show_menu_byCat('starter')
Rest.show_menu_byCat('maincourse')
Rest.show_menu_byCat('dessert')

# Rest.take_order([('C3',2),('A1',3),('A2',2),('B5',3)])
Rest.take_order('C3',2)
Rest.take_order('A3',3)
Rest.take_order('B2',4)

Rest.display_bill()
