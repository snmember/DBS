import pandas as pd
#wir lassen das cleaning Programm ueber die Hashtags laufen, damit die einzelnen
# Hashtags in einer Zelle und nicht über verschiedene Spalten gespeichert werden."
ha = pd.read_csv('hashtags_bracketless.csv', sep=';')
ha = ha.replace({r',': ''}, regex=True)
ha.to_csv('hashtagsclean.csv', index = False)


