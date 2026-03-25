class Office:
    employeesNum = 0

    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
        Office.employeesNum += len(self.employees)

    
    def get_all_employees(self):
        return self.employees.copy()

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        for i, emp in enumerate(self.employees):
            if emp.id == empId:
                del self.employees[i]
                Office.employeesNum -= 1
                return True
        return False
    
    def check_latenes (self, empId, moveHour, targetHour=9):
        emp = self.get_employee(empId)
        if emp is None:
            return None
        
        velocity = emp.car.velocity
        if velocity <= 0:
            return True
        
        is_late = Office.calculate_lateness(
            targetHour=targetHour,
            moveHour=moveHour,
            distance=emp.distanceToWork,
            velocity=velocity
        )

        if is_late:
            self.deduct(empId, 10)
        else:
            self.reward(empId, 10)

        return is_late

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity <= 0:
            return True

        arrival_time = moveHour + (distance / velocity)
        return arrival_time > targetHour

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp is None:
            return None
        emp.salary = max(0, emp.salary - deduction)
        return emp.salary

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp is None:
            return None
        emp.salary += reward
        return emp.salary

    @classmethod
    def change_emps_num(cls, num):
        if num < 0:
            raise ValueError("Number of employees cannot be negative")
        cls.employeesNum = num
