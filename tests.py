from models.client import Client
from models.account import Account


joao: Client = Client('Nyasha', 'nyashakarata35@gmail.com', '123456', '16/12/2003')
jennifer: Client = Client('Rockstar', 'rock3@gmail.com', '654321', '05/08/2003')

accountA: Account = Account(Nyasha)
accountB: Account = Account(Rockstar)

print(accountA)
print(accountB)
