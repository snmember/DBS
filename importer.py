import psycopg2

try:
        conn = psycopg2.connect("dbname='Election' user='postgres' host='localhost' password='postgres'") #stellt Verbindung zur Datenbank her
except:
        print "connection failed" #Fehlermeldung, falls Verbindung nicht gelingt

cur = conn.cursor() #Cursor, welcher in der Datenbank operiert
#query zum Erstellen einer Datenbank, durch den Cursor ausgefuehrt
cur.execute("""COPY usertweet FROM '/home/traplord/Schreibtisch/cleanelection.csv' DELIMITER ',' CSV HEADER""")
#Cursor fuehrt das einfuegen unserer aufbereiteten Tabelle in die kreiierte Datenbank durch
conn.commit() #Aenderung wird in Datenbank gespeichert
cur.close() #Cursor wird beendet
conn.close() #Verbindung wir beendet
