# This module will clearout the database
# Do some imports
# Postgres connection
import psycopg2
import psycopg2.extras


def empty_routes(connection_string, hike):
    # now we want to empty the routes table.
    # connect to the database
    try:
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()
    except:
        print("Error connecting to database, connection string:" + connection_string)
        print(e.pgerror)
        print(e.diag.message_detail)
        return -1
    else:
        try:
            cursor.execute("DELETE FROM routes WHERE hike_id = %s", (hike,))
            conn.commit()
            cursor.close()
        except psycopg2.Error as e:
            print("Error inserting route into table:" + str(e))
            print(e.pgerror)
            print(e.diag.message_detail)
            return 1

