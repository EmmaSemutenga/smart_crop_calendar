#Here we import the three models we need to import data into
from crop.models import MonthlyPrecipitation

#Here we import the python build in csv library(no need to pip install it)
import csv

#We define a function.... to upload the csv..
def uploadCSV():
	
	#We open the csv using open(--which is part of csv library) and asign it a variable 'f'
    f = open("monthly_precipitation.csv")
	
	#with csv.reader(f) --we read from it... and asign what we read to a variable called 'reader'
    reader = csv.reader(f)
	
	#we create a For-loop to loop through our data..
	#during the looping we asign each column in our csv to a variable..
    for district, jan, feb, mar, apr, may, jun, jul, aug, sept, oct, nov, dec in reader:
        MonthlyPrecipitation.objects.create( district = district, jan = jan, feb = feb, mar = mar, apr = apr, may = may, jun = jun, jul = jul, aug = aug, sept = sept, oct = oct, nov = nov, dec = dec)
        print(f"added {district}")

#Call the function so the we import it it will automatically run
uploadCSV()