import bevezetes
import sorozat
import epuletek

bevezetes.jatekos_krealas()
lista = sorozat.lista_generalas()
sorozat.lista_kiiratas(lista)

db = sorozat.fejek_szama(lista)
sorozat.konzol_kiir(db)
sorozat.file_kiir(db)

lista = epuletek.beolvas()
epuletek.epuletek_szama(lista)

epuletek.legoregebb_epulet(lista)