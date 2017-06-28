from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import json, MySQLdb, datetime

conn = MySQLdb.connect(host= "application-db",
                  user="app",
                  passwd="zTAcDEhTIM",
                  db="application")
cur= conn.cursor()

def function_ok():
    print "function_ok got called " 
    cur.execute("""insert into events (service,datetime,state) values ('application-python-server',now(),'ok');""")
    conn.commit()

def function_err():
    print "function_err got called"
    cur.execute("""insert into events (service,datetime,state) values ('application-python-server',now(),'ERROR');""")
    conn.commit()

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            if datetime.datetime.now().minute % 2 == 0:
              obj_ok = {
               'status': 'ok', 
               'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
             }
              self.send_response(200)
              self.send_header('Content-Type', 'application/json')
              self.end_headers()
              self.wfile.write(json.dumps(obj_ok,indent=4, sort_keys=True, default=str))
              function_ok()
            else:
              obj_err = {
               'status': 'error', 
               'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
             } 
              self.send_response(200)
              self.send_header('Content-Type', 'application/json')
              self.end_headers()
              self.wfile.write(json.dumps(obj_err,indent=4, sort_keys=True, default=str))
              function_err()
httpd = HTTPServer(("", 80), MyHandler)
httpd.serve_forever()
conn.close()
cur.close()
