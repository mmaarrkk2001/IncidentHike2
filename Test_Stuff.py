route_string = "1234567"
connection_string = "dbname=incident_hike user=mark"
hike_id = 10

# open a cursor
try:
    conn = psycopg2.connect(Connection_String)
    cursor = conn.cursor()
except:
    print("Error connecting to database, connection string:" + Connection_String)
    print(e.pgerror)
    print(e.diag.message_detail)

# this function will populate the route table with a new row for the route.
# time check
time = datetime.now()
print(time)

# Now insert the initial information into the table - Hike Id and Route
try:
    cursor.execute("INSERT INTO Routes (hike_id, route_id) VALUES ( %s, %s )", (hike_id, route_string,))
    # conn.commit()
except psycopg2.Error as e:
    print("Error inserting id & route into table:" + str(e))
    print(e.pgerror)
    print(e.diag.message_detail)
    return (False, -1)

# Now work out the individual bases from the input string and create the insert clause
for x in range (0,len(route_string)):
    if x == 0:
        base = route_string[x]
        try:
            cursor.execute("UPDATE routes SET base_1 = %s WHERE route_id = %s AND hike_id = %s",(base, route_string, hike_id))
        except psycopg2.Error as e:
            print("Error inserting base " + str(x) + "number into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return (False, -1)
    elif x == 1:
        base = route_string[x]
        try:
            cursor.execute("UPDATE routes SET base_2 = %s WHERE route_id = %s AND hike_id = %s",(base, route_string, hike_id))
        except psycopg2.Error as e:
            print("Error inserting base " + str(x) + "number into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return (False, -1)
    elif x == 2:
        base = route_string[x]
        try:
            cursor.execute("UPDATE routes SET base_3 = %s WHERE route_id = %s AND hike_id = %s",(base, route_string, hike_id))
        except psycopg2.Error as e:
            print("Error inserting base " + str(x) + "number into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return (False, -1)
    elif x == 3:
        base = route_string[x]
        try:
            cursor.execute("UPDATE routes SET base_4 = %s WHERE route_id = %s AND hike_id = %s",(base, route_string, hike_id))
        except psycopg2.Error as e:
            print("Error inserting base " + str(x) + "number into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return (False, -1)
    elif x == 4:
        base = route_string[x]
        try:
            cursor.execute("UPDATE routes SET base_5 = %s WHERE route_id = %s AND hike_id = %s",(base, route_string, hike_id))
        except psycopg2.Error as e:
            print("Error inserting base " + str(x) + "number into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return (False, -1)
    elif x == 5:
        base = route_string[x]
        try:
            cursor.execute("UPDATE routes SET base_6 = %s WHERE route_id = %s AND hike_id = %s",(base, route_string, hike_id))
        except psycopg2.Error as e:
            print("Error inserting base " + str(x) + "number into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return (False, -1)
    elif x == 6:
        base = route_string[x]
        try:
            cursor.execute("UPDATE routes SET base_7 = %s WHERE route_id = %s AND hike_id = %s",(base, route_string, hike_id))
        except psycopg2.Error as e:
            print("Error inserting base " + str(x) + "number into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return (False, -1)
    elif x == 7:
        base = route_string[x]
        try:
            cursor.execute("UPDATE routes SET base_8 = %s WHERE route_id = %s AND hike_id = %s",(base, route_string, hike_id))
        except psycopg2.Error as e:
            print("Error inserting base " + str(x) + "number into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return (False, -1)
    elif x == 8:
        base = route_string[x]
        try:
            cursor.execute("UPDATE routes SET base_9 = %s WHERE route_id = %s AND hike_id = %s",(base, route_string, hike_id))
        except psycopg2.Error as e:
            print("Error inserting base " + str(x) + "number into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return (False, -1)
    elif x == 9:
        base = route_string[x]
        try:
            cursor.execute("UPDATE routes SET base_10 = %s WHERE route_id = %s AND hike_id = %s",(base, route_string, hike_id))
        except psycopg2.Error as e:
            print("Error inserting base " + str(x) + "number into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return (False, -1)