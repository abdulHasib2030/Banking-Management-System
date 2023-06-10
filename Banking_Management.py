# Banking Management System

# User:
    # 1. create an account
    # 2. Can deposit and withdrawal amount
    # 3. can check available balance
    # 4. can transfer the amount from his account to another user account 
    # 5. Can check transaction history
    # 6. can take a loan from the bank twice of his total amount

# Admin
  #  1. can create an account
  #  2. can check the total available balance of the bank
  #  3. can check the total loan amount
  #  4. can on or off the loan feature of the bank

total_bank_amount = 0
loan_amount = 0

class User:
  def __init__(self, email, password, amount,history):
    self.history = history
    self.email = email
    self.password = password
    self.amount = amount
  


class Bank:
  def __init__(self,email, password):
    self.email = email
    self.password = password
    


class AB_Bank:
  total_customer = []
  admin = []
  

  def customer_account(self):
    email = input("Enter Your email: ")
    password = input("Enter Your Password: ")
    amount = 0
    history = []
    self.customer = User(email, password, amount, history)

    self.total_customer.append(vars(self.customer))

  def get_user(self):
    return self.total_customer
  
  def get_admin(self):
    return self.admin

  def admin_account(self):
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    self.admin_add = Bank(email, password)
    self.admin.append(vars(self.admin_add))



while True:
  company = AB_Bank()

  print("1. ENTER ONE FOR USER \n2. ENTER TWO FOR ADMIN \n3. EXIT")
  print('*'*50)
  num = int(input("Enter a Number: "))
  if num == 3:
    break
  elif num == 1:
    while True:
      
      print("\n1. Crate an account \n2. Login to your account \n3. EXIT")
      print('*'*50)

      a = int(input("Enter a Number: "))
      if a == 3:
        break
      elif a == 1:
        company.customer_account()
       
        print(f"{' '*25}Thank you account create successfully")
        print('*'*50)

      elif a == 2:  
        name = input("Enter your email: ")
        password = input("Enter your password: ")

        for i in company.get_user():
          if i['email'] == name and i['password'] == password:
            
            while True:
              print('*'*50)
              print("1. Enter one deposit amount provide: \n2. Enter two withdraw amount: \n3. Enter three check available balance \n4. Enter four transfer money another account \n5. Enter five check transaction history \n6. Enter six maximum loan amount \n7. EXIT")
              print('*'*50)
              b = int(input("Enter a Number: "))
              print()
              if b == 7:
                break
              elif b == 1:
                amount = int(input("Enter Deposit Amount: "))
                print()
                i['amount'] = i['amount'] + amount
                total_bank_amount += amount
               
                his = f'Deposit Amount: {amount}'
                i['history'].append(his)
                
                print(f'{" "*25}your deposit amount {amount} successfully done')
              elif b == 2:
                amount = int(input("Enter Your Withdrawal amount: "))
                print()
                if i['amount'] < amount:
                  print(f'{" "*25}your bank deposit total amount {i["amount"]}. You cannot withdraw more than {i["amount"]} taka....')
                else:
                  if total_bank_amount == 0:
                    print(f"{' '*25}Bank is brnkrupt.\n")
                    
                  total_bank_amount -= amount  
                  print(f"{' '*25}you are successfull withdrawal amount")
                  i['amount'] = i['amount'] - amount
                  his = f'Withdrawal Amount: {amount}'
                  i['history'].append(his)
                  
              elif b == 3:
                print(f'{" "*25}Your Bank Balance total available {i["amount"]}')
              
              elif b == 4:
                name = input("Enter a Transfer account email: ")
                amount = int(input("Enter a Transfer amount: "))
                if amount > i['amount']:
                  print(f'{"*"*50}\n {" "*25}Your bank balance total {i["amount"]}. You cannot transfer more than {i["amount"]}')
                else:
                  for w in company.get_user():
                    if w['email'] == name:
                      w['amount'] = w['amount'] + amount
                      his = f'Received Money for {i["email"]}: {amount}'
                      w['history'].append(his)

                  i['amount'] =i['amount'] - amount
                  print(f'{" "*25}your balance is {i["amount"]}')
                  print(f"{' '*25}successfully transfer money.")
                  his = f'Transfer Amount: {amount}'
                  i['history'].append(his)

              elif b == 5:
                for k in i['history']:
                    print(f"{' '*25}",k)

              elif b == 6:
                while True:

                  if total_bank_amount == 0:
                    print("Banks have lost their ability to make loans.")
                    break
                 
                  else:
                    print(f'{" "*25} You can borrow a total of {i["amount"] * 2} taka from the bank')
                    print('*'*50)
                 
                    print("1. Enter one take a loan \n2. Enter Two EXIT")
                    print('*'*50)
                    print()
                    one = int(input("Enter a Number: "))
                    if one == 2:
                      break
                    elif one == 1:
                      loan = int(input("Enter Loan Amount: "))
                      print()
                      if loan > (i['amount']*2):
                        print(f'{" "*25}Not this amount loan you. you can borrow a total of {i["amount"]* 2} taka.')
                      elif loan < (i['amount'] * 2):
                        if total_bank_amount < loan:
                          print(f'{" "*25} You do not have as much money is the bank as you want...')
                          break
                        else:
                          total_bank_amount -= loan
                          loan_amount += loan
                          hi = f'Loan Amount: {loan}'
                          i['history'].append(hi)
                          print(f"{' '*25}Thank you. successfully done loan amount")
                    
          elif i['email'] == name and i['password'] != password:
            print(f'{" "*25} Your password incorrect. Please correct password provide..')

          elif i['email'] != name and i['password'] == password:
            print(f'{" "*25} Your email incorrect. Please correct email provide...')



  elif num == 2:
    while True:
      print("*"*50)
      print(f'1. Enter one create a Account \n2. Enter  two login Account \n3. EXIT\n')
      a = int(input("Enter a Number: "))
      if a == 3:
        break
      elif a == 1:
        company.admin_account()
        print(f"{' '*25}Thank you account create successfully")
      elif a == 2:
        email= input("Enter your email: ")
        password = input("Enter your password: ")

        for bnk in company.get_admin():
          if bnk['email'] == email and bnk['password'] == password:
            while True:
              print('*'*50)
              print("1. Enter one check The total available bank balance \n2. Enter two Check the total loan Amount \n3. Enter three on or off the loan feature of the bank \n4. EXIT\n")
              bank_num = int(input("Enter a Number: "))
              if bank_num == 4:
                break
              elif bank_num == 1:
                print(f'{" "*25}The total available bank balance {total_bank_amount}')
              elif bank_num == 2:
                print(f'{" "*25}The total loan Amount: {loan_amount}')
              elif bank_num == 3:
                 if total_bank_amount <=0:
                  print(f"{' '*25}OFF loan Feature.")
                 else:
                  print(f"{' '*25}On loan Feature.")





