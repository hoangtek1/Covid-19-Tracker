import requests
import json
import sys
import datetime
import pandas as pd
import numpy as np

from datetime import datetime
from datetime import date, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates


def getChartCountry(countryName):
    # Tắt tất cả những đồ thị(matpltlib) trước đó
    plt.close("all")

    apiData = getDataFromApi(countryName)

    daysShowInChart = 30
    aDay = 1

    listTotalCaseOfDay = [0]*(daysShowInChart)

    endDate = date.today() + timedelta(aDay)
    startDate = endDate - timedelta(daysShowInChart)

    getListOfDaysShowInChart = getListOfDaysFromTwoDay(startDate, endDate)


    for i in range (0,daysShowInChart):
        newestDataOfDay = list(filter(lambda data: data["day"] == getListOfDaysShowInChart[i].strftime("%Y-%m-%d"), apiData))
        if(len(newestDataOfDay) > 0):
            listTotalCaseOfDay[i] = formatDataOfCase(newestDataOfDay[0]["cases"]["new"])
        else:
            listTotalCaseOfDay[i] = 0

    
    plt.style.use('seaborn-colorblind')

    cmap = plt.cm.winter
    fig,ax = plt.subplots()
    fig.autofmt_xdate()
    plt.plot(getListOfDaysShowInChart, listTotalCaseOfDay)

    plt.gcf().autofmt_xdate()
    date_format = mpl_dates.DateFormatter('%d - %m - %Y')
    plt.gca().xaxis.set_major_formatter(date_format)


    plt.title(stringNotifyNewDataIsUpdate(listTotalCaseOfDay, apiData))

    fig.canvas.set_window_title('Chart Covid 19 case for 30days')


    sc = plt.scatter(getListOfDaysShowInChart, listTotalCaseOfDay, s=100, cmap = 'Reds', edgecolor = 'black', linewidth=1, alpha = 0.75)
    annot = ax.annotate("", xy=(0,0), xytext=(30,30),textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    mngr = plt.get_current_fig_manager()
    # to put it into the upper left corner for example:
    mngr.window.setGeometry(340,585,1270,450)


    listStringDate = []
    listStringCaseData = []
    

    for i in getListOfDaysShowInChart:
        listStringDate.append(str(i.strftime("%Y-%m-%d")))

    for i in listTotalCaseOfDay:
        listStringCaseData.append(str(i))

    def update_annot(ind):
        pos = sc.get_offsets()[ind["ind"][0]]
        annot.xy = pos
        text = "{}, {}".format(" ".join([listStringCaseData[n] for n in ind["ind"]]), 
                               " ".join([listStringDate[n] for n in ind["ind"]]))
        annot.set_text(text)
        annot.get_bbox_patch().set_facecolor(cmap(listTotalCaseOfDay[ind["ind"][0]]))
        annot.get_bbox_patch().set_alpha(0.4)

    # Hiện data mỗi khi hover vào đồ thị    
    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)
    plt.show()

def getDataFromApi(countryName):
    url = "https://covid-193.p.rapidapi.com/history?country="
    headers = {
        'x-rapidapi-key': "c0dced8bb9mshbc64e8fcf6cc50ap124d32jsn54f979df4709",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

    response = requests.request("GET", url + countryName, headers=headers)
    return response.json()['response']

def formatDataOfCase(newCase):
    if(newCase != None):
        return int(newCase[1:])
    return 0

def getList30Days(datelist, Days):
    isUpdateDataToday = True if len(list(filter(lambda data: data["day"] == date.today(), apiData))) > 0 else False
    
    if(isUpdateDataToday):
        datelist[Days-1] = dayToday
        for i in range(28,-1,-1):
            dayToday -= timedelta(1)
            datelist[i] = dayToday
    else:
        for i in range(29,-1,-1):
            dayToday -= timedelta(1)
            datelist[i] = dayToday
    return datelist

def getListOfDaysFromTwoDay(startDate, endDate):
    return pd.date_range(startDate,endDate-timedelta(days=1),freq='d').tolist()

def stringNotifyNewDataIsUpdate(listTotalCaseOfDay, apiData):
    if(listTotalCaseOfDay[-1] == 0):
        return "Country: " + apiData[0]['country'] + "  (Still not updated data for new date)"
    return "Country: " + apiData[0]['country']