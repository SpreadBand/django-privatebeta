# -*- coding:Utf-8 -*-

import csv

invite = InviteRequest.objects.all()

csvWriter = csv.writer(open('privatebeta/exportcsv.csv', 'w'), delimiter=";")

for p in invite:
	info = (p.email, p.created, p.invited)
	csvWriter.writerow(info)


