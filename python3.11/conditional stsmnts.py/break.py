#eg-1:
books=["ramayanam"]
target_book="ramayanam"
for book in books:
    if book==target_book:
        print("found '{target_book}' in the list!.")
        break
    else:
        print("'{target_book}' not found in the list!.")

#eg-2:
while True:
    username=input("enter your username:")
    if len(username)>=3 and len(username)<=15:
        print("username is valid!")
        break
    else:
        print("username must be b/w 3 and 15 characters.")
           
