def introduce_yourself(name,age,country="india"):
    introduction=f"my name is {name} im {age} years old and im from {country}"
    return introduction
introduction1=introduce_yourself("sharan",23)
print(introduction1)
introduction2=introduce_yourself("sharan",23,"scotland")
print(introduction2)