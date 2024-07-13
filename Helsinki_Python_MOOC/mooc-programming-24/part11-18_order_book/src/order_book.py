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
