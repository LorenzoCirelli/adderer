#ricerca testo
#ricerca presenza css
def trovacss(truepos):
    descrizione = documento()
    start = (descrizione).index("\"",(truepos)+5)
    end = (descrizione).index("\"",(start)+2)
    link = (descrizione)[start+1:end]
    print(f"link {link} rilevato per il css")
    trovajs(truepos)

def trovajs(truepos):
    descrizione = documento()
    truepos2 = (descrizione).index("true",(descrizione).index("js",(truepos)+10))
    if truepos2>0 :
        start = (descrizione).index("\"",(truepos2)+5)
        end = (descrizione).index("\"",(start)+2)
        link = (descrizione)[start+1:end]
        print(f"link {link} rilevato per il js")
    else:
        print("Libreria js non rilevata")
    richiesta()    

def ricerca(val):
    descrizione = documento()
    lunghezza = len(val)
    if descrizione.find(val)!=-1:
        posizione = (descrizione).index(val)
        #verifica presenza liberia
        if posizione < 0 :
            print("Valore non trovato")
        else:
            #trova posizione css in manifesto e verifica che sia true
             if ((descrizione[(posizione+lunghezza+1):(posizione+lunghezza+30)]).find("\"true\""))!=-1:
                 truepos = (descrizione).index("true",(descrizione).index("css", (posizione+lunghezza)))
                 trovacss(truepos)
             else:
                  truepos = (descrizione).index("false",(descrizione).index("css", (posizione+lunghezza)))
                  trovajs(truepos)
    else:
        print("library not found")
        richiesta()              

def richiesta():
    txt = input("library to add or exit to exit from console\n")
    if txt == "exit":
        exit
    else:
        ricerca(txt)

#leggi file manifesto
def documento():
    
    manifesto = open('C:\\progetti github\\adderer\\libraries.adderer', 'r')
    line = manifesto.readline()
    testo = line
    while (line != ""):
        line = manifesto.readline()
        testo += line
    manifesto.close()
    return testo
    
#start
richiesta()


#to-do: aggiungi dati a file.js