#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import json

def json2table(json, tableHtml):  
    isMain=False
    if len(tableHtml) ==0:
        isMain=True
        tableHtml=("<table border=1 width=100%>") 
    if isinstance(json, list) :
            tableHtml+="<tr><td width=70%><table>"
            for k in range (0,len(json)): 
                if isinstance(json[k] , str) or isinstance(json, int):
                    tableHtml+="<tr><td>" +str(json[k].key()) +"</td><td>"+str(json[k])+"</td></tr>"
                elif str(json[k])[0]=="{" or isinstance(json[k], dict):
                    tableHtml +="<table border=1 width=100%><tr>" 
                    fieldNames=list(json[k].keys())
                    while len(fieldNames)>0:
                        if isinstance(json[k][fieldNames[0]], int) :
                            tableHtml +="name" 
                        tableHtml=json2table(json[k][fieldNames[0]],tableHtml)
                        del fieldNames[0]
                    tableHtml+="</tr></table>"
                else:
                    tableHtml=json2table(json[k],tableHtml) 
            if isinstance(json[0], str):
                tableHtml+="</table>" 
            tableHtml+="</td></tr>"       
    elif not isinstance(json, str) and not isinstance(json, int) :
        jsonKeys=list(json.keys())
        if isinstance(json[jsonKeys[0]], list) :
            tableHtml+="<tr><td width=30%>"+str(jsonKeys[0]).capitalize()+"</td><td width=70%><table>"
            for k in range (0,len(json[jsonKeys[0]])):
                if isinstance(json[jsonKeys[0]][k], str):
                    tableHtml+="<tr><td>"+str(json[jsonKeys[0]][k] )+"</td></tr>"
                elif str(json[jsonKeys[0]])[0]=="{" or isinstance(json[jsonKeys[0]][k], dict):
                    tableHtml +="<table border=1 width=100%><tr><th colspan=2>"+jsonKeys[0]+"</th></tr><tr>" 
                    fieldNames=list(json[jsonKeys[0]][k] .keys())
                    while len(fieldNames)>0:
                        tableHtml=json2table(json[jsonKeys[0]][k] [fieldNames[0]],tableHtml)
                        del fieldNames[0]
                    tableHtml+="</tr></table>"
                else:
                    tableHtml=json2table(json[jsonKeys[0]][k],tableHtml) 
            if isinstance(json[jsonKeys[0]][0], str):
                tableHtml+="</table>" 
            tableHtml+="</td></tr>"   
        elif str(json[jsonKeys[0]])[0]=="{" or isinstance(json[jsonKeys[0]], dict):
            tableHtml +="<table border=1 width=100%><tr><th colspan=2>"+jsonKeys[0]+"</th></tr><tr>" 
            fieldNames=list(json[jsonKeys[0]].keys())
            while len(fieldNames)>0:
                tableHtml=json2table(json[jsonKeys[0]][fieldNames[0]],tableHtml)
                del fieldNames[0]
            tableHtml+="</tr></table>"
        del json[jsonKeys[0]]
        jsonKeys=list(json.keys())
        if len(list(jsonKeys))>0:          
            tableHtml=json2table(json ,tableHtml)    
    else:
        tableHtml+="<td width=70%>"+str(json) +"</td></tr>" 
    if isMain==True:
        tableHtml+="</table>"
    return tableHtml 