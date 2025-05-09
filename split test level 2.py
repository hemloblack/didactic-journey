url="John Doe|123-456-7890|johndoe@example.com;Jane Smith|987-654-3210|janesmith@example.com;Bob Brown|555-123-4567|bobbrown@example.com"

persona=url.split(";")

for i in persona:
    number_and_name=i.split("|")
    print("name",number_and_name[0])
    print("phone",number_and_name[1])

