import requests
import json
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from poolModels import pool, poolBase
 
engine = create_engine('sqlite:///poolData.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
poolBase.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Insert a Person in the person table
new_pool = pool(url='https://api.dreamitsystems.com:1443/cxapi/live_stats', name='Official Pool', type="normal", poolurl='https://ccxpool.dreamitsystems.com')
session.add(new_pool)
new_pool = pool(url='https://ccx.go-mine.it/api/pool/stats', name='go mine it!', type="node", poolurl='https://ccx.go-mine.it/#/home')
session.add(new_pool)
new_pool = pool(url='https://ccx.scecf.org:21001/live_stats', name='SCECF', type="normal", poolurl='https://ccx.scecf.org/')
session.add(new_pool)
new_pool = pool(url='https://conceal.herominers.com/api/stats', name='herominers', type="normal", poolurl='https://conceal.herominers.com')
session.add(new_pool)
session.commit()
 
