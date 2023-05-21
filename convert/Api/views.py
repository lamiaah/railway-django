from rest_framework import status ,generics 
from convert.models import Convert
from convert.Api.serializers import ConvertSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from convert import process



@api_view(['GET','POST'])
def apirecord(request):

  if request.method == 'GET':
    samples = Convert.objects.last()
    serializer= ConvertSerializers(samples , many= False)
    return Response(serializer.data) 


  #  upload file 
  if request.method =='POST':
    serializer = ConvertSerializers(data= request.data)
    if serializer.is_valid():
      serializer.save()
      # pass obj to (speech to text) process
      process.file(serializer.data['id'])
      samples = Convert.objects.last()
      # return text in response
      serializer = ConvertSerializers(samples , many= False)
      return Response(serializer.data) 

      #  return Response(samples, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
  