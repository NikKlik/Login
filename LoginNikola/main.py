class Users:
    def __init__(self, username, password, fullname):
        
        self.username = ""
        self.password = ""
        self.fullname = ""
        
        
person = {}
    
# person =Users(input("Input your username here: "),input("Input your pasword here: "),input("Input your fullname here: ") ) #ovako se kreira novi korisnik
print("""
      
      Dobrodosli u program.
      
      Morate izabrati jednu od sledecih stavki.
      1. Sing in 
      2. Sing up
      3. Cancel
      """)
pristup_programu = int(input("Your input: "))
if pristup_programu == 1:
    person = Users.username.input("Username: ")
    Users.password = input("Password: ")
    print("Hello")

elif pristup_programu == 2:
    Users.username = input("Username: ")
    Users.password = input("Password: ")
    Users.fullname = input("Full Name: ")
    
elif pristup_programu == 3:
    exit

else:
    print("Unrecognized comand")
    
    
    