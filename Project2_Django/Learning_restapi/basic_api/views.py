

from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics
from rest_framework import mixins
from django.http import Http404, HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ArticleGenericView(generics.GenericAPIView, mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class ArticleDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, pk):
        if pk:
            return self.retrieve(request, pk)
        else:
            raise Http404

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

######################################################################
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def article_list(request):
    # someone asking for data from our database
    if request.method == 'GET':
        # retrieve all the rows/entries from Article model (complex data types objects)
        articles = Article.objects.all()
        # Serializer converts the data stored in models to a python data structure(Here it is a dictionary)
        serializer = ArticleSerializer(articles, many=True)  # many=True for querySet
        # print(serializer.data)
        # But here we just serialize the 3 fields(id, title, author) as serializer.data returns 3 fields
        # JsonResponse converts Python data structures to json format
        response = JsonResponse(serializer.data, safe=False)
        # print(response.content)
        return response

    elif request.method == 'POST':
        # JSONParser() converts Json format to Python Data structure(dictionary)
        received_data = JSONParser().parse(request)
        print(received_data)
        # Here it works as deserializer as it converts Python data types to complex data types
        serializer = ArticleSerializer(data=received_data)

        # as we have received the data, we need to validate
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return JsonResponse(serializer.data, status=201)  # 201 created status
        else:
            return JsonResponse(serializer.erros, status=400)


@csrf_exempt
def article_details(request, pk):
    try:
        # retrieve a single article object from the database with primary key
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    # User is asking a particular data from database
    if request.method == 'GET':
        # convert the complex data type to python data structure for a single data query(single entry with the given pk)
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    # some wants to update the particular data entry/row
    elif request.method == 'PUT':
        # convert the json format to python data structure
        new_data_entry = JSONParser().parse(request)
        # article is existing row, new_data_entry the new data row
        # convert the python data structure to complex data types and replace it with the original data
        deserializer = ArticleSerializer(article, new_data_entry)
        # as we have received the data we need to validate
        if deserializer.is_valid():
            deserializer.save()
            return JsonResponse(deserializer.data, status=201)
        else:
            return JsonResponse(deserializer.errors, status=400)
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)

#####################################################################
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def article_apiview_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
#@authentication_classes(TokenAuthentication)
#@permission_classes([IsAuthenticated])
def article_apiview_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








        









