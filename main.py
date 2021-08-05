import sqlite3, tinydb, json, yaml as pyyaml, strictyaml, toml, cson as pycson, os
from pysondb import db as pysondb
from dict2xml import dict2xml

div="-"*os.get_terminal_size().columns
jsond={"a":"fuck","b":420.69,"c":69,"e":None,"f":True}
fulld={"a":"fuck","b":420.69,"c":69,"d":bytes("h","utf-8"),"e":None,"f":True}

exists=lambda p: os.path.exists("./"+str(p))
rm=lambda p: os.remove("./"+str(p))
loaded=lambda s, d="": print(div+f"\n{str(s)} Loaded!!!\n\n{str(d).strip()}")

def _sqlite3(fp="sqlite3.db"):
    if exists(fp):
        rm(fp)
    con=sqlite3.connect(fp)
    cur=con.cursor()
    cur.execute("CREATE TABLE one (a TEXT, b REAL, c INTEGER, d BLOB, e NULL, f BOOL)")
    cur.execute("INSERT INTO one VALUES (?,?,?,?,?,?)",(fulld["a"],fulld["b"],fulld["c"],fulld["d"],fulld["e"],fulld["f"],))
    con.commit()
    cur.execute("SELECT * FROM one")
    loaded("SQLite3",cur.fetchall())
    con.close()

def _tinydb(fp="tinydb.json"):
    if exists(fp):
        rm(fp)
    db=tinydb.TinyDB(fp)
    db.insert(jsond)
    loaded("TinyDB",db.all())

def _json(fp="json.json"):
    f=open("./"+fp,"w")
    json.dump(jsond,f)
    f.close()
    loaded("JSON",json.dumps(jsond))

def _pysondb(fp="pysondb.json"):
    if exists(fp):
        rm(fp)
    a=pysondb.getDb("./"+fp)
    a.add(jsond)
    if exists(fp+".lock"):
        rm(fp+".lock")
    if "id" in jsond.keys():
        jsond.pop("id")
    loaded("PYSONDB",a.getAll())

def _pyyaml(fp="pyyaml.yaml"):
    f=open(fp,"w")
    f.write(pyyaml.dump(fulld))
    f.close()
    loaded("PyYAML",pyyaml.dump(fulld))

def _strictyaml(fp="strictyaml.yaml"):
    schema=strictyaml.Map({"a":strictyaml.Str(),"b":strictyaml.Float(),"c":strictyaml.Int(),"e":strictyaml.NullNone(),"f":strictyaml.Bool()})
    document=strictyaml.as_document(jsond,schema=schema)
    f=open(fp,"w")
    res=document.as_yaml()
    f.write(res)
    f.close()
    loaded("StrictYAML",res)

def _toml(fp="toml.toml"):
	f=open(fp,"w")
	res=toml.dumps(fulld)
	f.write(res)
	f.close()
	loaded("TOML",res)

def _pycson(fp="pycson.cson"):
	f=open(fp,"w")
	res=pycson.dumps(jsond)
	f.write(res)
	f.close()
	loaded("PyCSON",res)

def _dict2xml(fp="dict2xml.xml"):
	f=open(fp,"w")
	res=dict2xml(fulld)
	f.write(res)
	f.close()
	loaded("Dict2XML",res)

def main():
    print(div+"\nStarting...")
    _sqlite3()
    _tinydb()
    _json()
    _pysondb()
    _pyyaml()
    _strictyaml()
    _toml()
    _pycson()
    _dict2xml()
    print(div+"\nDone!!!\n"+div)

if __name__=="__main__":
    main()
