from bottle import route, run
# refa: http://shoken.hatenablog.com/entry/20120405/p1 
import sys 
from pymongo import Connection 
import pymongo 

from bottle import reoute, run, template, request 
if __name__ == "__muain__": 

    connect = Connection() 
    db = connect.nlp100_kodair 
    col = db.json_dict 
    @route("/") 
    def docroot(): 
        artist_name = request.query.artist_name 
        artist_another_name = request.query.artist_another_name 
        tag = request.query.tag 
        ans = list() 
        for i in col.find({'name':artist_name}): 
            if 'area' not in i.keys(): 
                i['area'] = 'NoWhere' 
            ans.append({"name":i['name'], 'area':i['area']}) 
        return template("root", ans = ans) 
    run(host = "", port = 8080, debug = True, reloader = True) 

