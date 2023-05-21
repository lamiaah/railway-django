# django-speech

#  setup project in your command line
  
1#    git clone https://github.com/lamiaah/django-speech

2#    cd django-speech

3#    python -m venv   your_env_name

 3##    your_env_name\Scripts\activate
 
4#    pip install -r req.txt

5#    got to folder convert -> Api -> views  change  chat to convert 

     from Convert.models import Chat
     from Convert.Api.serializers import ChatSerializers
      edit:
      from convert.models import Convert
      from convert.Api.serializers import ConvertSerializers
      and then in function-- ConvertSerializers
      
  6# python manage.py makemigrations
  
  7# python manage.py migrate
  
  8# python manage.py runserver
  
  when run programm must activate your_env
  or choese it in interpreter( ctrl+shift+p)
      
