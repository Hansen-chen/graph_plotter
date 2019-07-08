class backtester:

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        backtester.empCount += 1

    def displayCount(self):
        print
        "Total Employee %d" % backtester.empCount

    def displayEmployee(self):
        print
        "Name : ", self.name, ", Salary: ", self.salary