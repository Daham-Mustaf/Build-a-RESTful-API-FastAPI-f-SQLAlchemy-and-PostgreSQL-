from unicodedata import name
from models import Item

new_item = Item( name='Milk', description= 'good milk', price= 100, on_offer= True)
print(Item.__table__)