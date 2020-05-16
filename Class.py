class user():
    Name = ""
    Email = ""
    Password = ""
    login = False

    def __init__(self, name, email, password):
        self.Name = name
        self.Email = email
        self.Password = password

    def login(self):
        Email = input("enter your mail ")
        Password = input("enter your password ")

        if Email == self.Email and Password == self.Password:
            login = True
            print("You are Logged in")
        else:
            print("Access Dnied Try again")
            
            
    def Logout(self):
        logout = False
        print("Logged Out")
    def isLogin(self):
        if self.login:
            return True
        else:
            return False    
    def Profile(self):
        if self.isLogin:
            print (self.Name,"\n",self.Email )
        else:
            print("User is not login")

User1 = user ("Nakib", "nakibjuris", "nakib")

User1.login()

#Profile Method. 
User1.Profile()

