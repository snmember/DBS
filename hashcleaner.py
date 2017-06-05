import pandas as pd
#wir lassen das cleaning Programm ueber die Hashtags laufen, damit die einzelnen
# Hashtags in einer Zelle und nicht ueber verschiedene Spalten gespeichert werden."
ha = pd.read_csv('modcleanelection.csv', sep=';')
#ha = ha.replace({r',': ''}, regex=True)
ha.to_csv('hashtagsclean.csv', index = False)


