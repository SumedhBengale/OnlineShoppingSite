from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
import pyrebase


# Remember the code we copied from Firebase.
#This can be copied by clicking on the settings icon > project settings, then scroll down in your firebase dashboard
config = {
  'apiKey': "AIzaSyAHGoVJzGXpLBKR4yqCTNlVvYjVhBpDoBM",
  'authDomain': "onlineshoppingsite-89a1a.firebaseapp.com",
  'databaseURL': "https://onlineshoppingsite-89a1a-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "onlineshoppingsite-89a1a",
  'storageBucket': "onlineshoppingsite-89a1a.appspot.com",
  'messagingSenderId': "557035398725",
  'appId': "1:557035398725:web:ceb74573ffe9fe1d9ee52c",
  'measurementId': "G-E7JCH8LB2R"
};

#here we are doing firebase authentication
firebase=pyrebase.initialize_app(config)
auth = firebase.auth()
database=firebase.database()

def customer(request):
    fruits=database.child('data').child('inventory').child('fruits').get().val()
    if request.method == 'POST':
        avaliable=request.POST.get('av')
        name=request.POST.get('name')
        price=request.POST.get('price')

        print(avaliable)
        print(name)
        print(price)
        database.child("users").child(auth.current_user['localId']).child('cart').push({'name':name,'price':price})

    
    context={
        'results': render(request,'item.html'),
        'count': len(fruits),
        'fruits':fruits
    }
    return render(request,'customer.html',context)

def cart(request):
    return render(request,'cart.html')

def signin(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('pw')
        print(email)
        print(password)
        auth.sign_in_with_email_and_password(email, password)
        database.child("users").child(auth.current_user['localId']).set({'email':email})
        return redirect('/home')


    return render(request,'signin.html')
