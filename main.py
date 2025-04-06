import csv

class Transaction:
    def __init__(self, id, type, amount):
        self.id = id
        self.type = type
        self.amount = amount

#-----------------------------------------------------------------------

class Bank:
    def __init__(self):
        self.transactions = []

#-----------------------------------------------------------------------

    def read_data(self, filename):
        with open(filename, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transaction = Transaction(row["id"], row["tipo"], float(row["monto"]))
                self.transactions.append(transaction)
    
    def final_balance(self):
        debit = 0
        credit = 0

        for transaction in self.transactions:
            if transaction.type == "Débito":
                debit += transaction.amount

            elif transaction.type == "Crédito":
                credit += transaction.amount

        return round(credit - debit, 2)

    def highest_transaction(self):
        max_object = max(self.transactions, key=lambda x: x.amount)

        return f'ID {max_object.id} - {round(max_object.amount, 2)}'

    def trasaction_count(self):
        debit_count = 0
        credit_count = 0

        for transaction in self.transactions:
            if transaction.type == "Débito":
                debit_count += 1

            elif transaction.type == "Crédito":
                credit_count += 1 

        return f'Crédito: {credit_count} Débito: {debit_count}'

#-----------------------------------------------------------------------

if __name__ == "__main__":
    bank = Bank()
    bank.read_data("data.csv")

    report = f"""
    Reporte de Transacciones           
    ------------------------------------------------------
    Balance Final:               {bank.final_balance():.2f}
    Transacción de mayor monto:  {bank.highest_transaction()}
    Conteo de Transacciones:     {bank.trasaction_count()}
    """
    print(report)

    
