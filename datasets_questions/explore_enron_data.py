#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)

poi = 0
for key in enron_data:
    if enron_data[key]["poi"] == 1:
        poi += 1
print poi

print enron_data["PRENTICE JAMES"]["total_stock_value"]

print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print enron_data["LAY KENNETH L"]["total_payments"]

salary = 0
email_address = 0
for key in enron_data:
    if enron_data[key]["salary"] != "NaN":
        salary += 1
    if enron_data[key]["email_address"] != "NaN":
        email_address += 1
print salary
print email_address

total_payments = 0
for key in enron_data:
    if enron_data[key]["total_payments"] == "NaN":
        total_payments += 1
print total_payments
print float(total_payments)/len(enron_data)


total_payments_poi = 0
for key in enron_data:
    if enron_data[key]["total_payments"] == "NaN" \
            and enron_data[key]["poi"] == 1:
        total_payments_poi += 1
print float(total_payments_poi)/poi

for s in enron_data["LAY KENNETH L"]:
    print s, enron_data["LAY KENNETH L"][s]

exercised_stock_options = []
for key in enron_data:
    if enron_data[key]["exercised_stock_options"] != "NaN" and key != "TOTAL":
        exercised_stock_options.append(enron_data[key]["exercised_stock_options"])

print max(exercised_stock_options)
print min(exercised_stock_options)

salarys = []
for key in enron_data:
    if enron_data[key]["salary"] != "NaN" and key != "TOTAL":
        salarys.append(enron_data[key]["salary"])

print max(salarys)
print min(salarys)