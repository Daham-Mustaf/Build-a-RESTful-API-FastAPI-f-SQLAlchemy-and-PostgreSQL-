from database import Base, engine
from models import Item


print('creatim database ...')
Base.metadata.create_all(engine)