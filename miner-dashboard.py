#!/usr/bin/env python
# Description: Quick and dirty ethermine.org dashboard
# Author: syntacticNaCL

import requests
import json
import os
import time

# colors (bc pretty colors)
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

startTime = time.time()
callDelay = 180.0

def convertHashrate(hashrate):
    return round((hashrate /1000000), 3)

def convertTime(epoch):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(epoch)))

if "ETH_MINER_ADDRESS" and "ETH_MINER_WORKER" in os.environ:
    while True:
        baseUrl = "https://api.ethermine.org"
        ethAddr = os.environ['ETH_MINER_ADDRESS']
        worker = os.environ['ETH_MINER_WORKER'] 

        minerStats = requests.get(baseUrl + '/miner/' + ethAddr + '/worker/' + worker + '/currentStats')
        poolStats = requests.get(baseUrl + '/poolStats/')

        if(poolStats.ok):

            pool = json.loads(poolStats.content)
            poolData = pool["data"]
            mostRecentBlock = poolData["minedBlocks"][0]
            price = pool["data"]["price"]
            
            print "Ethermine Pool Data:\n"
            print "Most recent block mined: # {0} at {1}\n".format(mostRecentBlock["number"],convertTime(mostRecentBlock["time"]))
            print "Prices: \n USD: {0} BTC: {1}".format(price["usd"], price["btc"])
            print "\n"
            
        else:
            # Throw error if no 200 response received
            poolStats.raise_for_status()

        if(minerStats.ok):

            miner = json.loads(minerStats.content)
            minerData = miner["data"]
            
            print G+"{0} Dashboard --- {1}\n".format(worker.title(),convertTime(minerData["time"]))
            print O+"Average Hashrate: {0}".format(convertHashrate(minerData["averageHashrate"]))
            print "Reported Hashrate: {0}".format(convertHashrate(minerData["reportedHashrate"]))
            print G+"Current Hashrate: {0}\n".format(convertHashrate(minerData["currentHashrate"]))
            print "Valid Shares: {0}".format(minerData["validShares"])
            print R+"Invalid Shares: {0}".format(minerData["invalidShares"])
            print O+"Stale Shares: {0}".format(minerData["staleShares"])
            print W+"Last Seen by Pool: {0}".format(convertTime(minerData["lastSeen"]))

        else:
            # Throw error if no 200 response received
            minerStats.raise_for_status()

        print G+"\nZzzzzzzzzzz"

        # Sleep until next call
        time.sleep(callDelay - ((time.time() - startTime) % callDelay))

        # Refresh output
        os.system('cls' if os.name == 'nt' else 'clear')
        
else:
    print R+"Environment variable(s) `ETH_MINER_ADDRESS` and/or `ETH_MINER_WORKER` cannot be found. Please set it to your Ethereum wallet address to continue"

