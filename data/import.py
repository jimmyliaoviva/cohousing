import csv,sys,os
os.environ['DJANGO_SETTINGS_MODULE'] = 'cohousing.settings'
import django
django.setup()
from main.models import old_distribute_sm
data = csv.reader(open("old_distribute_sm.csv"),delimiter=",")
for row in data:
	if row[0] != 'COUNTY_ID':
		unit = old_distribute_sm()
		unit.COUNTY_ID = row[0]
		unit.COUNTY = row[1]
		unit.TOWN_ID = row[2]
		unit.TOWN = row[3]
		unit.FLD01 = row[4]
		unit.FLD02 = row[5]
		unit.FLD03 = row[6]
		unit.FLD04 = row[7]
		unit.FLD05 = row[8]
		unit.FLD06 = row[9]
		unit.INFO_TIME = row[10]
		unit.save()