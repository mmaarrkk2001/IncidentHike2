#Do some imports
#Postgres connection
import psycopg2
import psycopg2.extras
from datetime import datetime

#Let's create a function to calculate the permutations P(n,r) = n!/(n-r)!
def calc_permutations (total_set, number_selected):
    # n will be the length of the input string
    n = len(total_set)
    #then work out (n-r) as y
    y = n-number_selected
    #if we have a negative number, something has gone wrong!.
    if y <0:
        return 0
    else:
        #now we work out n!
        my_numerator = 1
        while n > 0:
            my_numerator = my_numerator * n
            n = n - 1
        #now we work out (n-r)!
        my_denominator = 1
        while y > 0:
            y = y -1
            my_denominator = my_denominator * y
        # finally we work out n!/(n-r)!
        return my_numerator / my_denominator


#Define the function that will iterate through the string and print the output.
#This function will call itself for every position in the input string (so for an 8 character input string, there will be 7 levels of call) each then iterates through it's input string
#shifting a character from the second string to the end of the first string.
#I'm indebted to an excel example found online for the process!
def GetPermutation(Str1, Str2, pCounter,connection_string,hike_id,cursor,debug_flag):
    #print("GetPermutation called with Str1 = " + str(Str1) + ", Str2 = " + str(Str2) + ", pCounter = " + str(pCounter))
    Str2Length = len(Str2)
    if Str2Length < 2:
        #We want to store the output to the database as a route. Create the route
        route = Str1 + Str2

        #now we want to add the result to the routes table
        insert_route(route,connection_string,hike_id, cursor,debug_flag)

    else:
        for i in range(0,Str2Length):
            #For i = 1 To xLen
            #Call GetPermutation(Str1 + Mid(Str2, i, 1), Left(Str2, i - 1) + Right(Str2, xLen - i), xRow)

            #Calculate Mid(Str2,i,1)
            j = i+1
            Str3 = Str2[i:j]

            #Calculate Left(Str2, i - 1)
            if i > 0:
                h = i
                Str4 = Str2[0:h]
            else:
                Str4 = ""

            #Calculate Right(Str2, xLen - i)
            k = Str2Length - (Str2Length - j)
            Str5 = Str2[k:Str2Length]

            #Calculate Str1 + Mid(Str2, i, 1)
            Str6 = Str1 + Str3

            #Calculate Left(Str2, i - 1) + Right(Str2, xLen - i)
            Str7 = Str4 + Str5
            GetPermutation(Str6,Str7,pCounter,connection_string,hike_id,cursor,debug_flag)
    # print("Returning from GetPermutation called with Str1 = " + str(Str1) + ", Str2 = " + str(Str2) + ", pCounter = " + str(pCounter))


def insert_route(route_string, connection_string, hike_id,cursor,debug_flag):
    # this function will populate the route table with a new row for the route.
    # time check
    if debug_flag:
        time = datetime.now()
        print(time)
    # open cursor here:
    # return (False, -1)

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

# close cursor here:
#return (False, -1)

def route_distance_calculator(hike_id, connection_string, debug_flag):
    # this function will calculate the distance for all routes in the routes table for the given hike_id
    # it takes the base distances into a list for performance
    # then takes each route in turn from the routes table and sums the distance - writing it back to the routes table.
    # time check
    if debug_flag:
        time = datetime.now()
        print(time)

    # load the bases into a list, this list will have all of the base distances calculated.
    #create a dictionary for them
    bases_dict = {}

    # open cursor
    try:
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()
    except psycopg2.Error as e:
        print("Error connecting to database, connection string:" + connection_string)
        print(e.pgerror)
        print(e.diag.message_detail)

    #loop through the records and add to the dictionary
    try:
        cursor.execute("SELECT * FROM Bases WHERE hike_id = %s ORDER BY base_no",[hike_id,])

        if debug_flag:
            print("Bases found:\n")

        for record in cursor:
            my_key = str(record[1]) + "-1"
            bases_dict[my_key] = record[3]
            my_key = str(record[1]) + "-2"
            bases_dict[my_key] = record[4]
            my_key = str(record[1]) + "-3"
            bases_dict[my_key] = record[5]
            my_key = str(record[1]) + "-4"
            bases_dict[my_key] = record[6]
            my_key = str(record[1]) + "-5"
            bases_dict[my_key] = record[7]
            my_key = str(record[1]) + "-6"
            bases_dict[my_key] = record[8]
            my_key = str(record[1]) + "-7"
            bases_dict[my_key] = record[9]
            my_key = str(record[1]) + "-8"
            bases_dict[my_key] = record[10]
            my_key = str(record[1]) + "-9"
            bases_dict[my_key] = record[11]

        if debug_flag:
            print(bases_dict)

        cursor.close()
    except psycopg2.Error as e:
        print("Error selecting the bases from the table:" + str(e))
        print(e.pgerror)
        print(e.diag.message_detail)
        return 1

    # now we need to work out the distance for each route:

    # open cursor
    try:
        cursor = conn.cursor()
    except psycopg2.Error as e:
        print("Error connecting to database, connection string:" + connection_string)
        print(e.pgerror)
        print(e.diag.message_detail)

    try:
        cursor.execute("SELECT * FROM routes WHERE hike_id = %s",[hike_id,])

        for record in cursor:
            # reset the distance counter
            route_distance = 0.0

            #create a key for the dictionary and add the amount to the route
            if record[3] != None:
                if record[4] != None:
                    my_key = str(record[3]) + "-" + str(record[4])
                    route_distance = route_distance + bases_dict[my_key]
                    if record[5] != None:
                        my_key = str(record[4]) + "-" + str(record[5])
                        route_distance = route_distance + bases_dict[my_key]
                        if record[6] != None:
                            my_key = str(record[5]) + "-" + str(record[6])
                            route_distance = route_distance + bases_dict[my_key]
                            if record[7] != None:
                                my_key = str(record[6]) + "-" + str(record[7])
                                route_distance = route_distance + bases_dict[my_key]
                                if record[8] != None:
                                    my_key = str(record[7]) + "-" + str(record[8])
                                    route_distance = route_distance + bases_dict[my_key]
                                    if record[9] != None:
                                        my_key = str(record[8]) + "-" + str(record[9])
                                        route_distance = route_distance + bases_dict[my_key]
                                        if record[10] != None:
                                            my_key = str(record[9]) + "-" + str(record[10])
                                            route_distance = route_distance + bases_dict[my_key]
                                            if record[11] != None:
                                                my_key = str(record[10]) + "-" + str(record[11])
                                                route_distance = route_distance + bases_dict[my_key]

            if debug_flag:
                print("Total distance for route - " + record[1] + " = " + str(route_distance))

            # now we need to update the record with the distance.
            try:
                update_cursor = conn.cursor()
                update_cursor.execute("UPDATE routes SET total_distance = %s WHERE hike_id = %s AND route_id = %s",())

    except psycopg2.Error as e:
        print("Error reading from the routes table in route_distance_calculator:" + connection_string)
        print(e.pgerror)
        print(e.diag.message_detail)
