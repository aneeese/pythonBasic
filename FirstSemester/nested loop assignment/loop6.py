import datetime
weeks=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months=['January','Feburary','March','April','May','June','July','August','September','October','November','December']
def first_days():
    year=int(input("Enter the year: "))
    day=str(input("Enter the 1st day of the year: "))
    for i in range(12):
        datetimea=datetime.datetime(year,i+1,1)
        print(months[i] + ' 1, ' + str(year) + ' is '+weeks[datetimea.weekday()])
def run():
    first_days()
if __name__=='__main__':
    run()
