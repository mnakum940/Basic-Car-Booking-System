import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="ur password",
                                   database="school")
    c = mydb.cursor(buffered = True)
    class Application:
        def __init__(self):
            self.name = input("Search Name: ")
            sql = "SELECT * FROM appointments WHERE name LIKE %s"
            c.execute(sql, (self.name,))
            res = c.fetchall()
            #res = self.res
            for row in res:
                print("Name =", row[0])
                print("Age =", row[1])
                print("Gender =", row[2])
                print("Location =", row[3])
                print("Time =", row[4])
                print("Phone =", row[5],"\n")
                x = input("Want to Delete or Update? D/U: ")
                if x=="U" or x=="u":
                    newname = input("Enter New Name: ")
                    newage = input("Enter New Age: ")
                    newgender = input("Enter new gender M/F/O: ")
                    newlocation = input("Enter new location: ")
                    newtime = input("Enter new time: ")
                    newphone = input("Enter New number: ")
                    if newname == '' or newage == '' or newgender == '' or newlocation == ''or newtime == ''or newphone == '':
                        print("Warning", "Please Fill Up All Boxes")
                        return Application()
                    else:
                        query = "UPDATE appointments SET name= %s, age= %s, gender= %s, location= %s,time= %s, phone= %s"
                        c.execute(query,(newname, newage, newgender, newlocation, newtime, newphone))
                        mydb.commit()
                        print("Updated successfully")
                if x=="D" or x=="d":
                    num = input("Enter the Phone Number to delete data: ")
                    y = input("Are you sure you want to DELETE? Y/N: ")
                    if y=="Y" or y=="y":
                        sql2 = "DELETE FROM appointments WHERE name LIKE %s"
                        c.execute(sql2, (num,))
                        mydb.commit()
                        print("Deleted Successfully...")
                    else:
                        return Application()
            else:
                print("No such data in out server.")
                return Application()
                    
                    
except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))



Application()
