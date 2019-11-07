command = ""

while command.lower() != "quit":

    #Lower case we can declare here so that we dont need to write all the time. 
    command =input("> ").lower()
    if command == "start":
        print ("Car started....")
    elif command == "stop":
        print("Car stopped.")
        
    pass
