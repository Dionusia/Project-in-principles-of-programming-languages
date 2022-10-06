import mysql.connector
import pandas as pd

########################################################################################################################
#YEAR TOTAL

#open the csv file in read mode
with open('RecyclingData.csv', 'r') as csvfile:
    #connect to the database
    try:
        database = mysql.connector.connect(host="127.0.0.1", user="root", passwd="Dionusia1080", database="recycling")
    except:
        print('Cant connect to database!')

    # Get the cursor, which is used to traverse the database, line by line
    mycursor = database.cursor()

    mycursor.execute("SELECT * FROM year_recycling")
    select_result = mycursor.fetchall()

    #read the rows from tha database to csv using pandas dataframe
    df = pd.DataFrame(select_result)
    df.to_csv('year_total.csv', header=["YEAR", "TOTAL (IN TONS)"], index=False)
    mycursor.close()
    #close the csv file
csvfile.close

########################################################################################################################
#TYPE_TOTAL

#open the scv file in read mode
with open('RecyclingData.csv', 'r') as csvfile:
    #connect to the database
    try:
        database = mysql.connector.connect(host="127.0.0.1", user="root", passwd="Dionusia1080", database="recycling")
    except:
        print('Database connection failed!')

    # Get the cursor, which is used to traverse the database, line by line
    mycursor = database.cursor()

    mycursor.execute("SELECT * FROM type_recycling")
    select_result = mycursor.fetchall()

    #read the rows from tha database to csv using pandas dataframe
    df = pd.DataFrame(select_result)
    df.to_csv('type_total.csv', header=["TYPE", "TOTAL (IN TONS)"], index=False)
    mycursor.close()
    #close the csv file
csvfile.close


########################################################################################################################
#TOP5

# open the scv file in read mode
with open('RecyclingData.csv', 'r') as csvfile:
        # connect to the database
        try:
            database = mysql.connector.connect(host="127.0.0.1", user="root", passwd="Dionusia1080", database="recycling")
        except:
            print('Database connection failed!')

        # Get the cursor, which is used to traverse the database, line by line
        mycursor = database.cursor()

        mycursor.execute("SELECT * FROM top5months_recycling")
        select_result = mycursor.fetchall()

        # read the rows from tha database to csv using pandas dataframe
        df = pd.DataFrame(select_result)
        df.to_csv('top5months_total.csv',
                  header=["MONTH", "TOTAL (IN TONS)"],
                  index=False)
        mycursor.close()
# close the csv file
csvfile.close





