from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:
    LOAN_TYPES = {'StudentLoan': StudentLoan, 'MortgageLoan': MortgageLoan}
    CLIENTS_TYPES = {'Student': Student, 'Adult': Adult}

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        new_loan = self.LOAN_TYPES[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type, client_name, client_id, income):
        if client_type not in self.CLIENTS_TYPES:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return f"Not enough bank capacity."

        new_client = self.CLIENTS_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):
        loan = self._get_loan(loan_type)
        client = self._get_client(client_id)

        if not (
            (loan.__class__.__name__ == 'StudentLoan' and client.__class__.__name__ == 'Student') or
            (loan.__class__.__name__ == 'MortgageLoan' and client.__class__.__name__ == 'Adult')
        ):
            raise Exception("Inappropriate loan type!")

        client.loans.append(loan)
        self.loans.remove(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id):
        client = self._get_client(client_id)

        if client is None:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):
        counter = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                counter += 1
                loan.increase_interest_rate()

        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate):
        counter = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_client_interest()
                counter += 1

        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        result = f"Active Clients: {len(self.clients)}\n"

        total_income = sum([c.income for c in self.clients])
        result += f"Total Income: {total_income:.2f}\n"

        loans_count = sum([len(c.loans) for c in self.clients])
        loans_sum = sum([sum([l.amount for l in c.loans]) for c in self.clients if c.loans])
        result += f"Granted Loans: {loans_count}, Total Sum: {loans_sum:.2f}\n"

        not_granted_loans = len(self.loans)
        not_granted_loans_sum = sum([l.amount for l in self.loans])
        result += f"Available Loans: {not_granted_loans}, Total Sum: {not_granted_loans_sum:.2f}\n"

        total_interest_rate = sum([c.interest for c in self.clients])
        average_rate = 0
        if len(self.clients) != 0:
            average_rate = total_interest_rate / len(self.clients)

        result += f"Average Client Interest Rate: {average_rate:.2f}"
        return result

    def _get_loan(self, loan_type):
        loan = [l for l in self.loans if l.__class__.__name__ == loan_type]
        return loan[0] if loan else None

    def _get_client(self, client_id):
        client = [c for c in self.clients if c.client_id == client_id]
        return client[0] if client else None
