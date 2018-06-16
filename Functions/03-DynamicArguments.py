# *args
# **kwargs
def emp(id,name,age,*address):
    print("ID : {}".format(id))
    print("Name : {}".format(name))
    print("Age : {}".format(age))
    # print("Address : {}".format(address))

    for i,addr in enumerate(address):
        print("Address {} : {}".format(i+1,addr))

# emp(101,'Ram',30,'Delhi','Noida')
# emp(102,'Shyam',32,'Delhi','Noida','Pune')

def student(**details):
    print(details)

student(name = 'Ram', age = 18, college = 'IP')
student(name = 'Shyam', college = 'DU', hobby = 'cricket')
student(name = 'Mohan', age = 20, hobby = 'Football', gender = 'male')

