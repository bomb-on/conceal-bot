import requests
import json
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from poolModels import pool, poolBase
 
engine = create_engine('sqlite:///poolData.db')
poolBase.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def main():
    allPools = session.query(pool).all()
    totalPools = len(allPools)
    for poolNumber in range(0,totalPools):
        poolName = allPools[poolNumber].name
        poolURL = allPools[poolNumber].url
        poolType = allPools[poolNumber].type
        print("INFO: Getting data for pool {} at URL {} and type {}".format(poolName, poolURL, poolType))
        response = requests.get(poolURL)
        if response.status_code != 200:
            allPools[poolNumber].miners = 0
            allPools[poolNumber].hashrate = 0
            continue
        print("response: {}".format(response.status_code))
        if poolType == "normal":
            dataLocation = "pool"
            keyHashrate = "hashrate"
        else:
            dataLocation = "pool_statistics"
            keyHashrate = "hashRate"       
        data = response.json()
        poolData = data[dataLocation]
        poolMiners = int(poolData["miners"])
        poolHashrate = int(poolData[keyHashrate])
        allPools[poolNumber].miners = poolMiners
        allPools[poolNumber].hashrate = poolHashrate           
        print("DATA: {} miners {}".format(poolName, poolMiners))
        print("DATA: {} hashrate {}".format(poolName, poolHashrate))    
    session.commit()
    print("updated database")

while 1:
    try:
        main()
        print("INFO: 120 second pause")
        time.sleep(120)
    except:
        continue