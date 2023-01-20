#============================ imports ============================
from django.shortcuts import render
from django.shortcuts import render,redirect
from . serializers import SignUpSerializer
from . models import SignUp_info
from rest_framework.response import Response
from rest_framework.views import APIView
import sqlite3
from pathlib import Path
from django.core.files.storage import FileSystemStorage
import os
from django.db.models import Q
from time import *
import random
import shutil
#============================ imports ============================


BASE_DIR = Path(__file__).resolve().parent.parent


#====================================================== Home / Profile  =====================================================

class Home(APIView):
      def get(self, request):
        #-------------------- Checking for cookies -----------------------
        if '32ewrdszxewr' in request.COOKIES:
         user_check = request.COOKIES['32ewrdszxewr']
         info = SignUp_info.objects.filter(id=user_check).values()[0]
        #------------------- Checking for cookies ------------------------

         rand = random.randint(0,1000)
         return render(request, 'index.html', {"Data":info,'Rand':rand})
        else:
         return redirect("login")

class Profile(APIView):
      def get(self, request):
        #--------------------- Checking for cookies ------------------------
        if '32ewrdszxewr' in request.COOKIES:
         user_check = request.COOKIES['32ewrdszxewr']
         info = SignUp_info.objects.filter(id=user_check).values()[0]["id"]     
        #--------------------- Checking for cookies ------------------------

         rand = random.randint(0,1000)
         return render(request, 'Profile.html', {"id":info,"Rand":rand})
        else:
         return redirect("login")
      def post(self, request):
        #--------------------- Checking for cookies -----------------------
        if '32ewrdszxewr' in request.COOKIES:
         user_check = request.COOKIES['32ewrdszxewr']
         info = SignUp_info.objects.filter(id=user_check).values()[0]["id"]
        #-------------------- Checking for cookies -----------------------
        
        
        #------------------------------Replacing Profile Image---------------------------------
         uploading_file = request.FILES['New_Img']
         fs = FileSystemStorage()
         try:
          os.remove(f"{BASE_DIR}//media//Users//{info}.jpg")
         except:
            pass
         fs.save("Users//"+str(info)+".jpg",uploading_file)
         return redirect("defult") 
        else:
         return redirect("login")
        #------------------------------Replacing Profile Image---------------------------------


#====================================================== Home / Profile  =====================================================



#====================================================== Register / Login  =====================================================

class Login(APIView):
      def get(self, request):
         return render(request, 'login.html')
      def post(self, request):
        try:
         #---------------------------- Checking username existence ---------------------------   
          data = SignUp_info.objects.get(User=request.data['User'])
         #---------------------------- Checking username existence ---------------------------  

          try:
         #----------------------------- Checking username and password matches ----------------------------
            data = SignUp_info.objects.get(User=request.data['User'], Password=request.data['Password']).id
            response =  Response('Good')
            response.set_cookie('32ewrdszxewr',data )
         #----------------------------- Checking username and password matches -----------------------------  

            return response
          except:   
            return Response("Err0")
        except:
            return Response('Err1')

         
         
class Logout(APIView):
    def get(self , request):
    #---------------------- Deleting cookies -----------------------
      response = redirect("login")
      response.delete_cookie('32ewrdszxewr')
      return response
    #--------------------- Deleting cookies ------------------------

class Register(APIView):
      def get(self, request):
          return render(request, 'register.html')
      def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        user = request.data["User"]
        try:
         #------------------------ Checking if usename already exit's ---------------------------  
         data = SignUp_info.objects.get(User=user)
         return Response("Err2")
         #------------------------ Checking if usename already exit's ---------------------------   

        except:    
          if serializer.is_valid():  
         #------------------------ Creating a new user if usename is free ------------------------ 
           serializer.save()    
           id = SignUp_info.objects.latest('id')
           shutil.copyfile(f'{BASE_DIR}/static/Default.jpg',f'{BASE_DIR}/media/Users/{str(id.id)}.jpg')
           response = Response(str(id.id))
           response.set_cookie('32ewrdszxewr', str(id.id))
           return response
         #------------------------ Creating a new user if usename is free -------------------------
           
          else:
         #------------------------- User input error -------------------------- 
           return Response("Err3")
         #------------------------- User input error --------------------------  

#====================================================== Register / Login =====================================================


