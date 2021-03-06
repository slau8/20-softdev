from pymongo import MongoClient

'''
 Team heySui
 Shannon Lau and Jen Yu
 SoftDev pd7
 K#04: Mi only nyam ital food, mon!
 2018-02-14
'''

c = MongoClient("lisa.stuy.edu")
r = c["test"]["restaurants"]

#all restaurants in a specified borough
def from_borough(boro):
    qd = { "borough" : boro }
    return r.find(qd)

#all restaurants in a specified zipcode
def from_zip(zip):
    qd = { "address.zipcode" : zip }
    return r.find(qd)

#all restaurants in a specified zipcode with a specified grade (e.g. A, B..)
def from_zip_grade(zip, grade):
    qd = { "$and" : [ { "address.zipcode" : zip }, { "grades.grade" : grade } ] } 
    return r.find(qd)

#all restaurants in a specified zipcode and a score below a threshold
#score must be inputted as int, not a string!
def from_zip_score(zip, score):
    qd = {"$and" : [{"address.zipcode" : zip}, {"grades.score" : {"$lt": score}}]}
    return r.find(qd)

#the "something clever"
#Usually people want to find a specific type of food, no? 
def from_zip_cuisine(zip, cuisine):
    qd = {"$and" : [{"address.zipcode" : zip}, {"cuisine" : cuisine}]}
    return r.find(qd)

#modular design ftw
def loop_print(cursor):
    for i in cursor:
        print i

#function calls
def main():
    '''
    loop_print(from_borough("Manhattan"))
    loop_print(from_zip("10282"))
    loop_print(from_zip_grade("10282", "A"))
    loop_print(from_zip_score("10282", 10))
    '''
    loop_print(from_zip_cuisine("10282", "Mexican"))

#run da main
main()
