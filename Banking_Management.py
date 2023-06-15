class User:
  def __init__(self, name, password, amount,history):
    self.history = history
    self.name = name
    self.password = password
    self.amount = amount
  


class Admin:
  def __init__(self,name, password):
    self.name = name
    self.password = password
    


class AB_Bank:
  def __init__(self, name):
    self.total_customer = []
    self.admin = []
    self.name = name
    self.total_bank_amount = 0
    self.total_loan_amount = 0
    self.loan_feauture = False
  
  # Account Create Customer 
  def customer_account(self):
    email = input("Enter Your email: ")
    password = input("Enter Your Password: ")
    amount = 0
    history = []
    print(f"\n{('*'*50)}\n{(' '*10)} Account Successfully Created... \n{('*'*50)}")

    self.customer = User(email, password, amount, history)
    self.total_customer.append(vars(self.customer))


 # Customer Deposit Amount 
  def deposit(self, amount):
    email = input("Enter your Eamil: ")
    password = input("Enter your password: ")
    for i in self.total_customer:
      if i['name'] == email and i['password'] == password:
        i['amount'] = i['amount'] + amount
        his = f'You are deposit amount: {amount}'
        i['history'].append(his)
        print(f"{('*'*50)}\n {(' '*10)}Successfully deposit your amount..\n{('*'*50)}")
        self.total_bank_amount += amount

  # Customer Withdraw Amount 
  def withdraw(self, amount):
    email = input("Enter your Eamil: ")
    password = input("Enter your password: ")
    
    for i in self.total_customer:
      if i['name'] == email and i['password'] == password:
        if self.total_bank_amount == 0:
          print(f"{('*'*50)}\n {(' '*10)}BRANK is Fokira.\n{('*'*50)}")
        elif i['amount'] >= amount:
          print(f"{('*'*50)}\n {(' '*10)}Your are successfully done withdraw amount...\n{('*'*50)}")
          his = f'You are withdraw amount: {amount}'
          i['history'].append(his)
          self.total_bank_amount -= amount
          i['amount'] = i['amount'] - amount
        else:
          print(f"{('*'*50)}\n {(' '*10)}Your account not enough money...\n{('*'*50)}")
  
  # Customer Bank Balance Check
  def available_balance(self):
    email = input("Enter your Eamil: ")
    password = input("Enter your password: ")
    for i in self.total_customer:
      if i['name'] == email and i['password'] == password:
        print(f'{("*"*50)}\n {(" "*10)}Total available Balance: {i["amount"]}\n{("*"*50)}')
  
  # Customer Can Transfer money another Account
  def Transfer_amount(self):
    name = input("Enter Transfer Account Email: ")
    for i in self.total_customer:
      if i['name'] == name: 
        email = input("Enter your email: ")
        password = input("Enter your Password: ")
        amount = int(input("Enter Transfer Amount: "))
        for j in self.total_customer:
          if j['name'] == email and j['password'] == password:
            print("some thing")
            if amount <= j['amount']:
              j['amount'] = j['amount'] - amount
              his1 = f'Transfer money with Account email {i["name"]} tk {amount}.'
              j['history'].append(his1)
              i['amount'] = i['amount'] + amount
              his2 = f'Received money with account email {j["name"]} tk {amount}'
              i['history'].append(his2)
              print(f"{('*'*50)}\n {(' '*10)} Successfully transfer money..\n{('*'*50)}")
            else:
              print(f"{('*'*50)}\n {(' '*10)}Not enough money your accout..\n{('*'*50)}")
         
  # Customer Transaction History
  def History(self):
    email = input("Enter your Email: ")
    password = input("Enter your password: ")
    print(f"{('*'*50)}")
    for i in self.total_customer:
      if i['name'] == email and i['password'] == password:
        for k in i['history']:
          print(f"{(' '*10)}", k)
    print(f"{('*'*50)}")  

  # Customer can withdraw a loan
  def user_loan(self):
    if self.loan_feauture == False:
      print(f"{('*'*50)}\n {(' '*10)} Loan Feature is OFF\n{('*'*50)}")
      return
    else:
      email = input("Enter your Email: ")
      password = input("Enter your password: ")
      for i in self.total_customer:
        if i['name'] == email and i['password'] == password:
          print(f'{("*"*50)}\n {(" "*10)}You can loan withdraw amount {i["amount"]*2}\n{("*"*50)}')
          amount = int(input("Enter your loan amount: "))
          if amount < self.total_bank_amount and amount <= i['amount']:
            self.total_bank_amount -= amount
            self.total_loan_amount += amount
            his = f"Loan amount {amount}"
            i['history'].append(his)
            print(f"{('*'*50)}\n {(' '*10)}you successfully done loan withdraw.. {amount} \n{('*'*50)}")
          elif amount> self.total_bank_amount:
            print(f"{('*'*50)}\n {(' '*10)} Bank fokira hoiha jabe..\n{('*'*50)}")
          elif amount >= i['amount']:
            print(f"{('*'*50)}\n {(' '*10)}You cannot withdraw loan This amount {amount}\n{('*'*50)}")

  # Admin create account
  def admin_account(self):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    print(f"{('*'*50)}\n {(' '*10)} Successfully admin account create.\n{('*'*50)}")
    self.admin_add = Admin(email, password)
    self.admin.append(vars(self.admin_add))

  # Admin Check Total Bank Balance
  def bank_balance(self):
    email = input("Enter admin Email: ")
    password = input("Enter admin password: ")
    for i in self.admin:
      if i['name'] == email and i['password'] == password:
        print(f"{('*'*50)}\n {(' '*10)} Total Available Bank Balance: {self.total_bank_amount} \n{('*'*50)}")
  
  # Admin check Total loan Balance
  def loan_bank(self):
    email = input("Enter admin Email: ")
    password = input("Enter admin password: ")
    for i in self.admin:
      if i['name'] == email and i['password'] == password:
        print(f"{('*'*50)}\n {(' '*10)}Total loan Bank Balance: {self.total_loan_amount}\n{('*'*50)}")

  # Loan Feauture On or off
  def loan_feauture_off_or_on(self):
    if self.total_bank_amount == 0:
      self.loan_feauture = False
      print(f"{('*'*50)}\n {(' '*10)}OFF loan feauture...\n{('*'*50)}")
    else:
      self.loan_feauture = True
      print(f"{('*'*50)}\n {(' '*10)}ON loan feauture...\n{('*'*50)}")



bank = AB_Bank('AB')
while True:
  print("----------------BANK USER HOLDER INFORMATION-----------")
  print("1. Enter one  for creater customer account: \n2. Enter two deposit and withdraw amount \n3. Enter Three check Avalable Balance \n4. Enter four transfer money another Account \n5. Enter five Check Transaction History. \n6. Enter six withdraw loan..")
  print("----------------BANK ADMIN INFORMATION--------------")
  print("7. Enter seven create admin account \n8. Enter eight total avilable bank balance \n9. Enter nine total loan amount \n10. Enter ten off or on loan feauture.. \n11 Enter ten EXIT..")

  num = int(input(f"{('*'*50)}\nEnter a Number: "))
  if num == 11: 
    break
  if num == 1:
    bank.customer_account()
  elif num == 2:
    print(f"{('*'*50)}\n1. Enter one deposit money \n2. Enter two withdraw money \n{('*'*50)}")
    b = int(input("Enter a number: "))       
    if b == 1:
      bank.deposit(int(input("Enter deposit amount: ")))
    elif b == 2:
      bank.withdraw(int(input("Enter Withdraw amount: ")))
  elif num == 3:
    bank.available_balance()
  elif num == 4:
    bank.Transfer_amount()
  elif num == 5:
    bank.History()
  elif num == 6:
    bank.user_loan()
  elif num == 7:
    bank.admin_account()
  elif num == 8:
    bank.bank_balance()
  elif num == 9:
    bank.loan_bank()
  elif num == 10:
    bank.loan_feauture_off_or_on()
