class chatbook:
    def __init__ (self):
        self.username = '' 
        self.password = ''
        self.logged_in = False
        self.menu()
    def menu (self):
        print("Welcome to ChatBook!")
        print("1. Login")
        print("2. Sign Up")
        choice = input("Choose an option (1 or 2): ")
        if choice == '1':
            pass
        elif choice == '2':
            pass
        else:
            print("Invalid choice. Please try again.")
            exit

obj = chatbook()