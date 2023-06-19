class User:
  def __init__(self, name, password):
    self.name = name
    self.password = password
    self.amount = 0
    self.id = None
    self.history = []

class Admin_account:
  def __init__(self, email, password):
    self.email = email
    self.password = password
    self.id = None


class AB_Bank:
  def __init__(self, name):
    self.total_customer = {}
    self.admin = {}
    self.name = name
    self.total_bank_amount = 0
    self.total_loan_amount = 0
    self.loan_feauture = False
  
  def user_create_account(self, user_email, user_password):
    user = User(user_email, user_password)
    serial_id = f'{self.name}-{len(self.total_customer) + 1}'
    user.id = serial_id
    self.total_customer[serial_id] = user

  def admin_create_account(self, email, password):
    admin = Admin_account(email, password)
    serial_id = f'{self.name}_admin-{len(self.admin) + 1}'
    self.admin[serial_id] = admin




class user_account:
  def __init__(self, bank):
    self.bank = bank
  
  def deposit(self, user_id, amount):
    if user_id in bank.total_customer.keys():
      bank.total_customer[user_id].amount += amount
      bank.total_bank_amount += amount
      his = f'{(" "*10)}Deposit amount: {amount}'
      bank.total_customer[user_id].history.append(his)
      print("-------------SuccessFully Done Deposit-----------\n")
  
  def withdraw(self, user_id, amount):
    if user_id in bank.total_customer.keys():
      if bank.total_bank_amount < amount and amount <= bank.total_customer[user_id].amount:
        print("-----------Bank is bankrupt----------\n")
      elif amount > bank.total_customer[user_id].amount:
        print(f'--------Your account not enough money. You can withdraw {bank.total_customer[user_id].amount}tk--------\n')
      elif amount <= bank.total_customer[user_id].amount:
        bank.total_customer[user_id].amount -= amount
        bank.total_bank_amount -= amount
        his = f'{(" "*10)}Withdraw amount: {amount}'
        bank.total_customer[user_id].history.append(his)
        print("-----------SuccessFully Done Withdraw---------\n")

  def check_available_balance(self, user_id):
    if user_id in bank.total_customer.keys():
      print(f'-----------Your bank account total available Balance: {bank.total_customer[user_id].amount}-----------\n')
  
  def transfer_money_another_account(self, transfer_account_id, transfer_money, user_id):
    if user_id in bank.total_customer.keys():
      if bank.total_customer[user_id].amount < transfer_money:
        print(f'-----------My account not enough money. I tranfer money {bank.total_customer[user_id].amount}----------\n')
      
      elif bank.total_customer[user_id].amount >= transfer_money:
        if transfer_account_id in bank.total_customer.keys():
          bank.total_customer[transfer_account_id].amount += transfer_money
          bank.total_customer[user_id].amount -=transfer_money
          his = f'{(" "*10)}Transfer amount: {transfer_money}'
          bank.total_customer[user_id].history.append(his)
          his_1 = f'{(" "*10)}Recived money with {bank.total_customer[user_id].name} amount: {transfer_money}'
          bank.total_customer[transfer_account_id].history.append(his_1)
          print("-------------Successfully done Transfer amount-----------\n")

  def check_history(self, user_id):
    if user_id in bank.total_customer.keys():
      print(f"-----------{bank.total_customer[user_id].name} History-------------\n")
      for i in bank.total_customer[user_id].history:
        print(i)
      print()

  def loan_user(self, user_id, amount):
    if bank.loan_feauture == False:
      print("-------------Loan feauture OFF-------------\n")
    else:
      total_loan_cus = bank.total_customer[user_id].amount*2
      if amount > bank.total_bank_amount:
        print("---------Bank fokira. Not Enough money you want---------\n")
      else:
        print(f'----------You can withdraw loan {total_loan_cus}--------\n')
        his = f'{(" "*10)}Loan amount: {amount}'
        bank.total_loan_amount += amount
        bank.total_bank_amount -= amount
        bank.total_customer[user_id].history.append(his)
        print("-----------SuccessFully Done loan-----------\n")
      
class Admin:
  def __init__(self, bank):
    self.bank = bank

  def check_total_bank_balance(self, admin_id):
    if admin_id in bank.admin.keys():
      print(f'-------------Total available Bank Balance: {bank.total_bank_amount}-----------\n')
  
  def check_total_loan_amount(self, admin_id):
    if admin_id in bank.admin.keys():
      print(f'----------Total loan amount: {bank.total_loan_amount}---------\n')
  
  def on_off_loan_feauture(self, admin_id):
    if admin_id in bank.admin.keys():
      if bank.total_bank_amount > 1:
        bank.loan_feauture = True
        print("---------Loan Feauture ON---------\n")
      else:
        bank.loan_feauture = False
        print("--------Loan Feauture OFF-------\n")



bank = AB_Bank('AB')
#1. Create account User:
bank.user_create_account('abdul', 123)
bank.user_create_account('kaosar', 523)

#2. Deposit And withdrawal Amount User:
user = user_account(bank)
# print Deposit 
user.deposit('AB-1', 3000)
user.deposit('AB-1', 5000)
user.deposit('AB-2', 20000)
# print Withdraw
user.withdraw('AB-1', 2000)
user.withdraw('AB-2', 50000)

#3. Check Available Balance:
user.check_available_balance('AB-1')
user.check_available_balance('AB-2')

#4. Transfer money another account:
user.transfer_money_another_account('AB-2', 8000, 'AB-1')
user.transfer_money_another_account('AB-1', 5000, 'AB-2')

#5. Check Transaction History:
user.check_history('AB-1')

user.check_history('AB-2')

#6. Loan Amount:
user.loan_user('AB-1', 1000)
user.loan_user('AB-2', 1000)

## Admin
# 1. Create admin Account:
bank.admin_create_account('ad@gmail.com', 12)

#2. Check Total Balance of the Bank:
admin = Admin(bank)
admin.check_total_bank_balance('AB_admin-1')

#3. Check Total Loan Amount:
admin.check_total_loan_amount('AB_admin-1')

#4. Loan feature on or off:
admin.on_off_loan_feauture('AB_admin-1')

###### Check Bank is bankrupt
user.loan_user('AB-2', 26000)
admin.check_total_bank_balance('AB_admin-1')
user.withdraw('AB-1', 1000)



