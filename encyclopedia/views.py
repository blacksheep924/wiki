from django.shortcuts import render
from markdown2 import markdown
from django import forms

from . import util



def index(request):
    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):

    content = util.get_entry(title.strip())
    

       
    if content == None:
        return render(request, "encyclopedia/error.html")
    else:
        content = markdown(content)
        return render(request, "encyclopedia/title.html", {'content':content, 'title':title})
        
def error(request):
    return render(request, "encyclopedia/error.html")

def search(request):
    if request.method == "GET":
        query = request.GET.get('q', 'None').lower()
        titles = util.list_entries()
        newlist = []
        
        for title in titles:
            
            
            if query.lower() in title.lower() and query.lower() != title.lower():
                newlist.append(title)
                
                
            if query.lower() == title.lower():
                content = util.get_entry(title)
                content = markdown(content)
                return render(request,"encyclopedia/title.html",{'content': content, 'title' : title})
        if newlist:
            return render(request,"encyclopedia/search.html", {'query' : query, "titles" : newlist})
            
        else:
            return render(request, "encyclopedia/error.html")
            
            



        
        

        
    
         

    
    
    
    


