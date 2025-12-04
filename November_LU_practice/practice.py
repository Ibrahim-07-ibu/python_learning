class ContactBook :
    def __init__(self):
        self.contacts = []

    def add_contact(self,name,phone_number,email):
        curr_contact = {"name" : name , "phone_number" : phone_number , "email" : email}
        self.contacts.append(curr_contact)
    def get_phone(self,phone_number):
        for el in self.contacts:
            if el["name"] == name:
                print(name,el)
    def update_phone(self,name,phone_number):
        pass
    def delete_contact(self,name):
        pass 

    # test case 1
    my_book = ContactBook()

    my_book.add_contact("John", "9994254379", "alice@email.com")
    my_book.add_contact("Bob", "9876543210", "bob@email.com")

    # print(my_book.get_phone("John"))  # Should output: 123-456-7890
    # print(my_book.get_phone("Charlie")) # Should output: Contact not found.

    # print(my_book.update_phone("John","8994254379")) # should update the contact
    # print(my_book.delete_contact("Bob")) # should delete and print output: "Deletion Completed"

    # print(my_book.delete_contact("Ram")) # Should Print: Contact Not found






