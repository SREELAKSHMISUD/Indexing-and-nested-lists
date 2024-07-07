districts_of_kerala="Kasaragod, Kannur, Wayanad, Kozhikode, Malappuram, Palakkad, Thrissur, Ernakulam, Idukki, Kottayam, Alappuzha, Pathanamthitta, Kollam, Thiruvananthapuram"
districts=districts_of_kerala.split(", ")

num_districts=len(districts)
print(num_districts)

print(districts[1])
print(districts[-1])#get last item

districts[3]='Calicut'#kozhikode as calicut 
print(districts)

districts.extend(["kochi","cochin"])# updating multiple items at end of list
print(districts)
