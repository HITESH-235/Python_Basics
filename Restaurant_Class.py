# Create a MenuItem class with name, price, category. Create a Restaurant class that: Has a list,lets users view menu by category, place an order and displays total bill.

class Restaurant:
    lst = []
    def __init__(self):
        return
      
    def show_menu(self):
        n = 1
        for x in self.lst:
            print(f"Item.{n}: {x.name}, price:{x.price}, category:{x.category}")
            n+=1

    @staticmethod
    def fn(category):
        n = 1
        print(category+"s :")
        for x in Restaurant.lst:
            if x.category == category:
                print(f"{n}.{x.name}, Price:{x.price}")
                n+=1

    def show_categories(self):
        return self.fn("starter"),self.fn("maincourse"),self.fn("dessert")
    
    def Take_order(self,order):
        bill = 0
        print("Your Order:")
        for name,count in order.items():
            for x in self.lst:
                if x.name == name:
                    bill+=(x.price)*count
                    print(f"{count}x {x.name} : -/{(x.price)*count}")
        print(f"Total amount: -/{bill}")

class MenuItem():
    def __init__(self,name,price,category): #starter/maincourse/dessert
        self.name = name
        self.price = price
        self.category = category
        Restaurant.lst.append(self)

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

# Rest.show_menu()
Rest.show_categories()
Rest.Take_order({'C3':2, 'A1':3, "A4":4, "B2":2, "B5":5})
