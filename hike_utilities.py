import psycopg2
import psycopg2.extras
from datetime import datetime

# Checks a string is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def build_string(s):
    out_str = ""
    for x in range (0,int(s)):
        out_str = out_str + str(x + 1)

    return out_str

def return_hike_id(connection_string):
    # this function displays the unique hike id's in the table
    # connect to the database & open cursor
    try:
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()
    except:
        print("Error connecting to database, connection string:" + connection_string)
        print(e.pgerror)
        print(e.diag.message_detail)
        return 1
    else:
        try:
            cursor.execute("SELECT DISTINCT hike_id FROM routes;")
            print("Current Hikes:\n")
            for record in cursor:
                print(record[0])
            cursor.close()
        except psycopg2.Error as e:
            print("Error selecting the hikes from the table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return 1

def insert_base_distance (hike_id, base_no, to_base, distance, connection_string, debug_flag):
    # this function will update or insert a record into the bases table for the distance
    if debug_flag:
        print ("insert_base_distance called. Hike_id = " + str(hike_id) + ", base_no = " + str(base_no) + ", to base = " + str(to_base) +", distance = " + str(distance))
        print ("database connection: " + connection_string)
        print (datetime.now())

    # open cursor
    try:
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()
    except psycopg2.Error as e:
        print("Error connecting to database, connection string:" + connection_string)
        print(e.pgerror)
        print(e.diag.message_detail)



    try:
        cursor.execute("SELECT COUNT(*) FROM bases WHERE hike_id = %s AND base_no = %s", [hike_id, base_no,])
        record = cursor.fetchone()[0]
    except psycopg2.Error as e:
        print("Error counting routes on route table:" + str(e))
        print(e.pgerror)
        print(e.diag.message_detail)
        return 1

    # if record count is 0, then we insert a record
    if record == 0:
        if debug_flag:
            print("No records, doing an insert")

        # we are going to insert a new record for the base into the bases table.
        # we need to insert the distance into the right base value
        cursor_insert = conn.cursor()

        # create the SQL string based on the base we are updating
        z = base_distance_SQL_insert(to_base)
        if debug_flag:
            print(z)

        try:
            cursor_insert.execute(z,[hike_id, base_no, distance,])
            conn.commit()
        except psycopg2.Error as e:
            print("Error inserting base distances into bases table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return 1

    elif record == 1:
        if debug_flag:
            print("Record found, we do an update")

        # we are going to update an existing record for the base in the bases table.
        # we need to insert the distance into the right base value
        cursor_insert = conn.cursor()

        # create the start of the SQL string
        z = base_distance_SQL_update(to_base)
        if debug_flag:
            print(z)

        # Format is: "UPDATE Bases SET time_at_base = %s, base_1 = %s) WHERE hike_id = %s AND base_no = %s",
        try:
            cursor_insert.execute(z,[distance, hike_id,base_no,])
            conn.commit()
        except psycopg2.Error as e:
            print("Error inserting base record into bases table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return 1

    else:
        print("more than one record found, we have a problem!")


    print(record)
    cursor.close()

#CONFIGURATION  VARIABLES:
# Connection_String = "dbname=incident_hike user=mark"
# return_hike_id(Connection_String)

def base_distance_SQL_insert(x):
    return {
        1: "INSERT INTO Bases (hike_id, base_no, base_1) VALUES( %s, %s, %s)",
        2: "INSERT INTO Bases (hike_id, base_no, base_2) VALUES( %s, %s, %s)",
        3: "INSERT INTO Bases (hike_id, base_no, base_3) VALUES( %s, %s, %s)",
        4: "INSERT INTO Bases (hike_id, base_no, base_4) VALUES( %s, %s, %s)",
        5: "INSERT INTO Bases (hike_id, base_no, base_5) VALUES( %s, %s, %s)",
        6: "INSERT INTO Bases (hike_id, base_no, base_6) VALUES( %s, %s, %s)",
        7: "INSERT INTO Bases (hike_id, base_no, base_7) VALUES( %s, %s, %s)",
        8: "INSERT INTO Bases (hike_id, base_no, base_8) VALUES( %s, %s, %s)",
        9: "INSERT INTO Bases (hike_id, base_no, base_9) VALUES( %s, %s, %s)"
        }[x]

def base_distance_SQL_update(x):
    return {
        1: "UPDATE Bases SET base_1 = %s WHERE hike_id = %s AND base_no = %s",
        2: "UPDATE Bases SET base_2 = %s WHERE hike_id = %s AND base_no = %s",
        3: "UPDATE Bases SET base_3 = %s WHERE hike_id = %s AND base_no = %s",
        4: "UPDATE Bases SET base_4 = %s WHERE hike_id = %s AND base_no = %s",
        5: "UPDATE Bases SET base_5 = %s WHERE hike_id = %s AND base_no = %s",
        6: "UPDATE Bases SET base_6 = %s WHERE hike_id = %s AND base_no = %s",
        7: "UPDATE Bases SET base_7 = %s WHERE hike_id = %s AND base_no = %s",
        8: "UPDATE Bases SET base_8 = %s WHERE hike_id = %s AND base_no = %s",
        9: "UPDATE Bases SET base_9 = %s WHERE hike_id = %s AND base_no = %s",
        }[x]

def insert_base (hike_id, base_no, time_at_base, connection_string, debug_flag):
    # this function will update or insert a record into the bases table for the distance
    if debug_flag:
        print ("insert_base called. Hike_id = " + str(hike_id) + ", base_no = " + str(base_no) + ", time at base = " + str(time_at_base))
        print ("database connection: " + connection_string)
        print (datetime.now())

    # open cursor
    try:
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()
    except psycopg2.Error as e:
        print("Error connecting to database, connection string:" + connection_string)
        print(e.pgerror)
        print(e.diag.message_detail)

    # first see if there is a record on the table.
    try:
        cursor.execute("SELECT COUNT(*) FROM bases WHERE hike_id = %s AND base_no = %s", [hike_id, base_no,])
        record = cursor.fetchone()[0]
    except psycopg2.Error as e:
        print("Error counting bases on the bases table:" + str(e))
        print(e.pgerror)
        print(e.diag.message_detail)
        return 1

    # if record count is 0, then we insert a record
    if record == 0:
        if debug_flag:
            print("No records, doing an insert")

        # we are going to insert a new record for the base into the bases table.
        # we need to insert the distance into the right base value
        cursor_insert = conn.cursor()

        try:
            cursor_insert.execute("INSERT INTO Bases (hike_id, base_no, time_at_base) VALUES (%s, %s, %s)",[hike_id,base_no, time_at_base,])
            conn.commit()
        except psycopg2.Error as e:
            print("Error inserting base record (time at base) into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return 1

    elif record == 1:
        if debug_flag:
            print("Record found, we do an update")

        # we are going to update an existing record for the base in the bases table.
        # we need to insert the distance into the right base value
        cursor_insert = conn.cursor()

        # Format is: "UPDATE Bases SET time_at_base = %s, base_1 = %s) WHERE hike_id = %s AND base_no = %s",
        try:
            cursor_insert.execute("UPDATE Bases SET time_at_base = %s WHERE hike_id = %s AND base_no = %s",[time_at_base, hike_id,base_no,])
            conn.commit()
        except psycopg2.Error as e:
            print("Error inserting base record into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return 1

    else:
        print("more than one record found, we have a problem!")


    print(record)
    cursor.close()
# print (base_SQL(2))
