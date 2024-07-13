# Write your solution here
class OrderBookApplication:
    def __init__(self):
        self.order_book = OrderBook()

    @staticmethod
    def instructions():
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
    
    def run(self):
        OrderBookApplication.instructions()

        while True:
            command = int(input("command: "))
            if command == 0:
                break
            if command == 1:
                self.add_order()
            if command == 2:
                self.list_finished_tasks()
            if command == 3
                self.list_unfinished_tasks()
            if command == 4:
                self.mark_task_finished()
            if command == 5:
                self.programmers()
            if command == 6:
                self.status_of_programmer()
    
    def add_order(self):
        try: 
            description = input("description: ")
            programmer, workload = OrderBookApplication.validate_order(input("programmer and workload estimate: ").split())
        except ValueError:
            print("erroneous input")
        else:
            self.order_book.add_order(description, programmer, workload)
            print("added!")

    @staticmethod
    def validate_order(*args):
            try:
                if len(args) != 2:
                    raise ValueError()
                args = list(args)
                args[1] = int(args[1])
            except:
                raise ValueError()
            else:
                return args[0], args[1]      

    def list_finished_tasks(self):
        finished = self.order_book.finished_orders()
        if finished:
            for task in finished:
                print(task)
            return
        print("no finished tasks")
    
    def list_unfinished_tasks(self):
        unfinished = self.order_book.unfinished_orders()
        if unfinished:
            for task in unfinished:
                print(task)
            return
        print("no unfinished task")
    
    def mark_task_finished(self):
        id = int(input("id: "))
        self.order_book.mark_finished(id)
        print("marked as finished")
    
    def programmers(self):
        for programmer in self.order_book.programmers():
            print(programmer)
    
    def status_of_programmer(self):
        programmer = input("programmer")
        finished, unfinished, work_f, work_u = self.order_book.status_of_programmer(programmer)
        print(f"tasks: finished {finished} not finished {unfinished}, hours: done {work_f} scheduled {work_u}")

    

# If you use the classes made in the previous exercise, copy them here
class Task:
    counter = 1

    def __init__(self, description: str, programmer: str, workload: int = 0):
        self.__description = description
        self.__workload = workload
        self.__programmer = programmer
        self.__finished = False
        self.id = Task.counter
        Task.counter += 1
    
    @property
    def description(self):
        return self.__description

    @property
    def programmer(self):
        return self.__programmer

    @property
    def workload(self):
        return self.__workload

    def is_finished(self):
        return self.__finished
    
    def mark_finished(self):
        self.__finished = True
    
    def __str__(self):
        return f"{self.id}: {self.__description} ({self.__workload} hours), programmer {self.__programmer} {'FINISHED' if self.__finished else 'NOT FINISHED'}"


class OrderBook:
    def __init__(self):
        self.task_list = []
    
    def add_order(self, description, programmer, workload):
        self.task_list.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.task_list
    
    def programmers(self):
        return list({task.programmer for task in self.task_list})
    
    def mark_finished(self, id: int):
        for task in self.task_list:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError("Task with given id not found")

    def finished_orders(self):
        return [task for task in self.task_list if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.task_list if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        finished = [task.workload for task in self.finished_orders() if task.programmer == programmer]
        unfinished = [task.workload for task in self.unfinished_orders() if task.programmer == programmer]
        if not (finished or unfinished):
            raise ValueError()
        return (len(finished), len(unfinished), sum(finished), sum(unfinished))

