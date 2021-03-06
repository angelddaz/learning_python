'''
Created on Apr 24, 2017

@author: angel
3-5      DONE
6-8      DONE
9-10     DONE
11-13    DONE
14-16    DONE
17-19    DONE
20-22    DONE
23-25    EASIESTEST
'''

users = [[0, "Hero", 0],
         [1, "Dunn", 2],
         [2, "Sue", 3],
         [3, "Chi", 3]]

class Table:
    def __init__(self, columns):
        self.columns = columns
        self.rows = []

 def __repr__(self):
    """pretty representation of the table: columns then rows"""
    return str(self.columns) + "\n" + "\n".join(map(str, self.rows))

def insert(self, row_values):
    if len(row_values) != len(self.columns):
        raise TypeError("wrong number of elements")
    row_dict = dict(zip(self.columns, row_values))
    self.rows.append(row_dict)
 
users = Table(["user_id", "name", "num_friends"])
users.insert([0, "Hero", 0])
users.insert([1, "Dunn", 2])
users.insert([2, "Sue", 3])
users.insert([3, "Chi", 3])
users.insert([4, "Thor", 3])
users.insert([5, "Clive", 2])
users.insert([6, "Hicks", 3])
users.insert([7, "Devin", 2])
users.insert([8, "Kate", 2])
users.insert([9, "Klein", 3])
users.insert([10, "Jen", 1])

#I know SQL relatively well so this chapter is a bit of a breeze

#CHAPTER 24 MAPREDUCE

#Before this book, I had a lot of semi unknown unknowns.
#Now there are many known unknowns.

#just reading for this chapter

#CHAPTER 25
#SOME MORE READING

