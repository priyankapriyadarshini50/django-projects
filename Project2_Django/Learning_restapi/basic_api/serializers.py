from rest_framework import serializers
from basic_api.models import Article


# class ArticleSerializer(serializers.Serializer):
    #title = serializers.CharField(max_length=100)
    #author = serializers.CharField(max_length=30)
    #email = serializers.EmailField(max_length=30)
    #date = serializers.DateTimeField()

    #def create(self, validated_data):
        #return Article.objects.create(validated_data)

    #def update(self, instance, validated_data):
        #instance.title = validated_data.get('title', instance.title)
        #instance.author = validated_data.get('author', instance.author)
        #instance.email = validated_data.get('email', instance.email)
        #instance.date = validated_data.get('date', instance.date)
        #instance.save()
        #return instance

# NOW WE ARE GOING TO USER SERIALIZERMODEL CLASS SO THAT WE CAN CHOOSE SPECIFIC FIELDS TO PARSE DATA
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']
        # fields = '__all__'

