# find users with lots of restaurante reviews
# in this case, find one user to start with,
# for each restaurant
# then, figure out how to do it for all users that have a certain number of reviews.



'''
 db.users.find({user_id: "G-uVT9JxNMbrPApvuVO6pg" }  )


  db.users.find({review_count:{$gt:10000}})



  db.academic_reviews.find( {user_id: "G-uVT9JxNMbrPApvuVO6pg"})
'''

# generate the model on 80% of the reviews


# for the last 20% of reviews, find all reviews not from that user




#############

from pymongo import MongoClient
from datetime import datetime
import json
import pdb

'''
create a list of all users that have reviews over 1000
'''
conn = MongoClient(ip, 27017)

c = db.get_collection('academic_reviews')
u = db.get_collection('users')



biguser = []

for obj in u.find({'review_count':{'$gt':1000}}):
    print(obj['user_id'])
    biguser.append(obj['user_id'])

'''
get the business ids of the places they review
'''


biznames =[]

for user in biguser:
    for obj in c.find({'user_id':user}):
        biznames.append(obj['business_id'])
    return biznames

'''
next step - build a list of reviews for each business
'''

'''
then build a "generative " data set from each user and a test set
'''




conn = MongoClient()

print(conn.database_names())

db = conn.get_database('yelpbiz')

print(db.collection_names())


c = db.get_collection('academic_reviews')
u = db.get_collection('users')


states =c.distinct('state')
print(states)
test = db.academic_reviews.find_one()
print(test)

guser =db.academic_reviews.find({'user_id': 'G-uVT9JxNMbrPApvuVO6pg'})
print(guser)

print(db.academic_reviews.index_information())




for obj in c.find( ):
        try:
            if len(reviews_dict[obj['state']]) > num_reviews:
                continue
        except KeyError:
            pass
        if datetime.strptime(obj['date'][0:4], '%Y') >= threshold_year:
            del obj['_id']
            try:
                reviews_dict[obj['state']].append(obj)
            except KeyError:
                reviews_dict[obj['state']]=[obj]
        else:
            pass



#pdb.set_trace()
