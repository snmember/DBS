import pandas as pd  
ce = pd.read_csv('american-election-tweets.csv' , error_bad_lines=False,sep= ';') #ordnet ce  die gelesene Tabelle zu. UTF-8 wird by default kodiert. error_bad _lines wirft problematische Zeilen von sich aus raus.
ce = ce.drop(ce[ce.truncated == True].index) #alle gekuerzten Tweets werden geloescht
ce = ce.drop('in_reply_to_screen_name', 1)
ce = ce.drop('is_quote_status', 1)
ce = ce.drop('source_url', 1)
ce = ce.drop('truncated', 1)
ce = ce.drop('is_retweet', 1)#Spalten, welche wir als ueberfluessig betrachtet haben werden geloescht
ce.insert(0, 'index',(range(0,len(ce)))) # Jeder Zeile wird ein Index zugeordnet
ce['index'] = ce['index'].astype(str)
ce['index'] = '$'+ce['index']+'$'
ce = ce.replace({r'@': ''}, regex=True) # entfernt @
ce = ce.replace({r'\n': ''}, regex=True) # entfernt Zeilenumbrueche
ce = ce.replace({r'\r': ''}, regex=True) # entfernt Wagenruecklauf
ce = ce.replace({r',': ''}, regex=True) # entfernt Kommas
ce = ce.replace({r';': ''}, regex=True) # entfernt Semicolons, durch diesen und den letzten Befehl verhindert wir ein potentielles Verrutschen der Eintraege fuer weitere Anwendungen
ce.text.replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True) #entfernt nicht ASCII-Zeichen
ce.to_csv("cleanelection.csv", index=False, sep =',') #speichert die gesaeuberte Tabelle unter cleanelection.csv



