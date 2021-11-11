#Here we import the three models we need to import data into
from crop.models import SeasonalPrecipitation

#Here we import the python build in csv library(no need to pip install it)
import csv

#We define a function.... to upload the csv..
def uploadCSV():
	
	#We open the csv using open(--which is part of csv library) and asign it a variable 'f'
    f = open("seasonal_precipitation.csv")
	
	#with csv.reader(f) --we read from it... and asign what we read to a variable called 'reader'
    reader = csv.reader(f)
	
	#we create a For-loop to loop through our data..
	#during the looping we asign each column in our csv to a variable..
    for district, dec_jan_feb, mar_apr_may, jun_jul_aug, sep_oct_nov in reader:
        SeasonalPrecipitation.objects.create( district = district, dec_jan_feb = dec_jan_feb, mar_apr_may = mar_apr_may, jun_jul_aug = jun_jul_aug, sep_oct_nov = sep_oct_nov)
        print(f"added {district}")

#Call the function so the we import it it will automatically run
uploadCSV()