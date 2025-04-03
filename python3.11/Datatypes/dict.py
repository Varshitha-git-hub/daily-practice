#example for dict datatype
#student profile
student_profile={"name":"john","age":20,"course":"python"}
print(student_profile,type(student_profile))

#example for boolean datatype
#login system
is_logged_in=True
if is_logged_in:
    print("you are logged in.")
else:
    print("you are not logged in.")    

#example for set datatype
#production recommendation system
recommendation_product={"laptop","smartphone"}
print(recommendation_product)
recommendation_product.add("earphones")#foe one element we use add
print("update production:",recommendation_product)
recommendation_product.update(["sells","iphone"])
print(recommendation_product)