from django.shortcuts import render, redirect
from .models import userContact, time

def index(request):
    date = time.objects.all()
    return render(request, "phoneContact/index.html", {"time":date})
def contact(request):
    phones = userContact.objects.all()
    return render(request, "phoneContact/contact.html", {"phones":phones})
def create_contact(request):
    return render(request, "phoneContact/create_contact.html", {})
def save(request):
    userContact.objects.create(
        FullName = request.POST['name'],
        Email = request.POST['email'],
        PhoneNo = request.POST['tel'],
        Address = request.POST['home']
    )
    return redirect('contact')
def edit(request, id):
    value = userContact.objects.get(id=id)
    return render(request, 'phoneContact/edit.html', {'value':value})
def edit_contact(request, id):
    value = userContact.objects.get(id=id)
    value.FullName = request.POST['name']
    value.Email = request.POST['email']
    value.PhoneNo = request.POST['tel']
    value.Address = request.POST['home']
    value.save()
    return redirect('contact')
def delete(request,id):
    value = userContact.objects.get(id=id)
    return render(request, 'phoneContact/delete.html', {'value':value})
def delete_contact(request,id):
    value =  userContact.objects.get(id=id)
    value.delete()
    return redirect('contact')
def back(request):
    return render(request, "phoneContact/index.html", {})
def search(request):
    search = request.POST['search']
    search_contact = userContact.objects.filter(FullName__contains=search)
    if request.method == 'POST':
        return render(request, 'phoneContact/search.html', {'search':search_contact})
    else:
         return render(request, 'phoneContact/search.html',{})
