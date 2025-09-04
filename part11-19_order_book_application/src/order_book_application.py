from order_book import OrderBook        

class UI:
    def __init__(self):
        self.order_book = OrderBook()
    
    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
        print()

    def add_order(self):
        description = input("description: ")
        try: 
            programmer, workload = input("programmer and workload estimate: ").split(" ")
            workload = int(workload)
            self.order_book.add_order(description, programmer, workload)
            print("added!")
        except:
            print("erroneous input")

    def list_finished(self):
        if len(self.order_book.finished_orders()) != 0:
            for order in self.order_book.finished_orders():
                print(order)
        else:
            print("no finished tasks")

    def list_unfinished(self):
        if len(self.order_book.unfinished_orders()) != 0:
            for order in self.order_book.unfinished_orders():
                print(order)
        else:
            print("no unfinished tasks")

    def mark_finished(self):
        try: 
            finished = int(input("id: "))
            if self.order_book.mark_finished(finished):
                print("marked as finished")
            else:
                print("erroneous input")
        except:
            print("erroneous input")

    def list_programmers(self):
        programmers = self.order_book.programmers()
        for p in programmers:
            print(p)

    def status(self):
        programmer = input("programmer: ")
        if self.order_book.status_of_programmer(programmer) != None:
            finished, not_finished, done, scheduled = self.order_book.status_of_programmer(programmer)
            print(f"tasks: finished {finished} not finished {not_finished}, hours: done {done} scheduled {scheduled}")
        else:
            print("erroneous input")


    def execute(self):
        self.help()

        while True:
            cmd = input("command: ")
            
            if cmd == "0":
                break
            if cmd == "1":
                self.add_order()
            if cmd == "2":
                self.list_finished()
            if cmd == "3":
                self.list_unfinished()
            if cmd == "4":
                self.mark_finished()
            if cmd == "5":
                self.list_programmers()
            if cmd == "6":
                self.status()

ui = UI()
ui.execute()