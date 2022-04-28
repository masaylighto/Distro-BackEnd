import json
from os import link
from urllib import response
from rest_framework import serializers,viewsets,permissions,response
from rest_framework.decorators import action

from polls.models import *;

class links_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = links        
        fields = ['name', 'link']
class Translations_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:       
        fields = ["page_name","key","value"]
class Features_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:       
       fields = ["name","description"]
class Distro_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:   
        fields = ['name',"Desc","link"]    
        





class Features_Set(viewsets.ViewSet):
    queryset = Features.objects.all()
    serializer_class = Features_Serializer
    permission_classes = [permissions.AllowAny]  
    @action(detail=False, methods=['get'],url_path="Get")
    def Get(self,request):
        #get request parameters
        try:          
            language =request.GET.get('language')            
        except:
            return response.Response({"State":"Failed","Error":"missing request paramters"})   
        #get data from db that match the condtions
        try:                
            data=(Features.objects.filter(language=language).values("name","description"))
        except BaseException as e:
            print(e)           
            return response.Response({"State":"Failed","Error":"no data match the condtions"}) 
        return response.Response({"State":"Done","Data":data})

class links_Set(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Website_link to be viewed
    """
    queryset = links.objects.all()
    serializer_class = links_Serializer
    permission_classes = [permissions.AllowAny]
    @action(detail=False, methods=['get'],url_path="Get")
    def Get(self,request):
        #get request parameters
        try:          
            language =request.GET.get('language')            
        except:
            return response.Response({"State":"Failed","Error":"missing request paramters"})   
        #get data from db that match the condtions
        try:                
            data=list(links.objects.filter(language=language).values_list("name","link").distinct())
        except BaseException as e:
            print(e)
            return response.Response({"State":"Failed","Error":"no data match the condtions"})     
        return response.Response({"State":"Done","Data":data})
    
class Translations_Set(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Translations to be viewed
    """
    queryset = Translation.objects.all()
    serializer_class = Translations_Serializer
    permission_classes = [permissions.AllowAny]      
    @action(detail=False, methods=['get'],url_path="Get")
    def Get(self,request):
        #get request parameters
        try: 
            page_name=request.GET.get('page_name')
            language=request.GET.get('language')           
        except:
            return response.Response({"State":"Failed","Error":"missing request paramters"})   
        #get data from db that match the condtions
        try:       
            data=dict(Translation.objects.filter(page_name=page_name,language=language).values_list("key","value"))
        except BaseException as e:
            print(e)        
            return response.Response({"State":"Failed","Error":"no data match the condtions"})   
        return response.Response({"State":"Done","Data":data})
    @action(detail=False, methods=['get'],url_path="GetLanguages")    
    def GetLanguages(self,request):  
        #get data from db that match the condtions
        try:
            #get all language and convert them to list for sake of encoding to json
            data=list(Translation.objects.distinct().values("language"))
        except BaseException as e:
            print(e)
            return response.Response({"State":"Failed","Error":"no data match the condtions"})      
        return response.Response({"State":"Done","Data":data})
class Distro_Set(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Contributors to be viewed
    """
    queryset = Distro.objects.all()
    serializer_class = Distro_Serializer
    permission_classes = [permissions.AllowAny]
    @action(detail=False, methods=['get'],url_path="Get")
    def Get(self,request):
        #get request parameters
        try:
            language =request.GET.get('language')            
        except:
            return response.Response({"State":"Failed","Error":"missing request paramters"})   
        #get data from db that match the condtions
        try:
            data=Distro.objects.values("name","Desc","link")
        except BaseException as e:
            print(e)
            return response.Response({"State":"Failed","Error":"no data match the condtions"})      
        #return it as response    
        return response.Response({"State":"Done","Data":data})
