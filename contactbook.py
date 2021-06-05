class contactbook():
    def __init__(self):
        self.contactBook = {}

    
    def newContact(self):
        name = input("Name: ")
        mobileNumber = input("Mobile number: ")
        address = input("Address: ")
        email = input("E-mail: ")
        if name != '' and mobileNumber != '':
            if address == '':
                address = '-'
            if email == '':
                email = '-'
            self.contactBook[name] = {'Name':name, 'Mobile Number':mobileNumber, 'address':address, 'email':email}
            
        elif name == '' or mobileNumber == '':
            print('must required name and mobile number')
            self.newContact()
    

    def listContact(self):
        i=0
        if self.contactBook !={}:
            for contacts in self.contactBook:
                i=i+1
                print("\nContact{}\nName: {}\nMobile Number: {}\naddress: {}\nemail: {}".format(i,self.contactBook[contacts]["Name"],self.contactBook[contacts]["Mobile Number"],self.contactBook[contacts]["address"],self.contactBook[contacts]["email"]))
        else:
            print("Contact is empty!!")
    
    def searchContact(self):
        search = input("Search the contact: ")
        if search in self.contactBook:
            print("\nName: {}\nMobile Number: {}\naddress: {}\nemail: {}".format(self.contactBook[search]["Name"],self.contactBook[search]["Mobile Number"],self.contactBook[search]["address"],self.contactBook[search]["email"]))
        else:
            print("no result!!")

    
    def deleteContact(self):
        delete = input("Delete the contact: ")
        if delete in self.contactBook:
            self.contactBook.pop(delete)
        else:
            print(f"No contact with the name '{delete}'!!")


    def editContact(self):
        edit = input("Edit the contact:")
        userinput = ''
        if edit in self.contactBook:
            print("\nName: {}\nMobile Number: {}\naddress: {}\nemail: {}".format(self.contactBook[edit]["Name"],self.contactBook[edit]["Mobile Number"],self.contactBook[edit]["address"],self.contactBook[edit]["email"]))
            while userinput != "finish":
                userinput = input("what do you want to edit name/mobilenumber/address/email, to finish edit type finish")
                if userinput == 'name':
                    self.contactBook[edit]["Name"] = input("Edit the Name:")
                elif userinput == 'mobilenumber':
                    self.contactBook[edit]["Mobile Number"] = input("Edit the Mobile Number:")
                elif userinput == 'address':
                    self.contactBook[edit]["address"] = input("Edit the address:")
                elif userinput == 'email':
                    self.contactBook[edit]["email"] = input("Edit the email:")
        else:
            print(f"No contact with the name '{edit}'!!")


import time
new = contactbook()
userinput = ""
while userinput != 'q':
    userinput = input("\n=====| Welcome to our contactbook |=====\ncerate contact=>c\nlist the contact=>l\nsearch in the contact=>s\nedit the contact =>e\ndelete the contact=>d\nquit the contactbook =>q\n")
    if userinput == 'c':
        new.newContact()
    elif userinput == 'l':
        new.listContact()
    elif userinput == 's':
        new.searchContact()
    elif userinput == 'e':
        new.editContact()
    elif userinput == 'd':
        new.deleteContact()
    time.sleep(1.5)