                                                      MUST READ
#webserver-repository
#simple basic server that can server HTML pages,Error pages and Images files according to its resources name.
#I have set the defaul port number as 8000 ,
#What you need is,you just need to create two folder parallel in this server.py
# 1st is "applications" and 2nd is "Root".
# in application folder you can create your website folders for instance : 'one.com'.
in one.com you must create a folder named as "configuration" in it a file "confif.json".
this json can defaultly choose the page that we want to server if there is no resources names;
#-----------------config.json---
{
"Homepage":"lalu.html"
}
#-------------------------------
it means we want to serve lalu.html if the address bar link as : 'http://localhost:8000/one.com/'
and in one.com you may create another folders like CSS/, images/ etc.

And Now in # Root Folder :
# Root folder contains our server default UI, means it can contain folders as - css, images, js, fonts, and
our HTML files like index.html, error.html etc.
# ---------------------------------------------------------------------------------------------------------------------------

