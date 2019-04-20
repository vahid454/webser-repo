from http.server import BaseHTTPRequestHandler,HTTPServer
import os
import json
import cgi
webApps=[]
r=0
PORT_NUMBER=8000
class WebApplicationConfiguration:
 def __init__(self):  
  self.homepageName=""
 def setHomepageName(self,homepageName):
  self.homepageName=homepageName
 def getHomepageName(self):
  return self.homepageName

class WebApplication:
 def __init__(self):
  self.contextName=""
  self.webApplicationConfiguration=None
 def setContextName(self,contextName):
  self.contextName=contextName
 def getContextName(self):
  return self.contextName
 def setWebApplicationConfiguration(self,webApplicationConfiguration):
  self.webApplicationConfiguration=webApplicationConfiguration
 def getWebApplicationConfiguration(self):
  return self.webApplicationConfiguration
 
def getWebApplicationsList():
 webApplications=[]
 files = os.listdir("applications")
 for name in files:
  webApplicationConf=WebApplicationConfiguration()
  if os.path.exists("applications/"+name+"/configuration/config.json")==True:
   config=json.loads(open('applications/'+name+'/configuration/config.json').read())
  if 'Homepage' not in config:
   webApplicationConf.setHomepageName("index.html")
  else:
   webApplicationConf.setHomepageName(config["Homepage"])
  if os.path.exists("applications/"+name+"/configuration/config.json")==False:
   print("False ke if me aaya")
   webApplicationConf.setHomepageName("index.html")
  webApplication=WebApplication()
  webApplication.setContextName(name)
  webApplication.setWebApplicationConfiguration(webApplicationConf)
  webApplications.append(webApplication)
 return webApplications

def searchPosition(a,str):
 count=-1
 applications=[]
 applications=getWebApplicationsList()
 for k in range(0,len(applications)):
  if((a==applications[k].getContextName()) or (str==applications[k].getContextName())):
   count=k
 return count
    

def searchAbsolutePath(pathName):
 j=pathName[1:len(pathName)]
 apps=[]
 apps=getWebApplicationsList()
 pth=pathName
 str=""
 a=j
 print("a:"+a)
 for x in range(0,len(j)):
  if(j[x]=="/"):
   str=j[0:x]
   break 
 print("Str",str)
 
 count=searchPosition(a,str)
 print("Count",count)
 if count==-1:
  if pth=="/":
   pth="Root/index.html"
   return pth
  else:
    pth="Root/"+pth
    return pth
 if a==apps[count].getContextName() and pth.endswith(".html")==False:
  pth="applications/"+apps[count].getContextName()+"/"+apps[count].getWebApplicationConfiguration().getHomepageName()
  return pth
 else:
  if str==apps[count].getContextName():
   if pth.endswith(".jpg") or pth.endswith(".png") or pth.endswith(".css") or pth.endswith(".html") or pth.endswith(".gif") or pth.endswith(".js"):
    pth="applications"+pth
    return pth
   else:
    pth="Root/error.html"
    return pth
 return pth  
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
 contextName=""
 webApps=getWebApplicationsList()
 def do_GET(self):
  self.path=searchAbsolutePath(self.path)
  print(self.path+"*********")
  if os.path.exists(self.path)==False:
   self.path="Root/error.html"
  try:
   sendReply=False
   if self.path.endswith(".html"):
    mimetype='text/html'
    sendReply=True
   if self.path.endswith(".css"):
    mimetype='text/css'
    sendReply=True
   if self.path.endswith(".jpg"):
    mimetype='image/jpg'
    sendReply=True
   if self.path.endswith(".png"):
    mimetype='image/png'
    sendReply=True
   if self.path.endswith(".js"):
    mimetype='application/javascript'
    sendReply=True
   if self.path.endswith(".gif"):
    mimetype='image/gif'
    sendReply=True
   f=open(self.path,'rb')
   self.send_response(200)
   self.send_header('Content-type',mimetype)
   self.end_headers()
   self.wfile.write(f.read())
   f.close()
   return
  except IOError:
    self.send_response(404)
    self.send_error(404,'Path Not Found ' )

def do_POST(self):
 print("do_POST got invoked")

try:
 server=HTTPServer(('localhost',PORT_NUMBER),SimpleHTTPRequestHandler)
 print("Started Http Server on Port",PORT_NUMBER,"................")
 apps=getWebApplicationsList()
 for i in range(0,len(apps)):
  print(apps[i].getContextName())
 server.serve_forever()
except KeyboardInterrupt:
 print("Interrupt recieve shutting down the web server")
 server.socket.close()
