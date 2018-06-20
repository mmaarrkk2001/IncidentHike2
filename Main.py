#Do some imports
import Calculate_Perms
import Dbase_clearup
from hike_utilities import is_number
from hike_utilities import build_string
from hike_utilities import return_hike_id
from hike_utilities import insert_base
from hike_utilities import insert_base_distance
import psycopg2
import psycopg2.extras
from datetime import datetime

# Let's set up some global variables
number_of_perms = 0
pCounter = 1

#CONFIGURATION  VARIABLES:
Connection_String = "dbname=incident_hike user=mark"
debug_flag = True

start = datetime.now()
if debug_flag:
    print(start)

#User needs to logon
flag = True
hike_id = input("Please enter hike number:")
while flag is True:
    if is_number(hike_id):
        flag = False
    else:
        hike_id = input("Must be a number:")
        flag = True

# list the hike ids
return_hike_id(Connection_String)

# are we continuing an existing hike, or are we starting a new one?
clearup = input("Empty Route Table (if N, we use the same hike data)?:")

# First, we need to clear up some stuff if the user wants us to
# Empty the route table
flag = True
while flag is True:
    if clearup == "Y":
        try:
            Dbase_clearup.empty_routes(Connection_String,hike_id)
            flag = False
        except:
            pass
    elif clearup == "N":
        flag = False
    else:
        clearup = input("Try again, Y/N:")
        flag = True

#Now we need to get the number of bases from the user
#check for valid number from the user (< 10) , and convert to string for iteration

if clearup == "Y":
    flag = True
    str_no_of_bases = input("Please enter number of bases:")
    while flag is True:
        if is_number(str_no_of_bases):
            if int(str_no_of_bases) < 10:
                no_of_bases = int(str_no_of_bases)
                route_string = build_string(str_no_of_bases)
                flag = False
            else:
                str_no_of_bases = input ("Try again, must be a number less than 10:")
                flag = True
        else:
            no_of_bases = input ("Try again, must be a number less than 10:")
            flag = True

    #And now we calaulte the number of permutations, then print out the result.

    number_of_perms = Calculate_Perms.calc_permutations(route_string, len(route_string))
    print ("There are " + str(number_of_perms) + " permutations, calculating....")

    #Now calculate the actual values of the permutation.
    # First open a cursor to the database
    try:
        conn = psycopg2.connect(Connection_String)
        cursor = conn.cursor()
    except:
        print("Error connecting to database, connection string:" + Connection_String)
        print(e.pgerror)
        print(e.diag.message_detail)

    x = Calculate_Perms.GetPermutation("", route_string, pCounter, Connection_String, hike_id,cursor,debug_flag)

    # commit and close the cursor
    try:
        conn.commit()
        cursor.close

    except psycopg2.Error as e:
        print("Error inserting route into table, commit and close cursor:" + str(e))
        print(e.pgerror)
        print(e.diag.message_detail)

    if debug_flag:
        print("Start: " + str(start))
        print("after perms calculated: " + str(datetime.now()))

    # now we need to insert the distance between the bases, and work out how long our routes are
    # loop for each base, and ask for the distance to the others
    # we only need to do half the bases, as the return will be the same

    for x in range (1,no_of_bases+1):
        flag = True
        time_at_base = input("How long at base " + str(x) + "?:")
        while flag is True:
            if is_number(time_at_base):
                flag = False
            else:
                time_at_base = input("Try again, must be a number. How long at base " + str(x) + "?:")
                flag = True
        # update the base record with the time at the base.
        insert_base(hike_id,x,time_at_base,Connection_String,debug_flag)

        for y in range (x,no_of_bases+1):
            if x != y:
                flag = True
                distance = input("Please input distance from base " + str(x) + " and " + str(y) + ": \n")
                while flag is True:
                    if is_number(distance):
                        insert_base_distance(hike_id,x,y,distance,Connection_String,debug_flag)
                        # now we need to call back to the function to do the reverse update
                        # base_no input becomes the to_base and to_base becomes the base_no
                        insert_base_distance(hike_id, y, x, distance, Connection_String, debug_flag)
                        flag = False
                    else:
                        distance = input("Try again, must be a number. Distance from base " + str(x) + " and " + str(y) + ": \n")
                        flag = True

    try:
        cursor.close()

    except psycopg2.Error as e:
        print("Error inserting route into table, commit and close cursor:" + str(e))
        print(e.pgerror)
        print(e.diag.message_detail)

# we now have all of the information on bases and routes. We can calculate the distance for each route.
Calculate_Perms.route_distance_calculator(hike_id,Connection_String,debug_flag)
