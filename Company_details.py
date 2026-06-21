class Company:

    class Owner:

        def __init__(self, owner_name, share):
            self.owner_name = owner_name
            self.share = share

        def get_details(self):
            return f"{self.owner_name} - {self.share}%"

    class Employee:

        def __init__(self, employee_name, position):
            self.employee_name = employee_name
            self.position = position

        def get_details(self):
            return f"{self.employee_name} - {self.position}"

    def __init__(self, company_name, valuation):
        self.company_name = company_name
        self.valuation = valuation
        self.owners = []
        self.employees = []

    def add_owner(self, owner_name, share):
        new_owner = Company.Owner(owner_name, share)
        self.owners.append(new_owner)

    def list_owners(self):
        return [owner.get_details() for owner in self.owners]

    def add_employee(self, employee_name, position):
        new_employee = Company.Employee(employee_name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

    @staticmethod
    def check_vacancies(position):
        vacancies = [
            "software engineer",
            "accountant",
            "marketing manager",
            "project lead"
        ]
        return position.lower() in vacancies


num_companies = int(input("Enter number of companies: "))
companies = []

for company_index in range(num_companies):

    company_name = input(f"\nEnter company {company_index + 1} name: ")
    company_valuation = input("Enter company valuation: ")
    print()

    company_obj = Company(company_name, company_valuation)
    companies.append(company_obj)

    num_owners = int(input("How many owners are there? "))
    print()

    for owner_index in range(num_owners):
        owner_name = input(f"Enter owner {owner_index + 1} name: ")
        owner_share = float(input("Enter owner's share (%): "))
        print()
        company_obj.add_owner(owner_name, owner_share)

    num_employees = int(input("How many employees are there? "))
    print()

    for employee_index in range(num_employees):
        employee_name = input(f"Enter employee {employee_index + 1} name: ")
        employee_position = input("Enter employee position: ")
        print()
        company_obj.add_employee(employee_name, employee_position)

print("\nCOMPANY DETAILS")

for company in companies:
    print(f"\nCompany: {company.company_name}")
    print(f"Valuation: ${company.valuation}")

    print("\nOwners:")
    for owner in company.list_owners():
        print(owner)

    print("\nEmployees:")
    for employee in company.list_employees():
        print(employee)