from django.shortcuts import render, redirect
from markdown2 import markdown
from django import forms
import os
from django.http import HttpResponse 
import random
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
    return render(request, "encyclopedia/error.html", {'message' : "Page cannot be found."})

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
                return redirect('title', title = title)
                
        if newlist:
            return render(request,"encyclopedia/search.html", {'query' : query, "titles" : newlist})
            
        else:
            return render(request, "encyclopedia/error.html",{'message': "There's no match with your query."})
    
def new(request):

    if request.method == "POST":
        new_title = request.POST.get('header', 'None')
        new_page = request.POST.get('new_page', 'None')
        titles = util.list_entries()
        for title in titles:
            if new_title.lower() == title.lower():
                return render(request, "encyclopedia/error.html", {'message' : "This entry already exist."})
            else:
                
                markdown_content = f"# {new_title}\n{new_page}"

                folder_path = os.path.join(os.path.dirname(__file__), '..', 'entries')
                file_path = os.path.join(folder_path, f"{new_title}.md")
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(markdown_content)                        
                    return redirect('title', title = new_title)
              
    return render(request, "encyclopedia/new.html")

def edit(request):
    title = request.GET.get('title')
    
    
    
    if request.method == "POST":
        title = request.POST.get('title', 'None')
        folder_path = os.path.join(os.path.dirname(__file__), '..', 'entries')
        file_path = os.path.join(folder_path, f"{title}.md")
        content = request.POST.get('new_page', 'None')
        with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)                        
                    return redirect('title', title = title)
    else:
        page_content = util.get_entry(title)

        
        return render(request, "encyclopedia/edit.html",{'title' : title, 'content' : page_content})
    
def rand(request):
    random_list = util.list_entries()
    random_number = random.randint(0, len(random_list)-1)
    random_entry = random_list[random_number]
    title = random_entry
    return redirect('title', title = title)



    

    
    
            
            
            
    


    
            
            



        
        

        
    
         

    
    
    
    


