import sqlite3, tinydb, json, yaml as pyyaml, strictyaml, os
from pysondb import db as pysondb

div="-"*os.get_terminal_size().columns
jsond={"a":"fuck","b":420.69,"c":69,"e":None}
fulld={"a":"fuck","b":420.69,"c":69,"d":bytes("h","utf-8"),"e":None}

exists=lambda p: os.path.exists("./"+str(p))
rm=lambda p: os.remove("./"+str(p))
loaded=lambda s: print(div+f"\n{str(s)} Loaded!!!")

def _sqlite3(fp="sqlite3.db"):
    if exists(fp):
        rm(fp)
    con=sqlite3.connect(fp)
    cur=con.cursor()
    cur.execute("CREATE TABLE one (a TEXT, b REAL, c INTEGER, d BLOB, e NULL)")
    cur.execute("INSERT INTO one VALUES (?,?,?,?,?)",(fulld["a"],fulld["b"],fulld["c"],fulld["d"],fulld["e"],))
    con.commit()
    con.close()
    loaded("SQLite3")

def _tinydb(fp="tinydb.json"):
    if exists(fp):
        rm(fp)
    db=tinydb.TinyDB(fp)
    db.insert(jsond)
    loaded("TinyDB")

def _json(fp="json.json"):
    f=open("./"+fp,"w")
    json.dump(jsond,f)
    f.close()
    loaded("JSON")

def _pysondb(fp="pysondb.json"):
    if exists(fp):
        rm(fp)
    a=pysondb.getDb("./"+fp)
    a.add(jsond)
    if exists(fp+".lock"):
        rm(fp+".lock")
    if "id" in jsond.keys():
        jsond.pop("id")
    loaded("PYSONDB")

def _pyyaml(fp="pyyaml.yaml"):
    f=open(fp,"w")
    f.write(pyyaml.dump(fulld))
    f.close()
    loaded("PyYAML")

def _strictyaml(fp="strictyaml.yaml"):
    schema=strictyaml.Map({"a":strictyaml.Str(),"b":strictyaml.Float(),"c":strictyaml.Int(),"e":strictyaml.NullNone()})
    document=strictyaml.as_document(jsond,schema=schema)
    f=open(fp,"w")
    f.write(document.as_yaml())
    f.close()
    loaded("StrictYAML")

def main():
    print(div+"\nStarting...")
    _sqlite3()
    _tinydb()
    _json()
    _pysondb()
    _pyyaml()
    _strictyaml()
    print(div+"\nDone!!!\n"+div)

if __name__=="__main__":
    main()