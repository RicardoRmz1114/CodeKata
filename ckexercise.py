from datetime import datetime

fileName = input("Enter file name: ")
file1 = open(fileName,'r')
Lines = file1.readlines()

driver = []
trip = []
tot = 0 
time = 0
mph = 0
dic = {}
dicspeed = {}
dicreport = {}

#read file
for line in Lines:
    if line != '\n':
        new = str(line).strip('\n')
        newline = str(new)
        nw = newline.split(' ')
        if nw[0] == 'Driver':
            driver.append(nw[1])
        else:
            #convert string to time format(hours) and then to seconds
            time1pt = datetime.strptime(nw[3],'%H:%M')
            time1pt2 = time1pt.strftime("%H:%M")
            time1pt3 = datetime.strptime(time1pt2,'%H:%M')
            total_seconds = time1pt3.second + time1pt3.minute*60 + time1pt3.hour*3600
            time2pt = datetime.strptime(nw[2],'%H:%M')
            time2pt2 = time2pt.strftime("%H:%M")
            time2pt3 = datetime.strptime(time2pt2,'%H:%M')
            total_seconds2 = time2pt3.second + time2pt3.minute*60 + time2pt3.hour*3600   
            trip.append([nw[1], nw[-1], (total_seconds - total_seconds2)/60])


#get time and distance
for element in trip:
    if element[0] in driver:
        if element[0] in dic:
            x = dic.get(element[0])# distance
            y = dicspeed.get(element[0])# seconds
            tot += float(element[1]) + float(x)
            time += float(element[2] + float(y))
            dic[element[0]] = tot
            dicspeed[element[0]] = time
            continue
        dic[element[0]] = float(element[1])
        dicspeed[element[0]] = element[2]


#sort dict
for key in driver:
    if key not in dic:
        dicreport[key] = 0
        dicspeed[key] = 0
        continue
    dicreport[key] = dic.get(key)
sort_dic = dict(sorted(dicreport.items(), key=lambda x: x[1], reverse=True))


#print values with sorted dict
for key in sort_dic:
    dicreport[key] = dic.get(key)
    x = sort_dic.get(key)# distance
    y = dicspeed.get(key)# seconds
    if x == 0:
        print(key + ': 0 miles')
        continue
    mph = (float(x) / float(y))*60
    if mph >=5 and mph <=100:
        print(key + ': ' + str(round(float(x))) + ' miles' + ' @ ' + str(round(float(mph))) + ' mph' '\n')
        continue