import mysql.connector
from web_scraping import my_dict1, my_dict2, my_dict3

try:
    connection= mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Dionusia1080",
    database="recycling" )
    
    ###############################################################################################
    #year_total table
    mycursor = connection.cursor()

    mycursor.execute("CREATE TABLE year_recycling (year YEAR(4) PRIMARY KEY,number_of_garbage INT)")\

    insert_query = "INSERT INTO year_recycling (year,number_of_garbage)VALUES (%s,%s)"

    val = (list(my_dict1.items())[0])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict1.items())[1])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict1.items())[2])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict1.items())[3])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict1.items())[4])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict1.items())[5])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict1.items())[6])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict1.items())[7])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict1.items())[8])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict1.items())[9])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict1.items())[10])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict1.items())[11])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")
    
    mycursor.close()

    ###############################################################################################
    #type_total table
    mycursor = connection.cursor()

    mycursor.execute("CREATE TABLE type_recycling (type VARCHAR(20) PRIMARY KEY,number_of_garbage INT)")\

    insert_query = "INSERT INTO type_recycling (type,number_of_garbage)VALUES (%s,%s)"

    val = (list(my_dict2.items())[0])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict2.items())[1])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict2.items())[2])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict2.items())[3])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict2.items())[4])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict2.items())[5])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict2.items())[6])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict2.items())[7])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict2.items())[8])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict2.items())[9])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict2.items())[10])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict2.items())[11])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")
    
    mycursor.close()

    ###############################################################################################
    #top5 months table
    mycursor = connection.cursor()

    mycursor.execute("CREATE TABLE top5Months_recycling (month VARCHAR(20) PRIMARY KEY,number_of_garbage INT)")\

    insert_query = "INSERT INTO  top5Months_recycling (month,number_of_garbage)VALUES (%s,%s)"

    val = (list(my_dict3.items())[0])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict3.items())[1])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict3.items())[2])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict3.items())[3])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")

    val = (list(my_dict3.items())[4])
    mycursor.execute(insert_query,val)
    connection.commit()
    print(mycursor.rowcount, "Data inserted successfully into year_recycling")
    mycursor.close()


#insert failed
except mysql.connector.Error as error:
    print("Error while inserting into table {}".format(error))
#close connection
finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")