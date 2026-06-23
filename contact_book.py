contacts = {
    "Rahul": "9876543210",
    "Amit": "9876543211",
    "Gopal": "9876543212"
}

name = input("Enter Name: ")

if name in contacts:
    print("Phone Number:", contacts[name])
else:
    print("Contact Not Found")
