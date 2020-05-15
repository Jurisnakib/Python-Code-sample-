class user():
    Name = ""
    Email = ""
    Password = ""
    login = False

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
            print (self.Name, "\n",self.Email )
        else:
            print("User is not login")

User1 = user ()
User1.Name = "Nakib"
User1.Email = "nakib@gmail.com"
User1.Password = "nakib"
User1.login()
