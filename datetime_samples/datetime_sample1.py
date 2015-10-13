#!/usr/bin/python

actual_date_str = raw_input()
expected_date_str = raw_input()

actual_date_arr = actual_date_str.split(' ')
expected_date_arr = expected_date_str.split(' ')

fine = 0

if len(actual_date_arr) >= 3 and len(expected_date_arr) >= 3:
	
	actual_day = 0
	actual_month = 0
	actual_year = 0
	
	expected_day = 0
	expected_month = 0
	expected_year = 0
	
	try:
		actual_day = int(actual_date_arr[0])
		actual_month = int(actual_date_arr[1])
		actual_year = int(actual_date_arr[2])
	
		expected_day = int(expected_date_arr[0])
		expected_month = int(expected_date_arr[1])
		expected_year = int(expected_date_arr[2])
		
	except ValueError:
		pass
	
	if actual_day >= 1 and actual_day <= 31 and actual_month >= 1 and actual_month <= 12 and actual_year >= 1 and actual_year <= 3000:
	
		if expected_day >= 1 and expected_day <= 31 and expected_month >= 1 and expected_month <= 12 and expected_year >= 1 and expected_year <= 3000:
	
			if actual_year > expected_year:
				fine = 10000
				
			elif actual_year == expected_year and actual_month > expected_month:
				fine = 500 * (actual_month - expected_month)
				 
			elif actual_year == expected_year and actual_month == expected_month and actual_day > expected_day:
				fine = 15 * (actual_day - expected_day)
				
			else:
				fine = 0
	
		else:
			pass
	
	else:
		pass
	
else:
	pass

print fine
