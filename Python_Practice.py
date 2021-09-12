print("Hello World")
#Name = "Vissu"
#status = True
#print("My Name is : "+ str(status))
#print(f" My name is : {status}")
#ball = 1,314
""" print(type(ball))
type(1)
help("keywords") 
print("Hello World") """

""" counties = ["A","B","C"]
print(f" {counties[1]} + {len(counties)}")
counties.append("D")
print(counties)
#print(counties.pop(2))
counties[2] = "E"
print(counties) """
""" 
con_dict = dict()
con_dict["A"] = 100
con_dict["B"] = 200
con_dict["C"] = 300
#print(f"{con_dict}")
print(con_dict.items())

listdict=[]
listdict.append({"Name":"A","TotalCount":100})
listdict.append({"Name":"B","TotalCount":200})
listdict.insert(1,{"Name":"C","TotalCount":300})
print(f"{listdict[1].keys()}") """



counties = {"A":100,"B":200,"C":300}
for county in counties:
    print(counties[county])

