import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ur password",
  database="school"
)


c = mydb.cursor()
#use the below line for the first time only than apply # again
c.execute("CREATE TABLE appointments ( name VARCHAR(30), age INT(4),gender VARCHAR(4), location VARCHAR(20), time VARCHAR(10), phone INT(14))")

class Application:
    def __init__(self):
        print("Enter Details")
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.gender = input("Enter Gender M/F/O: ")
        self.location = input("Enter Location to go: ")
        self.time = input("Enter Time: ")
        self.phone = input("Phone Number: ")


    
        if self.name == '' or self.age == '' or self.gender == '' or self.location == ''or self.time == ''or self.phone == '':
            print("Warning", "Please Fill Up All Boxes")
            
        else:
            sql = """INSERT INTO appointments (name, age, gender, location, time, phone) VALUES( %s, %s, %s, %s, %s, %s)"""
            c.execute(sql, (self.name, self.age, self.gender, self.location, self.time, self.phone))
            a = mydb.commit()
            if True:
                print("Success", "Booking for " + str(self.name) + " has been created.")

Application()
