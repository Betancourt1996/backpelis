import imp
from django.shortcuts import render
import requests, json
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from .models import Generos, Opinions,Usuarios
from .serializers import GenerosSerializer, OpinionsSerializer,UsuariosSerializer
import random
# Create your views here.
# Create your views here.
def index(request):
    #return HttpResponse("<h2>web</h2>")
    data = dict()
    data.update({'title': 'API'})
    return render(request,"index.html",data)

def generos(request):
    #return HttpResponse("<h2>web</h2>")
    data = dict()
    data.update({'title': 'generos'})
    return render(request,"index.html",data)
def usuarios(request):
    #return HttpResponse("<h2>web</h2>")
    data = dict()
    data.update({'title': 'usuarios'})
    return render(request,"index.html",data)


class GeneroList(APIView):
    #GET list 
    def get(self, request, format=None):
       #Obtener todos los datos
       generos = Generos.objects.all().order_by("nombre")
       #many=true, devolver  arreglo json
       serializer = GenerosSerializer(generos,many=True)
       #return JsonResponse(serializer.data,safe=False)
       return Response(serializer.data)

#--------------------------------------------
class GeneroDetail(APIView):
    
    #Retrieve, update or delete a snippet instance.
    
    def get_object(self, pk):
        try:
            return Generos.objects.get(pk=pk)
        except Generos.DoesNotExist:
            raise Http404
    #GET un objeto por pk
    def get(self, request, pk, format=None):
        genero = self.get_object(pk)
        serializer = GenerosSerializer(genero)
        return Response(serializer.data)
    #UPDATE los datos pk=?pk
    def put(self, request, pk, format=None):
        genero = self.get_object(pk)
        serializer = GenerosSerializer(genero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE ,elimina
    def delete(self, request, pk, format=None):
        try:            
            genero = self.get_object(pk).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
#------------------------------------------


class UsuarioList(APIView):
    #GET list 
    def get(self, request, format=None):
       #Obtener todos los datos
       usuarios = Usuarios.objects.all().order_by("usuario")
       #many=true, devolver  arreglo json
       serializer = UsuariosSerializer(usuarios,many=True)
       #return JsonResponse(serializer.data,safe=False)
       return Response(serializer.data)

class UsuarioDetail(APIView):
    
    #Retrieve, update or delete a snippet instance.
    
    def get_object(self, pk):
        try:
            return Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            raise Http404
    #GET un objeto por pk
    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuariosSerializer(usuario)
        return Response(serializer.data)
    #UPDATE los datos  pk=?pk
    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuariosSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE ,elimina
    def delete(self, request, pk, format=None):
        try:            
            usuario = self.get_object(pk).delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

def peliculas(request):
    url = requests.get("https://peliculas-84e27-default-rtdb.firebaseio.com/peliculas.json")
    text = url.text
    data = json.loads(text)
    return JsonResponse(data,safe=False)

def peliculasDetails(request,pk):
    url = requests.get("https://peliculas-84e27-default-rtdb.firebaseio.com/peliculas/"+str(pk)+".json")
    text = url.text
    data = json.loads(text)
    return JsonResponse(data)

def peliculasGenero(request,pk):
    url = requests.get("https://peliculas-84e27-default-rtdb.firebaseio.com/peliculas.json?orderBy=%22genero%22&equalTo="+str(pk))
    text = url.text
    data = json.loads(text)
    data2=[]
    for key  in data.keys():
        data2.append(data[key])    
    return JsonResponse(data2,safe=False)

class OpinionsList(APIView):
    #GET list 
    def get(self, request, format=None):
       #Obtener todos los datos
       opinions = Opinions.objects.all().order_by("id")
       #many=true, devolver  arreglo json
       serializer = OpinionsSerializer(opinions,many=True)
       #return JsonResponse(serializer.data,safe=False)
       return Response(serializer.data)

def peliculasOpinion(request,pk):
    url = requests.get("https://peliculas-84e27-default-rtdb.firebaseio.com/peliculas.json?orderBy=%22opinion%22&equalTo="+str(pk))
    text = url.text
    data = json.loads(text)
    data2=[]
    for key  in data.keys():
        data2.append(data[key])    
    return JsonResponse(data2,safe=False)

def peliculasRandom(request):
    random_number = random.randint(0, 999)
    url = requests.get("https://peliculas-84e27-default-rtdb.firebaseio.com/peliculas/"+str(random_number)+".json")    
    text = url.text
    data = json.loads(text)
    return JsonResponse(data,safe=False)