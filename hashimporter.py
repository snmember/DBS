import psycopg2

try:
        conn = psycopg2.connect("dbname='Election' user='postgres' host='localhost' password='postgres'")
except:
        print "connection failed"

cur = conn.cursor()
cur.execute("""COPY hashtag FROM '/home/traplord/Schreibtisch/Hashtag_list.csv'DELIMITER ',' CSV HEADER""")
conn.commit()
cur.close()
conn.close()


            
