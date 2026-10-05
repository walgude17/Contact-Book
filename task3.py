
contacts = []

def add_contact():
    name = input("Enter name:")
    phone = input("Enter phone numberr:")

    contact = {
     "name": name,
     "phone": phone
  }

    contacts.append(contact)
    print("Contact added sucessfully !!")

def view_contacts():
    for contact in contacts:
      print("Name:",contact["name"])
      print("Phone:",contact["phone"])

def search_contacts():
    name = input("Enter name to search:")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
          print("Name:",contact["name"])
          print("Phone:",contact["phone"])
          return

    print(("Contact not found!!"))  
def delete_contact():
    name = input("Enter name to delete:")
    for contact in contacts:
       if contact["name"].lower() == name.lower():
        contacts.remove(contact)
        print("Contact deleted sucessfully !!")
        return

    print("Contact not found !")

add_contact()
view_contacts()
search_contacts()
delete_contact()
