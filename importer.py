import psycopg2

try:
        conn = psycopg2.connect("dbname='Election' user='postgres' host='localhost' password='postgres'") #stellt Verbindung zur Datenbank her
except:
        print "connection failed" #Fehlermeldung, falls Verbindung nicht gelingt

cur = conn.cursor() #Cursor, welcher in der Datenbank operiert
cur.execute("""CREATE TABLE public.tweet(index integer NOT NULL, handle char(20) NOT NULL, text text NOT NULL, original_author char(20),time timestamp NOT NULL, retweet_count integer NOT NULL, favourite_count integer NOT NULL, CONSTRAINT "PK" PRIMARY KEY ("index"))""") #query zum Erstellen einer Datenbank, durch den Cursor ausgefuehrt
cur.execute("""COPY tweet FROM '/home/traplord/Schreibtisch/cleanelection.csv' DELIMITER ',' CSV HEADER""") #Cursor fuehrt das einfuegen unserer aufbereiteten Tabelle in die kreiierte Datenbank durch
conn.commit() #Aenderung wird in Datenbank gespeichert
cur.close() #Cursor wird beendet
conn.close() #Verbindung wir beendet
