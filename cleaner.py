import pandas as pd  
ce = pd.read_csv('american-election-tweets.csv' , error_bad_lines=False,sep= ';') #ordnet ce  die gelesene Tabelle zu. UTF-8 wird by default kodiert. error_bad _lines wirft probleatische Zeilen von sich aus raus.
ce = ce.drop(ce[ce.truncated == True].index) #alle gekürzten Tweets werden gelöscht
ce = ce.drop('in_reply_to_screen_name', 1)
ce = ce.drop('is_quote_status', 1)
ce = ce.drop('source_url', 1)
ce = ce.drop('truncated', 1)
ce = ce.drop('is_retweet', 1)#Spalten, welche wir als überflüssig betrachtet haben werden gelöscht
ce.insert(0, 'index', range(0, len(ce))) # Jeder Zeile wird ein Index zugeordnet
ce = ce.replace({r'@': ''}, regex=True) # entfernt @
ce = ce.replace({r'\n': ''}, regex=True) # entfernt Zeilenumbrüche
ce = ce.replace({r'\r': ''}, regex=True)
ce = ce.replace({r',': ''}, regex=True)
ce = ce.replace({r';': ''}, regex=True)
ce.text.replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True) #entfernt nicht ASCII Zeichen
ce.to_csv("cleanelection.csv", index=False) #speichert die gesäuberte Tabelle unter cleanelection.csv



