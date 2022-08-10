from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from joblib import load
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.models import Group
import pandas as pd
import sqlite3

model = load('./models/model.sav')

def res(request):
    return render(request, 'res.html')



def predict(request):
    if request.method == 'POST':
        marque = request.POST['marque']
        taille_ecran = float(request.POST['taille ecran'])
        type_ecran = request.POST['type ecran']
        type_processeur = request.POST['type cpu']
        nb_cores = float(request.POST['nb cores'])
        cpu_frequency = float(request.POST['cpu frequency'])
        ram = float(request.POST['ram'])
        HDD = float(request.POST['HDD'])
        SSD = float(request.POST['SDD'])
        carte_graphique = request.POST['carte graphique']

        if marque == 'Acer':
            m = 0
        if marque == 'Asus':
            m = 1
        if marque == 'Dell':
            m = 2
        if marque == 'Hp':
            m = 3
        if marque == 'Lenovo':
            m = 4
        if marque == 'Msi':
            m = 5
        if marque == 'Other':
            m = 6

        if type_ecran == "HD":
            display = 1
        elif type_ecran == "Full HD":
            display = 0
        else:
            display = 2

        if type_processeur == "Intel":
            cpu_type = 1
        elif type_processeur == "AMD":
            cpu_type = 0
        else:
            cpu_type = 2

        if carte_graphique == "Graphique Intégrée":
            graphic_card = 1
        elif carte_graphique == "AMD Radeon":
            graphic_card = 0
        else:
            graphic_card = 2

        dict = {"marque": [m], "taille ecran": [taille_ecran], "type ecran": [display], "type cpu": [cpu_type],
                "nb cores": [nb_cores], "cpu frequency": [cpu_frequency], "ram": [ram], "HDD": [HDD], "SSD": [SSD],
                "carte graphique": [graphic_card]}
        df = pd.DataFrame(dict)
        print(df)

        price = model.predict(df)
        print(price)

        return render(request, 'main.html', {'result': price[0]})
    else:
        return render(request, 'main.html')


def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('comp',f=1)
        else:
            messages.info(request, 'username or password is incorrect')
    else:
        return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')
def dashboarddesktop(request):
    return render(request, 'dashboard_desktop.html')
def dashboardsmartphone(request):
    return render(request, 'dashboard_smartphone.html')

def registerForm(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')

            if request.user.groups.filter(name='admin').exists():
                group = Group.objects.get(name='admin')

            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username + ' !')
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


"""def comp(request):
    data = pd.read_excel('C:/Users/trabe/OneDrive/Bureau/my_data1.xlsx')
    data = data.sort_values(by= 'prix' )
    if request.method == 'POST' :
        nom = []
        store = []
        link = []
        img = []
        prix = []
        recomended_nom = []
        recomended_store = []
        recomended_link = []
        recomended_img = []
        recomended_prix = []
        r = 0
        referance = request.POST['referance']
        for i in data.index :
            if data['reference'][i] == referance :
                nom.append(data['nom'][i])
                store.append(data['store'][i])
                link.append(data['link'][i])
                img.append(data['image link'][i])
                prix.append(data['prix'][i])

                if len(prix) > 0 and r == 0:
                    r = 1
                    for i in data.index :
                        print(data['prix'][i])
                        print(prix[0])
                        if float(data['prix'][i]) < float(prix[0])+30 and float(data['prix'][i]) > float(prix[0])  - 30 :
                            recomended_nom.append(data['nom'][i])
                            recomended_store.append(data['store'][i])
                            recomended_link.append(data['link'][i])
                            recomended_img.append(data['image link'][i])
                            recomended_prix.append(data['prix'][i])

        dict = zip(nom, store, link, img,prix)
        recomended = zip(recomended_nom,recomended_store,recomended_link,recomended_img,recomended_prix)
        context = {'dict': dict , 'recomended': recomended}
    else :
        dict = zip( data['nom'],data['store'],data['link'],data['image link'],data['prix'] )
        context = {'dict':dict}
       # print(dict)

    return render(request, 'comp.html',context)"""

def comp(request,f):
    con = sqlite3.connect(r'C:\Users\trabe\OneDrive\Bureau\djangoProject1\db.sqlite3')


    if f == '2' :
        data = pd.read_sql_query("select * from pred_product WHERE cast (prix as float ) > 1000 and cast (prix as float ) < 1500  ", con)
    elif f == '3' :
        data = pd.read_sql_query("select * from pred_product WHERE cast (prix as float ) > 1500 and cast (prix as float ) < 2000   ", con)
    elif f == '4' :
        data = pd.read_sql_query("select * from pred_product WHERE cast (prix as float ) > 2000  ", con)
    else :
        data = pd.read_sql_query("select * from pred_product WHERE cast (prix as float ) < 1000  ", con)

    data = data.sort_values(by='prix')



    nom = []
    img = []
    store1 = []
    store2 = []
    prix1 = []
    prix2 = []
    link1 = []
    link2 = []
    ref = []
    if request.method == "POST" :
        referance = request.POST['referance']
        data = pd.read_sql_query("select * from pred_product ", con )
        recomended_nom = []
        recomended_store = []
        recomended_link = []
        recomended_img = []
        recomended_prix = []
        r = 0
        for i in range(len(data)):
            if data['reference'][i] == referance and len(nom) == 0 :
                nom.append(data['nom'][i])
                store1.append(data['store'][i])
                img.append(data['image_link'][i])
                link1.append(data['link'][i])
                prix1.append(data['prix'][i])
                ref.append(data['reference'][i])
            elif data['reference'][i] == referance and len(nom) == 1 :
                store2.append(data['store'][i])
                prix2.append(data['prix'][i])
                link2.append(data['link'][i])
            if len(prix1) > 0 and r == 0:
                r = 1
                for i in data.index:
                    if float(data['prix'][i]) < float(prix1[0]) + 30 and float(data['prix'][i]) > float(prix1[0]) - 30 and referance != data['reference'][i] and len(recomended_nom) <= 10:
                        recomended_nom.append(data['nom'][i])
                        recomended_store.append(data['store'][i])
                        recomended_link.append(data['link'][i])
                        recomended_img.append(data['image_link'][i])
                        recomended_prix.append(data['prix'][i])
        recomended = zip(recomended_nom, recomended_store, recomended_link, recomended_img, recomended_prix)
        if len(store2) == 0 :
            dict1 = zip(nom, store1, link1, img, prix1)
            context = {'dict1': dict1, 'recomended': recomended}
        else :
            dict1 = zip(nom, store1, store2, link1, link2, img, prix1, prix2,ref)
            context = {'dict': dict1, 'recomended': recomended}

    else :
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data['reference'][i] == data['reference'][j]:
                    nom.append(data['nom'][i])
                    img.append(data['image_link'][i])
                    store1.append(data['store'][i])
                    store2.append(data['store'][j])
                    prix1.append(data['prix'][i])
                    prix2.append(data['prix'][j])
                    link1.append(data['link'][i])
                    link2.append(data['link'][j])
                    ref.append(data['reference'][i])
        dict = zip(nom ,store1 , store2, link1, link2, img, prix1,prix2,ref)
        context = {'dict': dict}
    return render(request, 'comp.html',context)

def affiche(request , ref) :
    nom = []
    img=[]
    prix = []
    ecran_size = []
    ecran_type = []
    cpu_type = []
    cpu_frequency = []
    ram = []
    rom = []
    carte_graphic = []
    ref_carte_graphic = []
    sys_exploitation = []
    garanti = []
    store = []
    link =[]

    prix2 = []
    ecran_size2 = []
    ecran_type2 = []
    cpu_type2 = []
    cpu_frequency2 = []
    ram2 = []
    rom2 = []
    carte_graphic2 = []
    ref_carte_graphic2 = []
    sys_exploitation2 = []
    garanti2 = []
    store2 = []
    link2 = []
    r = 0

    data = pd.read_excel('C:/Users/trabe/OneDrive/Bureau/my_data1.xlsx')
    print(ref)
    for i in range(len(data)):
        if data['reference'][i] == ref and r==0 :
            nom.append(data['nom'][i])
            img.append(data['image link'][i])
            prix.append(data['prix'][i])
            ecran_size.append(data['taille ecran'][i])
            ecran_type.append(data['type ecran'][i])
            cpu_type.append(data['type processeur'][i])
            cpu_frequency.append(data['referance processeur'][i])
            ram.append(data['ram'][i])
            rom.append(data['rom'][i])
            carte_graphic.append(data['carte graphique'][i])
            ref_carte_graphic.append(data['Referance carte graphique'][i])
            sys_exploitation.append(data["Systeme d'exploitation"][i])
            garanti.append(data['garanti'][i])
            store.append(data['store'][i])
            link.append(data['link'][i])
            r=1
        elif data['reference'][i] == ref and r==1 :
            prix2.append(data['prix'][i])
            ecran_size2.append(data['taille ecran'][i])
            ecran_type2.append(data['type ecran'][i])
            cpu_type2.append(data['type processeur'][i])
            cpu_frequency2.append(data['referance processeur'][i])
            ram2.append(data['ram'][i])
            rom2.append(data['rom'][i])
            carte_graphic2.append(data['carte graphique'][i])
            ref_carte_graphic2.append(data['Referance carte graphique'][i])
            sys_exploitation2.append(data["Systeme d'exploitation"][i])
            garanti2.append(data['garanti'][i])
            store2.append(data['store'][i])
            link2.append(data['link'][i])

    dict = zip(nom,img,prix,ecran_size,ecran_type,cpu_type,cpu_frequency,ram,rom,carte_graphic,ref_carte_graphic,sys_exploitation,garanti,store,link,prix2,ecran_size2,ecran_type2,cpu_type2,cpu_frequency2,ram2,rom2,carte_graphic2,ref_carte_graphic2,sys_exploitation2,garanti2,store2,link2)
    context={'dict':dict}
    print(len(nom))
    return render(request,'affiche.html',context)


def comp_burreau(request):
    con = sqlite3.connect(r'C:\Users\trabe\OneDrive\Bureau\djangoProject1\db.sqlite3')



    data = pd.read_sql_query("select * from pred_burreau", con)

    data = data.sort_values(by='prix')



    nom = []
    img = []
    store1 = []
    store2 = []
    prix1 = []
    prix2 = []
    link1 = []
    link2 = []
    ref = []
    if request.method == "POST" :
        referance = request.POST['referance']
        data = pd.read_sql_query("select * from pred_burreau ", con )
        recomended_nom = []
        recomended_store = []
        recomended_link = []
        recomended_img = []
        recomended_prix = []
        r = 0
        for i in range(len(data)):
            if data['reference'][i] == referance and len(nom) == 0 :
                nom.append(data['nom'][i])
                store1.append(data['store'][i])
                img.append(data['image_link'][i])
                link1.append(data['link'][i])
                prix1.append(data['prix'][i])
                ref.append(data['reference'][i])
            elif data['reference'][i] == referance and len(nom) == 1 :
                store2.append(data['store'][i])
                prix2.append(data['prix'][i])
                link2.append(data['link'][i])
            if len(prix1) > 0 and r == 0:
                r = 1
                for i in data.index:
                    if float(data['prix'][i]) < float(prix1[0]) + 30 and float(data['prix'][i]) > float(prix1[0]) - 30 and referance != data['reference'][i] and len(recomended_nom) <= 10:
                        recomended_nom.append(data['nom'][i])
                        recomended_store.append(data['store'][i])
                        recomended_link.append(data['link'][i])
                        recomended_img.append(data['image_link'][i])
                        recomended_prix.append(data['prix'][i])
        recomended = zip(recomended_nom, recomended_store, recomended_link, recomended_img, recomended_prix)
        if len(store2) == 0 :
            dict1 = zip(nom, store1, link1, img, prix1)
            context = {'dict1': dict1, 'recomended': recomended}
        else :
            dict1 = zip(nom, store1, store2, link1, link2, img, prix1, prix2,ref)
            context = {'dict': dict1, 'recomended': recomended}

    else :
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data['reference'][i] == data['reference'][j]:
                    nom.append(data['nom'][i])
                    img.append(data['image_link'][i])
                    store1.append(data['store'][i])
                    store2.append(data['store'][j])
                    prix1.append(data['prix'][i])
                    prix2.append(data['prix'][j])
                    link1.append(data['link'][i])
                    link2.append(data['link'][j])
                    ref.append(data['reference'][i])
        #print(ref)
        dict = zip(nom ,store1 , store2, link1, link2, img, prix1,prix2,ref)
        context = {'dict': dict}
    return render(request, 'comp_burreau.html',context)


def comp_smartphone(request):
    con = sqlite3.connect(r'C:\Users\trabe\OneDrive\Bureau\djangoProject1\db.sqlite3')



    data = pd.read_sql_query("select * from pred_smartphone", con)

    data = data.sort_values(by='prix')



    nom = []
    img = []
    store1 = []
    store2 = []
    prix1 = []
    prix2 = []
    link1 = []
    link2 = []
    ref = []
    if request.method == "POST" :
        referance = request.POST['referance']
        data = pd.read_sql_query("select * from pred_smartphone ", con )
        recomended_nom = []
        recomended_store = []
        recomended_link = []
        recomended_img = []
        recomended_prix = []
        r = 0
        for i in range(len(data)):
            if data['reference'][i] == referance and len(nom) == 0 :
                nom.append(data['nom'][i])
                store1.append(data['store'][i])
                img.append(data['image_link'][i])
                link1.append(data['link'][i])
                prix1.append(data['prix'][i])
                ref.append(data['reference'][i])
            elif data['reference'][i] == referance and len(nom) == 1 :
                store2.append(data['store'][i])
                prix2.append(data['prix'][i])
                link2.append(data['link'][i])
            if len(prix1) > 0 and r == 0:
                r = 1
                for i in data.index:
                    if float(data['prix'][i]) < float(prix1[0]) + 30 and float(data['prix'][i]) > float(prix1[0]) - 30 and referance != data['reference'][i] and len(recomended_nom) <= 10:
                        recomended_nom.append(data['nom'][i])
                        recomended_store.append(data['store'][i])
                        recomended_link.append(data['link'][i])
                        recomended_img.append(data['image_link'][i])
                        recomended_prix.append(data['prix'][i])
        recomended = zip(recomended_nom, recomended_store, recomended_link, recomended_img, recomended_prix)
        if len(store2) == 0 :
            dict1 = zip(nom, store1, link1, img, prix1)
            context = {'dict1': dict1, 'recomended': recomended}
        else :
            dict1 = zip(nom, store1, store2, link1, link2, img, prix1, prix2,ref)
            context = {'dict': dict1, 'recomended': recomended}

    else :
        for i in range(len(data)):
            nom.append(data['nom'][i])
            img.append(data['image_link'][i])
            store1.append(data['store'][i])

            prix1.append(data['prix'][i])

            link1.append(data['link'][i])

            ref.append(data['reference'][i])

        dict = zip(nom ,store1 ,  link1,  img, prix1,ref)
        #print(tuple(dict))
        context = {'dict': dict}
    return render(request, 'comp_smartphone.html',context)
def affiche_burreau(request , ref) :
    nom = []
    img=[]
    prix = []

    cpu_type = []
    cpu_frequency = []
    ram = []
    rom = []
    carte_graphic = []
    ref_carte_graphic = []
    sys_exploitation = []
    garanti = []
    store = []
    link =[]

    prix2 = []

    cpu_type2 = []
    cpu_frequency2 = []
    ram2 = []
    rom2 = []
    carte_graphic2 = []
    ref_carte_graphic2 = []
    sys_exploitation2 = []
    garanti2 = []
    store2 = []
    link2 = []
    r = 0

    con = sqlite3.connect(r'C:\Users\trabe\OneDrive\Bureau\djangoProject1\db.sqlite3')

    data = pd.read_sql_query("select * from pred_burreau", con)
    #print(ref)
    for i in range(len(data)):
        if data['reference'][i] == ref and r==0 :
            nom.append(data['nom'][i])
            img.append(data['image_link'][i])
            prix.append(data['prix'][i])

            cpu_type.append(data['type_processeur'][i])
            cpu_frequency.append(data['reference_processeur'][i])
            ram.append(data['ram'][i])
            rom.append(data['rom'][i])
            carte_graphic.append(data['carte_graphique'][i])
            ref_carte_graphic.append(data['reference_carte_graphique'][i])
            sys_exploitation.append(data["systeme_exploitation"][i])
            garanti.append(data['garanti'][i])
            store.append(data['store'][i])
            link.append(data['link'][i])
            r=1
        elif data['reference'][i] == ref and r==1 :
            prix2.append(data['prix'][i])

            cpu_type2.append(data['type_processeur'][i])
            cpu_frequency2.append(data['reference_processeur'][i])
            ram2.append(data['ram'][i])
            rom2.append(data['rom'][i])
            carte_graphic2.append(data['carte_graphique'][i])
            ref_carte_graphic2.append(data['reference_carte_graphique'][i])
            sys_exploitation2.append(data["systeme_exploitation"][i])
            garanti2.append(data['garanti'][i])
            store2.append(data['store'][i])
            link2.append(data['link'][i])

    dict = zip(nom,img,prix,cpu_type,cpu_frequency,ram,rom,carte_graphic,ref_carte_graphic,sys_exploitation,garanti,store,link,prix2,cpu_type2,cpu_frequency2,ram2,rom2,carte_graphic2,ref_carte_graphic2,sys_exploitation2,garanti2,store2,link2)
    context={'dict':dict}
    print(len(nom))
    return render(request,'affiche_burreau.html',context)

# Create your views here.

