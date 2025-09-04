class Task:
    id_counter = 0
    def __init__(self, description: str, programmer: str, hours: int):
        self.description = description
        self.programmer = programmer
        self.workload = hours
        self.finished = False
        Task.id_counter += 1
        self.id = Task.id_counter
    
    def __str__(self):
        if self.finished:
            str_fin = "FINISHED"
        else:
            str_fin = "NOT FINISHED"

        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {str_fin}"

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

class OrderBook:
    def __init__(self):
        self.orders = []
        self.programmers_list = []
        self.id_list = []
    
    def add_order(self, description, programmer, hours):
        new_order = Task(description, programmer, hours)
        self.orders.append(new_order)

        if programmer not in self.programmers_list:
            self.programmers_list.append(programmer)

        self.id_list.append(new_order.id)
        

    def all_orders(self):
        return self.orders
    
    def programmers(self):
        return self.programmers_list

    def mark_finished(self, id):
        if id in self.id_list:
            for order in self.orders:
                if order.id == id:
                    order.mark_finished()
                    return True
        else:
            return False

    def finished_orders(self):
        finished = []
        for order in self.orders:
            if order.is_finished():
                finished.append(order)
        return finished
    
    def unfinished_orders(self):
        unfinished = []
        for order in self.orders:
            if not order.is_finished():
                unfinished.append(order)
        return unfinished

    def status_of_programmer(self, programmer: str):
        if programmer in self.programmers_list:
            finished = [order for order in self.finished_orders() if order.programmer == programmer]
            unfinished = [order for order in self.unfinished_orders() if order.programmer == programmer]

            return(
                len(finished),
                len(unfinished),
                sum(order.workload for order in finished),
                sum(order.workload for order in unfinished)
            )
        else:
            return None