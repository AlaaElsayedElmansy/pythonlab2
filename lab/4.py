

while True:
    try:
        name = input('enter your name ')
        if name.isdigit() or name == '' :
            print("not vaild")
        else:
            import re
            email = input("enter email")
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            def check(email):
                if (re.search(regex, email)):
                    print("Valid Email")
                    print("your name is " + name)
                    print("your email is " + email)
                else:
                    print("Invalid Email")
            check(email)

            break;
    except ValueError:
        print("not vaild")
        continue



