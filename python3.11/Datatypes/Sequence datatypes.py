#example for sequence datatypes
#Music Playlist
song="happy birthday"#string
song_artists=["ajay","abdul","khan"]#list
song_generic=("classic","melody","pleasent")#tuple
song_artists.append("mr")#adding a elelment into list
print(song_generic)#print the tuple statement
l1=list(song_generic)#tuple to list conversion
l1.append("peace")#add a element into a conversion list
print(song_generic)
song_generic=tuple(l1)#list to tuple conversion
print(song_generic)
print(song)
print(song_artists)

#Example for string datatype
#social media
post_content="python full stack"
post_author="abdul ajay khan"
post_comments="congraluations! welldone"
print(post_content)
print(post_author)
print(post_comments)

#Example for list datatype
#Shopping cart
cart_items=["laptop","mobiles","smartwatch"]
print(cart_items,type(cart_items))
cart_items.append("intel laptop")
print("updated cart items:",cart_items)
cart_items.extend(["dell laptop","intel core"])
print(cart_items)

#Example for tuple datatype
#student record
student_record=("john",20,"computer science")
print("student_record:",student_record)