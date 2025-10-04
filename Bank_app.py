import streamlit as st


class BankAccount:
    def __init__(self,name,pin,balance=0):
        self._balance=balance
        self.name=name
        self.__pin=pin

    def deposit(self,amount,pin):  # public method
        if pin == self.__pin:
          if amount >0:
            self._balance += amount
            print(f"✔....Deposited ₹{amount}, New Balance : ₹{self._balance}")
          else:
            print("Invalid deposit Amount")
        else:
            print("Access Denied!.........❌Wrong pin number!")

    def get_balance(self,pin):  # public method with private data
        if pin == self.__pin:
            return f"Current Balance : ₹{self._balance}"
        else:
            print("Access Denied!..... Wrong pin number!")

    def withdraw(self,amount,pin):
        if pin == self.__pin:
          if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn ₹{amount}, New Balance : ₹{self._balance}")
          else:
            print("Incorrect Withdrawal Amount")
        else:
            print("Access Denied!..... Wrong pin number!")

# acc=BankAccount("Alex",125)

# acc.deposit(5000,126)
# acc.get_balance(125)
# acc.deposit(1000,125)
# acc.deposit(0,125)
# acc.get_balance(125)
# acc.withdraw(500,125)
# acc.get_balance(125)

# initialize
if "account" not in st.session_state:
  st.session_state.account =  None
st.title("🏛 Bank Account System")
menu=["Create Account","Deposit","Withdraw","Check Balance"]
choice=st.sidebar.selectbox("Menu",menu)

# Create Account
if choice == "Create Account":
  st.subheader("Open New Bank Account")
  name = st.text_input("Enter your name")
  pin = st.text_input("Set a 4-digit PIN",type="password")
  balance = st.number_input("Initial Deposit (₹)",min_value=0,step=100)
  if st.button("Create"):
    if name and pin.isdigit() and len(pin) ==4:
      st.session_state.account=BankAccount(name,pin,balance)
      st.success(f"Account created successfully for {name} with balance ₹{balance}")
    else:
      st.error("❌ please enter valid name and 4-digit PIN")

# Deposit money
elif choice =="Deposit":
  if st.session_state.account:
    st.subheader("Deposit Money")
    amount=st.number_input("Enter amount",min_value=1,step=100)
    pin=st.text_input("Enter PIN",type="password")
    if st.button("Deposit"):
      st.session_state.account.deposit(amount,pin)
  else:
    st.warning("⚠ No account found! please create one first.")

# withdraw money
elif choice =="Withdraw":
  if st.session_state.account:
    st.subheader("Withdraw Money")
    amount=st.number_input("Enter amount",min_value=1,step=100)
    pin=st.text_input("Enter PIN",type="password")
    if st.button("Withdraw"):
      st.session_state.account.withdraw(amount,pin)
  else:
    st.warning("⚠ No account found! please create one first.")

# check balance
elif choice == "Check Balance":
  if st.session_state.account:
    st.subheader("Check Balance")
    pin = st.text_input("Enter PIN",type="password")
    if st.button("Check"):
      st.success(st.session_state.account.get_balance(pin))
  else:
    st.warning("⚠ No account found! please create one first.")