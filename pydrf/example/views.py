from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.generics import GenericAPIView




# Create your views here.

#FBV 함수형 뷰
# @api_view(['GET'])
# def HelloAPI(Request):
#     return Response('hello world')

# @api_view(['GET','POST'])
# def booksAPI(request): #DB에 있는 데이터 시리얼라이저(json으로 변환)해서 화면에 표시 
#     if request.method == "GET":
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status = status.HTTP_200_OK)
    
#     elif request.method == "POST": #화면에 표시되어있는 직렬화된 데이터를 역직렬화하여 DB에 삽입 
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save() #DB에 저장 
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def bookAPI(request, bid):
#     book = get_object_or_404(Book, bid = bid)
#     serializer = BookSerializer(book) #DB 데이터 직렬화하기 
#     return Response(serializer.data, status=status.HTTP_200_OK)


#CBV 클래스형뷰

class HelloAPI(APIView):
    def get(self, request):
        return Response("Hello world")


class booksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response (serializer.data, status = status.HTTP_200_OK)
    def post(self , request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED )
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class bookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid = bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#mixin으로 post,get구현    
class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    #목록조회, mixins.ListModelMixin과 연결 
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    #도서정보추가, mixins.CreateModelMixin과 연결 
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid' #참조 
    
    #1개 목록조회, mixins.RetrieveModelMixin 연결 
    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    #1개 수정 
    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    #1개 삭제
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

#Generics
class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookAPIGenerics(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'

#Viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    