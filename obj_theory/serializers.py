('Section:B=2')

from rest_framework import serializers
from . import models

class BookSerializer(serializers.BookSerializer):
    class Meta :
        model = models.Book
        fields = ('title', 'author', 'publication_year')
        read_only_fields = ('title', 'author', 'publication_year')


('Section:B=3')

loops = ('for', 'while')
loops = ('for a particular in many items')
print('item')

for cat in 'animals' :
    print('animals')

#while = ('a conditon is set, in as much that is meant then the result is out')
    
x = 0
while x < 0:
    print(x)
    

('Section:B=4')

conditional_statement = ('if', 'else')
conditional_statement = ('elif')

('if we have a set of lists and if we begin check for a prticular in that lists elif until not there else get result')