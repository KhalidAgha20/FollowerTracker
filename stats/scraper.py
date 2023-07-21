from datetime import datetime, timedelta


def scraper(html):
    today = datetime.today().strftime('%Y-%m-%d')

    week = datetime.today() - timedelta(days=7)
    week = week.strftime('%Y-%m-%d')

    month = datetime.today() - timedelta(days=29)
    month = month.strftime('%Y-%m-%d')

    text = html
    text = text.split("\n")


    counter = 0
    list = []
    for line in text:
        if today in line:
            list.append(counter)
        counter = counter + 1
        
    if len(list) == 0:
        today = datetime.today() - timedelta(days=1)
        today = today.strftime('%Y-%m-%d')
        
        counter = 0
        list = []
        for line in text:
            if today in line:
                list.append(counter)
            counter = counter + 1
        
    current = text[list[-1]+6]
    current = current.replace('>','<')
    current = current.split('<')[2]
    current = int(current.replace(' ','').replace(',',''))

    
        

    counter = 0
    list = []
    for line in text:
        if week in line:
            list.append(counter)
        counter = counter + 1
        
    if len(list) == 0:
        week = datetime.today() - timedelta(days=6)
        week = week.strftime('%Y-%m-%d')
        
        counter = 0
        list = []
        for line in text:
            if week in line:
                list.append(counter)
            counter = counter + 1
        
        
    last_week = text[list[-1]+6]
    last_week = last_week.replace('>','<')
    last_week = last_week.split('<')[2]
    last_week = int(last_week.replace(' ','').replace(',','').replace("\t",""))
    
    
    

    counter = 0
    list = []
    for line in text:
        if month in line:
            list.append(counter)
        counter = counter + 1
        
    if len(list) == 0:
        month = datetime.today() - timedelta(days=28)
        month = month.strftime('%Y-%m-%d')
        
        counter = 0
        list = []
        for line in text:
            if month in line:
                list.append(counter)
            counter = counter + 1
        
        
        
    last_month = text[list[-1]+6]
    last_month = last_month.replace('>','<')
    last_month = last_month.split('<')[2]
    last_month = int(last_month.replace(' ','').replace(',','').replace("\t",""))
    
    return current, current-last_week, current-last_month



