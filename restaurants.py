from pymongo import MongoClient

c = MongoClient("lisa.stuy.edu")
r = c["test"]["restaurants"]

def from_borough(boro):
    qd = { "borough" : boro }
    return r.find(qd)

def from_zip(zip):
    qd = { "address.zipcode" : zip }
    return r.find(qd)

def from_zip_grade(zip, grade):
    qd = { $and : [ { "address.zipcode" : zip }, { "grades.grade" : grade } ] } 
    return r.find(qd)
    
def loop_print(cursor):
    for i in cursor:
        print i
        
def main():
    #loop_print(from_borough("Manhattan"))
    loop_print(from_zip("10282"))
    
    
main()
