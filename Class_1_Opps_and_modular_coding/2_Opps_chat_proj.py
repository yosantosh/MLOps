


class ChatHookup:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False

        self.home()            # Why home is here : well when we create object this magic method __init__ automatically called so that why it will call home automatically

    def home(self):
        u_input = int(input("""
                            Yo I hope you are doing well,
                            1 : Press 1 to signup or register
                            2 : Press 2 to login
                            3 : Press 3 to post something
                            4 : Press 4 to find strange to chat
                            5 : Press any key to exit
                        
                             """))
        if u_input == 1:
            self.signup()
        elif u_input == 2:
            # call the login method (not the boolean attribute `loggedin`)
            self.login()
        elif u_input == 3:
            self.post()
        elif u_input == 4:
            pass
        else :
            exit()

    def signup(self):
        email = input("Enter you email address : ")
        Pass = input('Enter the password : ')
        self.username = email
        self.password=Pass
        print('You now you are signedup, now try to login/n')
        self.home()

    def login(self):
        if self.username =='' and self.password=='':
            print("Yo bro pehle Singup to krle")
            self.signup()
        else:
                
            while True:
                input_email = input("Write your email address : ")
                input_pass = input("Write you login password : ")
                if self.username == input_email:
                    if self.password==input_pass:
                        print("Woah you loggedin now dont try to dance only backflip is allowed")
                        break
                    else:
                        print("Incorrect Password Pls try again ---> ")
                        continue
                else:
                    print("Incorrect username try again ---> ")
                    continue
            self.home()

    def post(self):
        if self.username=='' and self.password=='':
            print("Signup First!")
        else:
            caption = input("Write caption of the Post : ")
            from PIL import Image
            path = input("Write path of image that you wanna post: ")

            print(caption+'\n\n')
            from term_image.image import from_file, BlockImage
            img = BlockImage.from_file(path)
            img.draw()



chat_H = ChatHookup()