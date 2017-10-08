import datetime
import math
from datetime import date
#Load Metadata
f = open('D:/PROJECT/FOREST 2020/TRAINING/PyQgis/DATA/source/mtl.txt', 'r') #open file for reading
def build_data(f): #build dictionary
    output = {} #Dict
    for line in f.readlines(): #Iterates through every line in the string
        if "=" in line: #make sure line has data as wanted
            l = line.split("=") #Seperate by "=" and put into a list
            output[l[0].strip()] = l[1].strip() #First word is key, second word is value
    return output #Returns a dictionary with the key, value pairs.
data = build_data(f)

def year_date():
    date_file=data['FILE_DATE']
    yearTahun=date_file[:10]
    time_data=date_file[-9:-1]
    all= yearTahun+time_data
    dt = datetime.strptime(all, '%Y-%m-%d%H:%M:%S')
    return dt

def hour():
    if dt.hour <= 6:
        print "hasil:", dt.hour + 12
    else:
        print "hasil", dt,hour
def leap():
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))

def day():
    day_date= date(dt.year, dt.month, dt.day)
    sum_of_day=int(day_date.strftime('%j'))
    return sum_of_day

gamma=((2 * math.pi) / day()) * ((day() - 1) + ((hour() - 12) / 24) )

#sun declination angle
decl=0.006918 - 0.399912 * np.cos(np.radians(gamma)) + 0.070257 * np.sin(gamma) - 0.006758 * np.cos (2 * gamma)\
     + 0.000907 * np.sin (2 * gamma) - 0.002697 * np.cos (3 * gamma) + 0.00148 * np.sin (2 * gamma) #radians
decl_deg= (360 / (2 * math.pi)) * decl