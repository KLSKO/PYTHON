import sys
import csv

# import csv-file with masterdata
# and create dictionary
masterdata_customer = {}
reader = csv.reader(open("masterdata_customer.csv", "rb"), delimiter=';')
for row in reader:
  masterdata_customer.update({row[0] : row[1]})

# Open file with customer IDs
list_customer_file = open("list_customer.txt").readlines()

# Import file content
list_customer = []
for i in range(0,len(list_customer_file)):
  list_customer.append(list_customer_file[i].replace("\n",""))

# check if masterdata for customer id already exists
# if not: prompt for user to enter missing master data
limit = len(list_customer)
masterdata_customer_new = {}
for i in range(0,limit):
  if not list_customer[i] in masterdata_customer:
    confirmation = "init"
    while confirmation != "y":
      new_masterdata = raw_input("Please enter masterdata for %s: " % list_customer[i] )
      print list_customer[i], new_masterdata
      confirmation = raw_input("OK? (y = yes, n = no, q = quit): ")
      if confirmation == "q":
        sys.exit(0)
    masterdata_customer[list_customer[i]] = new_masterdata
    masterdata_customer_new[list_customer[i]] = new_masterdata

# TO DO: Export new masterdata file
# and write to stdout
print "New masterdata at a glance: "
masterdata_customer_new
