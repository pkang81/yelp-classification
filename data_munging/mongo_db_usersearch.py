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
import csv

'''
create a list of all users that have reviews over 1000
'''
conn = MongoClient()

db = conn.get_database('yelpbiz')


c = db.get_collection('academic_reviews')
u = db.get_collection('users')



biguser = []

for obj in u.find({'review_count':{'$gt':30}}):
    print(obj['user_id'])
    biguser.append(obj['user_id'])








'''
get the business ids of the places they review
'''

userreview = {}

for user in biguser:
    ulist = []
    for obj in c.find({'$and':[{'user_id':user,'stars':{'$gte':4}}]):
        ulist.append(obj)
        userreview.update({user:ulist})
# this throws an error because the first key is a bson object
# gotta fix this

keys =userreview.keys()

for key in keys:
    for review in userreview[key]:
        if '_id' in review: del review['_id']


with open('user_review_dictionary.json', 'w') as outfile:
    json.dump(userreview, outfile)




biznames =[]

for key in keys:
    for review in userreview[key]:
       biznames.append(review['business_id'])

restreview = {}

for restaurant in biznames:
    rlist = []
    for obj in c.find({'$and':[{'user_id':restaurant,'stars':{'$gte':4}}]):
        rlist.append(obj)
        restreview.update(restaurant:rlist})


with open('rest_review_dictionary.json', 'w') as outfile:
    json.dump(restreview, outfile)


'''
next step - build a list of reviews for each business
'''

'''
then build a "generative " data set from each user and a test set
'''


'''
scrap code


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
        if datetime.strptime(obj['date'][0:4], '') >= threshold_year:
            del obj['_id']
            try:
                reviews_dict[obj['state']].append(obj)
            except KeyError:
                reviews_dict[obj['state']]=[obj]
        else:
            pass



#pdb.set_trace()
'''
