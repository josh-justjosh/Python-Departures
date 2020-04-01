print("This Programme uses")
import mlcd
import time
import datetime
import urllib
import re
import nredarwin 
from nredarwin.webservice import DarwinLdbSession
import json
import requests


def sortServices():     
    try:
        global board
        if des != None and ori != None:
            if incArr == True: board = darwin_session.get_station_board(CRS, rows=200, destination_crs=des, origin_crs=ori, include_arrivals=True)
            else: board = darwin_session.get_station_board(CRS, rows=200, destination_crs=des, origin_crs=ori)
        elif des != None:
            if incArr == True: board = darwin_session.get_station_board(CRS, rows=200, destination_crs=des, include_arrivals=True)
            else: board = darwin_session.get_station_board(CRS, rows=200, destination_crs=des)
        elif ori != None:
            if incArr == True: board = darwin_session.get_station_board(CRS, rows=200, origin_crs=ori, include_arrivals=True)
            else: board = darwin_session.get_station_board(CRS, rows=200, origin_crs=ori)
        else:
            if incArr == True: board = darwin_session.get_station_board(CRS, rows=200, include_arrivals=True)
            else: board = darwin_session.get_station_board(CRS, rows=200)
        board.location_name
        '''while True:
            print(str(datetime.datetime.now())+": Still Alive")
            if (datetime.datetime.now().minute)%1 == 0:
                if (datetime.datetime.now().second) == 0:
                    try:
                        if board != darwin_session.get_station_board(tlc):
                            board = darwin_session.get_station_board(tlc,rows=200)
                            break
                    except:
                        print(str(datetime.datetime.now())+": Get Service Info Error")
                time.sleep(setTimer())#'''

        board.all_services = []

        t = 0
        b = 0
        f = 0
        tmax = len(board.train_services)
        bmax = len(board.bus_services)
        fmax = len(board.ferry_services)
        amax = tmax + bmax + fmax

        possibleETDs = ["On time","Delayed","Cancelled"]

        if datetime.datetime.now().hour < 22:

            if amax == 0:
                print("There are no services")

            if tmax != 0:
                #print("There are trains")
    
                board.all_services.append(board.train_services[t])
                board.all_services[0].serviceType = "Train"
                t = t+1
                
                for i in range(t,tmax):
                    for x in range(len(board.all_services)):
                        try:                                                                                                        ###First Section tries to run as normal###
                            if board.train_services[i].etd in possibleETDs:                                                         
                                if board.all_services[x].etd in possibleETDs:
                                    if board.train_services[i].std.replace(':', '') < board.all_services[x].std.replace(':', ''):
                                        board.all_services.insert(x,board.train_services[i])
                                        board.all_services[x].serviceType = "Train"
                                        break
                                else:
                                    if board.train_services[i].std.replace(':', '') < board.all_services[x].etd.replace(':', ''):
                                        board.all_services.insert(x,board.train_services[i])
                                        board.all_services[x].serviceType = "Train"
                                        break
                            else:
                                if board.all_services[x].etd in possibleETDs:
                                    if board.train_services[i].etd.replace(':', '') < board.all_services[x].std.replace(':', ''):
                                        board.all_services.insert(x,board.train_services[i])
                                        board.all_services[x].serviceType = "Train"
                                        break
                                else:
                                    if board.train_services[i].etd.replace(':', '') < board.all_services[x].etd.replace(':', ''):
                                        board.all_services.insert(x,board.train_services[i])
                                        board.all_services[x].serviceType = "Train"
                                        break
                            if x == len(board.all_services)-1:
                                board.all_services.append(board.train_services[i])
                                board.all_services[x+1].serviceType = "Train"
                        except AttributeError:                                                                                      #This section tries with the new service using arrival 
                            try:
                                if board.train_services[i].eta in possibleETDs:                                                         
                                    if board.all_services[x].etd in possibleETDs:
                                        if board.train_services[i].sta.replace(':', '') < board.all_services[x].std.replace(':', ''):
                                            board.all_services.insert(x,board.train_services[i])
                                            board.all_services[x].serviceType = "Train"
                                            break
                                    else:
                                        if board.train_services[i].sta.replace(':', '') < board.all_services[x].etd.replace(':', ''):
                                            board.all_services.insert(x,board.train_services[i])
                                            board.all_services[x].serviceType = "Train"
                                            break
                                else:
                                    if board.all_services[x].etd in possibleETDs:
                                        if board.train_services[i].eta.replace(':', '') < board.all_services[x].std.replace(':', ''):
                                            board.all_services.insert(x,board.train_services[i])
                                            board.all_services[x].serviceType = "Train"
                                            break
                                    else:
                                        if board.train_services[i].eta.replace(':', '') < board.all_services[x].etd.replace(':', ''):
                                            board.all_services.insert(x,board.train_services[i])
                                            board.all_services[x].serviceType = "Train"
                                            break
                                if x == len(board.all_services)-1:
                                    board.all_services.append(board.train_services[i])
                                    board.all_services[x+1].serviceType = "Train"
                            except AttributeError:                                                                                  #This section tries with the old service using arrival
                                try:
                                    if board.train_services[i].etd in possibleETDs:                                                         
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.train_services[i].std.replace(':', '') < board.all_services[x].sta.replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                        else:
                                            if board.train_services[i].std.replace(':', '') < board.all_services[x].eta.replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                    else:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.train_services[i].etd.replace(':', '') < board.all_services[x].sta.replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                        else:
                                            if board.train_services[i].etd.replace(':', '') < board.all_services[x].eta.replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                    if x == len(board.all_services)-1:
                                        board.all_services.append(board.train_services[i])
                                        board.all_services[x+1].serviceType = "Train"
                                except AttributeError:                                                                              #This section tries with both using arrival
                                    if board.train_services[i].eta in possibleETDs:                                                         
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.train_services[i].sta.replace(':', '') < board.all_services[x].sta.replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                        else:
                                            if board.train_services[i].sta.replace(':', '') < board.all_services[x].eta.replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                    else:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.train_services[i].eta.replace(':', '') < board.all_services[x].sta.replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                        else:
                                            if board.train_services[i].eta.replace(':', '') < board.all_services[x].eta.replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                    if x == len(board.all_services)-1:
                                        board.all_services.append(board.train_services[i])
                                        board.all_services[x+1].serviceType = "Train"
                    
            
            if bmax != 0:
                #print("There are busses")
    
                if len(board.all_services) == 0:
                    board.all_services.append(board.bus_services[b])
                    board.all_services[0].serviceType = "Bus"
                    b = b+1

                for i in range(b,bmax):
                    for x in range(len(board.all_services)):
                        try:
                            if board.bus_services[i].etd in possibleETDs:
                                if board.all_services[x].etd in possibleETDs:                                
                                    if board.bus_services[i].std.replace(':', '') < board.all_services[x].std.replace(':', ''):
                                        board.all_services.insert(x,board.bus_services[i])
                                        board.all_services[x].serviceType = "Bus"
                                        break
                                else:
                                    if board.bus_services[i].std.replace(':', '') < board.all_services[x].etd.replace(':', ''):
                                        board.all_services.insert(x,board.bus_services[i])
                                        board.all_services[x].serviceType = "Bus"
                                        break
                            else:
                                if board.all_services[x].etd in possibleETDs:
                                    if board.bus_services[i].etd.replace(':', '') < board.all_services[x].std.replace(':', ''):
                                        board.all_services.insert(x,board.bus_services[i])
                                        board.all_services[x].serviceType = "Bus"
                                        break
                                else:
                                    if board.bus_services[i].etd.replace(':', '') < board.all_services[x].etd.replace(':', ''):
                                        board.all_services.insert(x,board.bus_services[i])
                                        board.all_services[x].serviceType = "Bus"
                                        break
                            if x == len(board.all_services)-1:
                                board.all_services.append(board.bus_services[i])
                                board.all_services[x+1].serviceType = "Bus"
                        except AttributeError:
                            try:
                                if board.bus_services[i].eta in possibleETDs:
                                    if board.all_services[x].etd in possibleETDs:                                
                                        if board.bus_services[i].sta.replace(':', '') < board.all_services[x].std.replace(':', ''):
                                            board.all_services.insert(x,board.bus_services[i])
                                            board.all_services[x].serviceType = "Bus"
                                            break
                                    else:
                                        if board.bus_services[i].sta.replace(':', '') < board.all_services[x].etd.replace(':', ''):
                                            board.all_services.insert(x,board.bus_services[i])
                                            board.all_services[x].serviceType = "Bus"
                                            break
                                else:
                                    if board.all_services[x].etd in possibleETDs:
                                        if board.bus_services[i].eta.replace(':', '') < board.all_services[x].std.replace(':', ''):
                                            board.all_services.insert(x,board.bus_services[i])
                                            board.all_services[x].serviceType = "Bus"
                                            break
                                    else:
                                        if board.bus_services[i].eta.replace(':', '') < board.all_services[x].etd.replace(':', ''):
                                            board.all_services.insert(x,board.bus_services[i])
                                            board.all_services[x].serviceType = "Bus"
                                            break
                                if x == len(board.all_services)-1:
                                    board.all_services.append(board.bus_services[i])
                                    board.all_services[x+1].serviceType = "Bus"
                            except AttributeError:
                                try:
                                    if board.bus_services[i].etd in possibleETDs:
                                        if board.all_services[x].eta in possibleETDs:                                
                                            if board.bus_services[i].std.replace(':', '') < board.all_services[x].sta.replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                        else:
                                            if board.bus_services[i].std.replace(':', '') < board.all_services[x].eta.replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                    else:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.bus_services[i].etd.replace(':', '') < board.all_services[x].sta.replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                        else:
                                            if board.bus_services[i].etd.replace(':', '') < board.all_services[x].eta.replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                    if x == len(board.all_services)-1:
                                        board.all_services.append(board.bus_services[i])
                                        board.all_services[x+1].serviceType = "Bus"
                                except AttributeError:
                                    if board.bus_services[i].eta in possibleETDs:
                                        if board.all_services[x].eta in possibleETDs:                                
                                            if board.bus_services[i].sta.replace(':', '') < board.all_services[x].sta.replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                        else:
                                            if board.bus_services[i].sta.replace(':', '') < board.all_services[x].eta.replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                    else:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.bus_services[i].eta.replace(':', '') < board.all_services[x].sta.replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                        else:
                                            if board.bus_services[i].eta.replace(':', '') < board.all_services[x].eta.replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                    if x == len(board.all_services)-1:
                                        board.all_services.append(board.bus_services[i])
                                        board.all_services[x+1].serviceType = "Bus"
                
            if fmax != 0:
                #print("There are ferries")
    
                if len(board.all_services) == 0:
                    board.all_services.append(board.bus_services[f])
                    board.all_services[0].serviceType = "Ferry"
                    f = f+1

                for i in range(f,fmax):
                    for x in range(len(board.all_services)):
                        try:
                            if board.ferry_services[i].etd in possibleETDs:
                                if board.all_services[x].etd in possibleETDs:
                                    if board.ferry_services[i].std.replace(':', '') < board.all_services[x].std.replace(':', ''):
                                        board.all_services.insert(x,board.ferry_services[i])
                                        board.all_services[x].serviceType = "Ferry"
                                        break
                                else:
                                    if board.ferry_services[i].std.replace(':', '') < board.all_services[x].etd.replace(':', ''):
                                        board.all_services.insert(x,board.ferry_services[i])
                                        board.all_services[x].serviceType = "Ferry"
                                        break
                            else:
                                if board.all_services[x].etd in possibleETDs:
                                    if board.ferry_services[i].etd.replace(':', '') < board.all_services[x].std.replace(':', ''):
                                        board.all_services.insert(x,board.ferry_services[i])
                                        board.all_services[x].serviceType = "Ferry"
                                        break
                                else:
                                    if board.ferry_services[i].etd.replace(':', '') < board.all_services[x].etd.replace(':', ''):
                                        board.all_services.insert(x,board.ferry_services[i])
                                        board.all_services[x].serviceType = "Ferry"
                                        break
                            if x == len(board.all_services)-1:
                                board.all_services.append(board.ferry_services[i])
                                board.all_services[x+1].serviceType = "Ferry"
                        except AttributeError:
                            try:
                                if board.ferry_services[i].eta in possibleETDs:
                                    if board.all_services[x].etd in possibleETDs:
                                        if board.ferry_services[i].sta.replace(':', '') < board.all_services[x].std.replace(':', ''):
                                            board.all_services.insert(x,board.ferry_services[i])
                                            board.all_services[x].serviceType = "Ferry"
                                            break
                                    else:
                                        if board.ferry_services[i].sta.replace(':', '') < board.all_services[x].etd.replace(':', ''):
                                            board.all_services.insert(x,board.ferry_services[i])
                                            board.all_services[x].serviceType = "Ferry"
                                            break
                                else:
                                    if board.all_services[x].etd in possibleETDs:
                                        if board.ferry_services[i].eta.replace(':', '') < board.all_services[x].std.replace(':', ''):
                                            board.all_services.insert(x,board.ferry_services[i])
                                            board.all_services[x].serviceType = "Ferry"
                                            break
                                    else:
                                        if board.ferry_services[i].eta.replace(':', '') < board.all_services[x].etd.replace(':', ''):
                                            board.all_services.insert(x,board.ferry_services[i])
                                            board.all_services[x].serviceType = "Ferry"
                                            break
                                if x == len(board.all_services)-1:
                                    board.all_services.append(board.ferry_services[i])
                                    board.all_services[x+1].serviceType = "Ferry"
                            except AttributeError:
                                try:
                                    if board.ferry_services[i].etd in possibleETDs:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.ferry_services[i].std.replace(':', '') < board.all_services[x].sta.replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                        else:
                                            if board.ferry_services[i].std.replace(':', '') < board.all_services[x].eta.replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                    else:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.ferry_services[i].etd.replace(':', '') < board.all_services[x].sta.replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                        else:
                                            if board.ferry_services[i].etd.replace(':', '') < board.all_services[x].eta.replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                    if x == len(board.all_services)-1:
                                        board.all_services.append(board.ferry_services[i])
                                        board.all_services[x+1].serviceType = "Ferry"
                                except AttributeError:
                                    if board.ferry_services[i].eta in possibleETDs:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.ferry_services[i].sta.replace(':', '') < board.all_services[x].sta.replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                        else:
                                            if board.ferry_services[i].sta.replace(':', '') < board.all_services[x].eta.replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                    else:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.ferry_services[i].eta.replace(':', '') < board.all_services[x].sta.replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                        else:
                                            if board.ferry_services[i].eta.replace(':', '') < board.all_services[x].eta.replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                    if x == len(board.all_services)-1:
                                        board.all_services.append(board.ferry_services[i])
                                        board.all_services[x+1].serviceType = "Ferry"
                            
            for i in range(len(board.all_services)):
                try:
                    if board.all_services[0].etd in possibleETDs:
                        if int(board.all_services[0].std.replace(':', '')) < int(curTime()[:5].replace(":","")):
                            del board.all_services[0]
                        else: break
                    elif int(board.all_services[0].etd.replace(':', '')) < int(curTime()[:5].replace(":","")):
                        del board.all_services[0]
                    else: break
                except AttributeError:
                    if board.all_services[0].eta in possibleETDs:
                        if int(board.all_services[0].sta.replace(':', '')) < int(curTime()[:5].replace(":","")):
                            del board.all_services[0]
                        else: break
                    elif int(board.all_services[0].eta.replace(':', '')) < int(curTime()[:5].replace(":","")):
                        del board.all_services[0]
                    else: break
                
        else:
            if amax == 0:
                print("There are no services")

            if tmax != 0:
                #print("There are trains")
    
                board.all_services.append(board.train_services[t])
                board.all_services[0].serviceType = "Train"
                t = t+1

                for i in range(t,tmax):
                    for x in range(len(board.all_services)):
                        try:
                            if board.train_services[i].etd in possibleETDs:
                                if board.all_services[x].etd in possibleETDs:
                                    if board.train_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                        board.all_services.insert(x,board.train_services[i])
                                        board.all_services[x].serviceType = "Train"
                                        break
                                else:
                                    if board.train_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                        board.all_services.insert(x,board.train_services[i])
                                        board.all_services[x].serviceType = "Train"
                                        break
                            else:
                                if board.all_services[x].etd in possibleETDs:
                                    if board.train_services[i].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                        board.all_services.insert(x,board.train_services[i])
                                        board.all_services[x].serviceType = "Train"
                                        break
                                else:
                                    if board.train_services[i].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                        board.all_services.insert(x,board.train_services[i])
                                        board.all_services[x].serviceType = "Train"
                                        break
                            if x == len(board.all_services)-1:
                                board.all_services.append(board.train_services[i])
                                board.all_services[x+1].serviceType = "Train"
                        except AttributeError:
                            try:
                                if board.train_services[i].eta in possibleETDs:
                                    if board.all_services[x].etd in possibleETDs:
                                        if board.train_services[i].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                            board.all_services.insert(x,board.train_services[i])
                                            board.all_services[x].serviceType = "Train"
                                            break
                                    else:
                                        if board.train_services[i].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                            board.all_services.insert(x,board.train_services[i])
                                            board.all_services[x].serviceType = "Train"
                                            break
                                else:
                                    if board.all_services[x].etd in possibleETDs:
                                        if board.train_services[i].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                            board.all_services.insert(x,board.train_services[i])
                                            board.all_services[x].serviceType = "Train"
                                            break
                                    else:
                                        if board.train_services[i].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                            board.all_services.insert(x,board.train_services[i])
                                            board.all_services[x].serviceType = "Train"
                                            break
                                if x == len(board.all_services)-1:
                                    board.all_services.append(board.train_services[i])
                                    board.all_services[x+1].serviceType = "Train"
                            except AttributeError:
                                try:
                                    if board.train_services[i].etd in possibleETDs:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.train_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                        else:
                                            if board.train_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                    else:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.train_services[i].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                        else:
                                            if board.train_services[i].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                    if x == len(board.all_services)-1:
                                        board.all_services.append(board.train_services[i])
                                        board.all_services[x+1].serviceType = "Train"
                                except AttributeError:
                                    if board.train_services[i].eta in possibleETDs:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.train_services[i].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                        else:
                                            if board.train_services[i].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                    else:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.train_services[i].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                        else:
                                            if board.train_services[i].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.train_services[i])
                                                board.all_services[x].serviceType = "Train"
                                                break
                                    if x == len(board.all_services)-1:
                                        board.all_services.append(board.train_services[i])
                                        board.all_services[x+1].serviceType = "Train"
                                        
            if bmax != 0:
                #print("There are busses")
    
                if len(board.all_services) == 0:
                    board.all_services.append(board.bus_services[b])
                    board.all_services[0].serviceType = "Bus"
                    b = b+1

                for i in range(b,bmax):
                    for x in range(len(board.all_services)):
                        try:
                            if board.bus_services[i].etd in possibleETDs:
                                if board.all_services[x].etd in possibleETDs:                                
                                    if board.bus_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                        board.all_services.insert(x,board.bus_services[i])
                                        board.all_services[x].serviceType = "Bus"
                                        break
                                else:
                                    if board.bus_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                        board.all_services.insert(x,board.bus_services[i])
                                        board.all_services[x].serviceType = "Bus"
                                        break
                            else:
                                if board.all_services[x].etd in possibleETDs:
                                    if board.bus_services[i].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                        board.all_services.insert(x,board.bus_services[i])
                                        board.all_services[x].serviceType = "Bus"
                                        break
                                else:
                                    if board.bus_services[i].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                        board.all_services.insert(x,board.bus_services[i])
                                        board.all_services[x].serviceType = "Bus"
                                        break
                            if x == len(board.all_services)-1:
                                board.all_services.append(board.bus_services[i])
                                board.all_services[x+1].serviceType = "Bus"
                        except AttributeError:
                            try:
                                if board.bus_services[i].eta in possibleETDs:
                                    if board.all_services[x].etd in possibleETDs:                                
                                        if board.bus_services[i].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                            board.all_services.insert(x,board.bus_services[i])
                                            board.all_services[x].serviceType = "Bus"
                                            break
                                    else:
                                        if board.bus_services[i].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                            board.all_services.insert(x,board.bus_services[i])
                                            board.all_services[x].serviceType = "Bus"
                                            break
                                else:
                                    if board.all_services[x].etd in possibleETDs:
                                        if board.bus_services[i].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                            board.all_services.insert(x,board.bus_services[i])
                                            board.all_services[x].serviceType = "Bus"
                                            break
                                    else:
                                        if board.bus_services[i].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                            board.all_services.insert(x,board.bus_services[i])
                                            board.all_services[x].serviceType = "Bus"
                                            break
                                if x == len(board.all_services)-1:
                                    board.all_services.append(board.bus_services[i])
                                    board.all_services[x+1].serviceType = "Bus"
                            except AttributeError:
                                try:
                                    if board.bus_services[i].etd in possibleETDs:
                                        if board.all_services[x].eta in possibleETDs:                                
                                            if board.bus_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                        else:
                                            if board.bus_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                    else:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.bus_services[i].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                        else:
                                            if board.bus_services[i].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                    if x == len(board.all_services)-1:
                                        board.all_services.append(board.bus_services[i])
                                        board.all_services[x+1].serviceType = "Bus"
                                except AttributeError:
                                    if board.bus_services[i].eta in possibleETDs:
                                        if board.all_services[x].eta in possibleETDs:                                
                                            if board.bus_services[i].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                        else:
                                            if board.bus_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                    else:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.bus_services[i].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                        else:
                                            if board.bus_services[i].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.bus_services[i])
                                                board.all_services[x].serviceType = "Bus"
                                                break
                                    if x == len(board.all_services)-1:
                                        board.all_services.append(board.bus_services[i])
                                        board.all_services[x+1].serviceType = "Bus"
                
            if fmax != 0:
                #print("There are ferries")
    
                if len(board.all_services) == 0:
                    board.all_services.append(board.bus_services[f])
                    board.all_services[0].serviceType = "Ferry"
                    f = f+1

                for i in range(f,fmax):
                    for x in range(len(board.all_services)):
                        try:
                            if board.ferry_services[i].etd in possibleETDs:
                                if board.all_services[x].etd in possibleETDs:
                                    if board.ferry_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                        board.all_services.insert(x,board.ferry_services[i])
                                        board.all_services[x].serviceType = "Ferry"
                                        break
                                else:
                                    if board.ferry_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                        board.all_services.insert(x,board.ferry_services[i])
                                        board.all_services[x].serviceType = "Ferry"
                                        break
                            else:
                                if board.all_services[x].etd in possibleETDs:
                                    if board.ferry_services[i].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                        board.all_services.insert(x,board.ferry_services[i])
                                        board.all_services[x].serviceType = "Ferry"
                                        break
                                else:
                                    if board.ferry_services[i].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                        board.all_services.insert(x,board.ferry_services[i])
                                        board.all_services[x].serviceType = "Ferry"
                                        break
                            if x == len(board.all_services)-1:
                                board.all_services.append(board.ferry_services[i])
                                board.all_services[x+1].serviceType = "Ferry"
                        except AttributeError:
                            try:
                                if board.ferry_services[i].eta in possibleETDs:
                                    if board.all_services[x].etd in possibleETDs:
                                        if board.ferry_services[i].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                            board.all_services.insert(x,board.ferry_services[i])
                                            board.all_services[x].serviceType = "Ferry"
                                            break
                                    else:
                                        if board.ferry_services[i].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                            board.all_services.insert(x,board.ferry_services[i])
                                            board.all_services[x].serviceType = "Ferry"
                                            break
                                else:
                                    if board.all_services[x].etd in possibleETDs:
                                        if board.ferry_services[i].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                            board.all_services.insert(x,board.ferry_services[i])
                                            board.all_services[x].serviceType = "Ferry"
                                            break
                                    else:
                                        if board.ferry_services[i].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                            board.all_services.insert(x,board.ferry_services[i])
                                            board.all_services[x].serviceType = "Ferry"
                                            break
                                if x == len(board.all_services)-1:
                                    board.all_services.append(board.ferry_services[i])
                                    board.all_services[x+1].serviceType = "Ferry"
                            except AttributeError:
                                try:
                                    if board.ferry_services[i].etd in possibleETDs:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.ferry_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                        else:
                                            if board.ferry_services[i].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                    else:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.ferry_services[i].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                        else:
                                            if board.ferry_services[i].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                    if x == len(board.all_services)-1:
                                        board.all_services.append(board.ferry_services[i])
                                        board.all_services[x+1].serviceType = "Ferry"
                                except AttributeError:
                                    if board.ferry_services[i].eta in possibleETDs:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.ferry_services[i].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                        else:
                                            if board.ferry_services[i].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                    else:
                                        if board.all_services[x].eta in possibleETDs:
                                            if board.ferry_services[i].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                        else:
                                            if board.ferry_services[i].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '') < board.all_services[x].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', ''):
                                                board.all_services.insert(x,board.ferry_services[i])
                                                board.all_services[x].serviceType = "Ferry"
                                                break
                                    if x == len(board.all_services)-1:
                                        board.all_services.append(board.ferry_services[i])
                                        board.all_services[x+1].serviceType = "Ferry"
        
            for i in range(len(board.all_services)):
                try:
                    if board.all_services[0].etd in possibleETDs:
                        if int(board.all_services[0].std.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '')) < int(curTime()[:5].replace(":","")):
                            del board.all_services[0]
                        else: break
                    elif int(board.all_services[0].etd.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '')) < int(curTime()[:5].replace(":","")):
                        del board.all_services[0]
                    else: break
                except AttributeError:
                    if board.all_services[0].eta in possibleETDs:
                        if int(board.all_services[0].sta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '')) < int(curTime()[:5].replace(":","")):
                            del board.all_services[0]
                        else: break
                    elif int(board.all_services[0].eta.replace('00:','24:').replace('01:','25:').replace('02:','26:').replace(':', '')) < int(curTime()[:5].replace(":","")):
                        del board.all_services[0]
                    else: break

        return board.all_services
    except urllib.error.URLError:
        print("Internet Lost")
    #except AttributeError:
        #print("Including arrivals is not yet fully supported, showing trains only in scheduled order")
        #return board.train_services
    except:
        print("Sort Error")
      
def now():
    return datetime.datetime.now()

def curTime():
    return time.asctime()[11:19]

def setMinTimer():
    return 60 - (now().second+now().microsecond*0.000001)

def setSecTimer():
    return 1 - now().microsecond*0.000001

def setShortTimer(t):
    return t - (now().microsecond*0.000001)%t

def serviceDetail(No):
    while True:
        try:
            return darwin_session.get_service_details(services[No].service_id)
            break
        except:
            print("Get Service Info Error")

def callingAt(No):
    possibleETDs = ["On time","Delayed","Cancelled"]
    cpList = []
    for cp in serviceDetail(No).subsequent_calling_points:
        cpInfo = []
        if cp.et == "Cancelled":
            cpInfo.append(None)
            cpInfo.append(None)
        elif cp.et != "Cancelled":
            cpInfo.append(customStation(cp.location_name))
        if cp.et == "On time":
            cpInfo.append(cp.st)
        elif cp.et != "Delayed":
            cpInfo.append(cp.st+" exp "+cp.et)
        else:
            cpInfo.append(None)
        cpInfo.append(None)
        cpList.append(cpInfo)
    return cpList

def stoppedAt(No):
    possibleETDs = ["On time","Delayed","Cancelled"]
    cpList = []
    for cp in serviceDetail(No).previous_calling_points:
        cpInfo = []
        if (cp.et or cp.at) == "Cancelled":
            cpInfo.append(None)
            cpInfo.append(None)
        elif (cp.et or cp.at) != "Cancelled":
            cpInfo.append(customStation(cp.location_name))
        if (cp.et or cp.at) == "On time":
            cpInfo.append(cp.st)
        elif (cp.et or cp.at) != "Delayed":
            if cp.et != None: cpInfo.append(cp.st+" exp "+cp.et)
            elif cp.at != None: cpInfo.append(cp.at+" sch "+cp.st)
        else:
            cpInfo.append(None)
        cpInfo.append(None)
        cpList.append(cpInfo)
    return cpList

def customStation(name):
    try:
        if "London St Pancras (Intl)" in name:
            return name.replace("London St Pancras (Intl)", "St Pancras International")
        if "Farringdon Underground" in name:
            return name.replace("Farringdon Underground","Farringdon")
        if "London Blackfriars" in name:
            return name.replace("London Blackfriars","Blackfriars")
        if "London Waterloo" in name:
            return name.replace("London Waterloo","Waterloo")
        if "London Victoria" in name:
            return name.replace("London Victoria","Victoria")
        if "London Liverpool Street" in name:
            return name.replace("London Liverpool Street","Liverpool Street")
        if "London Kings Cross" in name:
            return name.replace("London Kings Cross","Kings Cross")
        if "London Charing Cross" in name:
            return name.replace("London Charing Cross","Charing Cross")
        if "London Paddington" in name:
            return name.replace("London Paddington","Paddington")
        if "London Euston" in name:
            return name.replace("London Euston","Euston")
        if "Llanfairpwll" in name:
            return name.replace("Llanfairpwll","Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch")
        else:
            name = re.sub(" \(.*\)","",name)
            return name
    except:
        name = re.sub(" \(.*\)","",name)
        return name
        
def center(lineno):
    return (int((width-len(lineno))/2)*" ")+lineno

def customOperator(i):
    if services[i].operator_name == "London North Eastern Railway":
        return "LNER"
    else:
        return services[i].operator_name

def printDepartures(Limit):
    if services == None:
        return print("No Services Found")
    elif Limit>len(services):
        Limit = len(services)
    print(" "*int((103-len(board.location_name+" Departures"))/2)+board.location_name+" Departures")
    print("-"*103)
    print("| SCHED | PLAT |    DUE    |                    DEST                   |           OPERATOR           |")
    print("-"*103)

    for x in range(Limit):
        i = services[x]
        print("| %5s | %4s | %9s | %41s | %28s |" %(i.std or i.sta, i.platform or "", i.etd or i.eta,i.destination_text.replace(", "," and "),i.operator_name))
    print("-"*103)

def getTLC():
    while True:
        TLC = input("Enter TLC: ")
        TLC = TLC.upper()
        try:
            board = darwin_session.get_station_board(TLC)
            print(customStation(board.location_name), "Confirmed")
            return TLC, customStation(board.location_name)
            break
        except nredarwin.webservice.WebServiceError:
            print("Invalid CRS, try again")
        except urllib.error.URLError:
            print("Connection Failed")
            errorCoolOff()
                
def getStation():
    global CRS
    global services
    global line1Text
    global line1
    global line2
    global line3
    global line4
    global line5
    global line3Text
    global std2
    global pla2
    global des2
    global desText2
    global etd2
    global std4
    global pla4
    global des4
    global desText4
    global etd4
    global op2
    
    CRS = getTLC()[0]
    getDes()
    if des == None: getOri()
    priorCP()
    incArrivals()
    incTimes()
    services = sortServices()
    print("This program will show departures from "+customStation(board.location_name)+" station")
    line1Text = customStation(board.location_name) + " Departures"
    if des != None: line1Text += " To "+destination
    elif ori != None: line1Text += " From "+origin
    line1 = line1Text
    line2 = ""
    line3 = center("Data Loading")
    line3Text = ""
    line4 = ""
    desText4 = ""
    line5 = ""
    std2 = ""
    pla2 = ""
    des2 = ""
    desText2 = ""
    etd2 = ""
    std4 = ""
    pla4 = ""
    des4 = ""
    desText4 = ""
    etd4 = ""
    op2 = ""
    services = sortServices()
    try: op2 = customOperator(0)
    except IndexError: print("Index Error")
    except TypeError: print("Type Error")
    generateLine3()
    line3 = line3Text
    mlcd.draw([center(line1)[:width],line2[:width],line3[:width],line4[:width],center(line5)[:width]])
    printDepartures(10)

def errorCoolOff():
    global eTime
    eTime += 1
    print("Waiting",eTime,"seconds")
    for i in range(eTime):
        print (eTime-i)
        time.sleep(setSecTimer())

def stationMessageParser(i):
    i = re.sub("<A.*</A>","",i)
    i = i.replace("More information can be found in"," ")
    i = i.replace("More details can be found in"," ")
    i = i.replace("<P>"," ")
    i = i.replace("</P>"," ")
    i = i.replace(" ."," ")
    i = i.replace("Additional trains to Great Northern destinations operate from London St Pancras International which is a short walk from London Kings Cross."," ")
    i = i.replace("Additional trains to Great Northern destinations operate from London Kings Cross which is a short walk from London St Pancras International."," ")
    i = i.replace("There is step free access at London Victoria Rail Station to the Victoria Line on the Underground. This can be accessed via the Cardinal Place entrance to the underground."," ")
    i = customStation(i)
    i = i.replace("  "," ")
    return i

def generateLine3():
    global line3Text
    global caText
    global op2
    global line3
    global services
    global calling
    
    if len(services) != 0 and services != None:
        calling = callingAt(0)
        stopped = stoppedAt(0)
        if serviceDetail(0).is_cancelled == True or etd2 == "Cancelled":
            if customOperator(0)[-6:] == "Trains" and services[0].serviceType.lower() == "train":
                line3Text = "This "+customOperator(0) +" service has been cancelled. " + (serviceDetail(0).disruption_reason or "")
            else:
                line3Text = "This "+customOperator(0) +" "+services[0].serviceType.lower()+" has been cancelled. " + (serviceDetail(0).disruption_reason or "")
        else:
            if stopped != [] and prior == True:
                saText = ". This service will have called at: "
                if stopped != None:
                    for i in range(len(stopped)):
                        saText += stopped[i][0]
                        if stopped[i][1] != None and incTi == True: saText += " ("+stopped[i][1].replace(":","")+")"
                        saText += ", "
                        if i == len(stopped)-2:
                            saText = saText[0:-2] + " and "
                    saText = saText[0:-2]
                    if len(stopped) < 3:
                        saText = saText.replace(":","")
                        if len(stopped) == 1:
                            saText += " only"
            else: saText = ""
                
            if calling != []:
                caText = "calling at: "
                if calling != None:
                    for i in range(len(calling)):
                        caText += calling[i][0]
                        if calling[i][1] != None and incTi == True: caText += " ("+calling[i][1].replace(":","")+")"
                        caText += ", "
                        if i == len(calling)-2:
                            caText = caText[0:-2] + " and "
                    caText = caText[0:-2]
                    if len(calling) < 3:
                        caText = caText.replace(":","")
                        if len(calling) == 1:
                            caText += " only. "
            elif des2 == (customStation(board.location_name)):
                caText = "terminating here. "
            else: caText = ""
            Text = (caText + ". " + saText + ". ").replace(" . ", ". ").replace("..",".").replace(" . ", ". ").replace("..",".")
            
            if op2[0] in ["A","E","I","O","U"] or op2 == "LNER":
                line3Text = "An "
            else:
                line3Text = "A "
            if op2[-6:] == "Trains" and services[0].serviceType.lower() == "train":
                line3Text += op2 +" service " + Text + (serviceDetail(0).disruption_reason or "")# + (serviceDetail(0).overdue_message or "")
            else:
                line3Text += op2 +" "+services[0].serviceType.lower()+" " + Text + (serviceDetail(0).disruption_reason or "")# + (serviceDetail(0).overdue_message or "")
        """try:
            for i in board.nrcc_messages:
                line3Text += stationMessageParser(i)
        except IndexError:
            print("No Station Messages")"""
        while line3Text[-1:] == " ":
            line3Text = line3Text[:-1]
        line3Text = line3Text.replace("  "," ").replace(" .",".")
        if line3 not in line3Text:
            if line3 != center("Data Loading"): line3 = ""
            line3 = line3Text
        
        print("Line3 Text Generated "+str(now()))

def getDes():
    global des
    global destination
    des = input("Would you like the board to only show services to a specific station? (y/n) ").lower()
    if des == "y":
        des = getTLC()
        destination = des[1]
        des = des[0]
    else: des = None

def getOri():
    global ori
    global origin
    ori = input("Would you like the board to only show services from a specific station? (y/n) ").lower()
    if ori == "y":
        ori = getTLC()
        origin = ori[1]
        ori = ori[0]
    else: ori = None

def priorCP():
    global prior
    prior = input("Would you like the board to show previous calling points? (y/n) ").lower()
    if prior == "y":
        prior = True
    else:
        priot = False

def incArrivals():
    global incArr
    incArr = input("Would you like the board to include terminating services? (y/n) ").lower()
    if incArr == "y":
        incArr = True
    else:
        incArr = False

def incTimes():
    global incTi
    incTi = input("Would you like the board to include calling point times? (y/n) ").lower()
    if incTi == "y":
        incTi = True
    else:
        incTi = False

def rttServices():
    global CRS
    return json.loads(str(requests.get('https://api.rtt.io/api/v1/json/search/'+CRS, auth=(rttapi_username,rttapi_password)).text))

def rttServiceDetails(serviceUid):
    url = 'https://api.rtt.io/api/v1/json/service/'+serviceUid+'/'+str(now().year)+'/'
    if len(str(now().month)) == 1:
        url += '0'+str(now().month)+'/'+str(now().day)
    else:
        url += str(now().month)+'/'+str(now().day)
    return json.loads(str(requests.get(url, auth=(rttapi_username,rttapi_password)).text))

def getCancelReason(serviceUid):
    global CRS
    rttServiceDetails(serviceUid)

eTime = 0
services = []
width = 48
rttapi_username = "rttapi_Mindi_Crayon"
rttapi_password = "ebe2c5759068e9ab0fe82d84fafe5122342d97e1"

while True:
    try:
        size = int(input("Enter a scale: "))
        break
    except ValueError:
        print("Try Again")
mlcd.init(width,5,size)

while True:
    try:
        darwin_session = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx",api_key='0f01bfbd-ea5f-4954-8d5c-910db25e31de')
        break
    except urllib.error.URLError:
        print("Connection Failed")
        errorCoolOff()
eTime = 0

des = None
ori = None
prior = None

getStation()

eTime = 0


line1 = ""
line2 = ""
line3 = center("Data Loading")
line4 = ""
line5 = ""

line3Text = ""
std2 = ""
pla2 = ""
des2 = ""
desText2 = ""
etd2 = ""
std4 = ""
pla4 = ""
des4 = ""
desText4 = ""
etd4 = ""
a = 0
b = 0
c = 0
d = 0
e = 0
TerminatingText = "Terminates Here"

mlcd.draw([center(line1),line2,line3,line4,center(line5)])

while True:
    try:
        start = now()
        if len(line1Text) > width:
            if len(line1) == width:
                if a != 5:
                    a += 1
                else:
                    a = 0
                    line1 = center(line1Text + " "*5)
            elif len(line1) == 0:
                line1 = line1Text + " "*5
            elif len(line1)>len(line1Text):
                line1=line1[0:len(line1)-1]
            else: line1=line1[1:]
        else: line1 = center(line1Text)
        
        if len(line3Text) > width:
            if len(line3) == width:
                if c != 5:
                    c += 1
                else:
                    c = 0
                    line3 = center(line3Text + " "*5)
            elif len(line3) == 0:
                line3 = line3Text + " "*5
            elif len(line3)>len(line3Text):
                line3=line3[0:len(line3)-1]
            else: line3=line3[1:]
        else: line3 = center(line3Text)

        try:
            if len(std4+" "+pla4+" "+desText4 +" "+etd4) > width:
                line4 = std4 +" "+pla4+" "
                if len(line4+des4+" "+etd4) == width:
                    if d != 5:
                        d += 1
                    else:
                        d = 0
                        des4 = ""
                if len(des4) == 0:
                    des4 = desText4+ " "*5
                elif len(des4) > len(desText4):
                    des4 = des4[0:-1]
                else:
                    des4 = des4[1:]
                line4 += des4[0:width-len(line4+" "+etd4)]
                line4 += ((width-len(line4))-len(etd4))*" "+etd4
        except IndexError:
            if len(services) != 0:
                line4 = center("No Subsequent Services")

        if start.second == 0:
            if services != sortServices():
                services = sortServices()
                print("Update Check Complete "+str(now()))
                printDepartures(10)
                print("Departures Printed "+str(now()))
                line2 = ""
            else:
                print("Update Check Complete "+str(now()))

        if services == None:
            line2 = ""
            line3 = center("Error")
            line4 = ""
        elif len(services) == 0:
            line3 = center("No Departures In")
            line4 = center("The Next Two Hours")
        elif line2 == "":
            try:
                std2 = services[0].std.replace(":","")
                etd2 = services[0].etd.replace(":","")
            except AttributeError:
                std2 = services[0].sta.replace(":","")
                etd2 = services[0].eta.replace(":","")
            pla2 = services[0].platform or " "
            des2 = customStation(services[0].destination_text.replace(", "," and "))
            if des2 == customStation(board.location_name):
                    des2 = TerminatingText
            desText2 = des2 + " "
            op2 = customOperator(0)
            line2 = std2 +" "+pla2+" "+des2
            line2 += ((width-len(line2))-len(etd2))*" "+etd2
            print("Line2 Text Generated "+str(now()))
            
            if serviceDetail(0).is_cancelled == True:
                if op2[-6:0] == "Trains" and services[0].serviceType.lower() == "train":
                    line3Text = "This "+op2 +" service has been cancelled." + (serviceDetail(0).disruption_reason or "")
                else:
                    line3Text = "This "+op2 +" "+services[0].serviceType.lower()+" has been cancelled." + (serviceDetail(0).disruption_reason or "")
                line3 = (line3Text + " ").replace("  "," ")
                
        try:
            noserv = len(services)
            if incArr != True:
                if start.second == 0:
                    service4 = services[1]
                elif start.second == 30:
                    if noserv > 2:
                        service4 = services[2]
                elif start.second == 40:
                    if noserv > 3:
                        service4 = services[3]
                    else:
                        service4 = services[1]
                elif start.second == 50:
                    if noserv > 4:
                        service4 = services[4]
                    elif noserv == 3:
                        service4 = services[2]
                    else:
                        service4 = services[1]
            else:
                if start.second == 0:           #T>6 T=3 T=2
                    service4 = services[1]      #1
                elif start.second == 10:
                    if noserv > 2:
                        service4 = services[2]  #2
                elif start.second == 20:
                    if noserv > 3:
                        service4 = services[3]  #3
                    else:
                        service4 = services[1]      #1  #1
                elif start.second == 30:
                    if noserv > 4:
                        service4 = services[4]  #4
                    elif noserv == 3:
                        service4 = services[2]  
                    else:
                        service4 = services[1]
                elif start.second == 40:
                    if noserv > 5:
                        service4 = services[5]  #5
                    elif noserv == 4:
                        service4 = services[2]
                    else:
                        service4 = services[1]
                elif start.second == 50:
                    if noserv > 6:
                        service4 = services[6]  #6
                    elif noserv == 3:
                        service4 = services[2]
                    else:
                        service4 = services[1]
                        
            if start.second in [0,10,20,30,40,50]:
                try:
                    std4 = service4.std.replace(":","")
                    etd4 = service4.etd.replace(":","")
                except AttributeError:
                    std4 = service4.sta.replace(":","")
                    etd4 = service4.eta.replace(":","")
                pla4 = service4.platform or " "
                des4 = customStation(service4.destination_text.replace(", "," and "))
                if des4 == customStation(board.location_name):
                    des4 = TerminatingText
                desText4 = des4 + " "
                line4 = std4+" "+pla4+" "+des4
                line4 = line4+((width-len(line4))-len(etd4))*" "+etd4
                #print("Line4 Text Generated "+str(now()))

        except IndexError:
            if len(services) != 0:
                line4 = center("No Subsequent Services")
            
        if start.second == 0 and len(services) != 0:
            generateLine3()

        line2 = std2 +" "+pla2+" "+des2+" "+etd2
        if len(line2) > width:
            if b < 1+len(line2) - width:
                line2 = std2 +" "+pla2+" "+des2[b:b+len(des2)-(len(line2)-width)]+" "+etd2
                b += 1
            else:
                b = 0
        else:
            line2 = std2 +" "+pla2+" "+des2+(width-len(line2))*" "+" "+etd2

        line4 = std4 +" "+pla4+" "+des4+" "+etd4
        if len(line4) > width:
            if c < 1+len(line4) - width:
                line4 = std4 +" "+pla4+" "+des4[c:c+len(des4)-(len(line4)-width)]+" "+etd4
                c += 1
            else:
                c = 0
        else:
            line4 = std4 +" "+pla4+" "+des4+(width-len(line4))*" "+" "+etd4

        if des2 == TerminatingText:
            if start.second % 2 == 0:
                line2 = std2 +" "+pla2+" "+des2
                line2 += ((width-len(line2))-len(etd2))*" "+etd2
            elif start.second % 2 == 1:
                line2 = std2 +" "+pla2+" "
                line2 += ((width-len(line2))-len(etd2))*" "+etd2
                
        if etd2 == "Cancelled":
            if start.second % 2 == 0:
                line2 = line2[:-9]+etd2
            elif start.second % 2 == 1:
                line2 = line2[:-9]+(" "*9)
                
        if des4 == TerminatingText:
            if start.second % 2 == 0:
                line4 = std4 +" "+pla4+" "+des4
                line4 += ((width-len(line4))-len(etd4))*" "+etd4
            elif start.second % 2 == 1:
                line4 = std4 +" "+pla4+" "
                line4 += ((width-len(line4))-len(etd4))*" "+etd4
                
        if etd4 == "Cancelled":
            if start.second % 2 == 0:
                line4 = line4[:-9]+etd4
            elif start.second % 2 == 1:
                line4 = line4[:-9]+(" "*9)
                
        if len(services) == 0:
            line3 = center("No Departures In")
            line4 = center("The Next Two Hours")
        line5 = curTime()
        mlcd.draw([line1[:width],line2[:width],line3[:width],line4[:width],center(line5)[:width]])
        time.sleep(setShortTimer(0.125))
        eTime = 0
    except KeyboardInterrupt:
        getStation()
    except urllib.error.URLError:
        print("Connection Failed")
        errorCoolOff()
    except TypeError:
        print("Type Error")
        try:
            if services != sortServices():
                services = sortServices()
                print("Update Check Complete "+str(now()))
                printDepartures(10)
                print("Departures Printed "+str(now()))
                line2 = ""
            else:
                print("Update Check Complete "+str(now()))
        except KeyboardInterrupt:
            getStation()
        except urllib.error.URLError:
            print("Connection Failed")
            errorCoolOff()
        except TypeError:
            print("Type Error")
        except:
            print("Unknown Error")
            errorCoolOff()
        errorCoolOff()
    #except:
     #   print("Unknown Error")
      #  errorCoolOff()
