greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)


still_missing = mpr[mpr.Status == 'Still Missing']
print(still_missing)


not_poodle = mpr[mpr['Dog Breed'] != 'Poodle']
print(not_poodle)
