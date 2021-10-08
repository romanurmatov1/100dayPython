class User:
   def __init__(self, id, name):
      self.id1 = id
      self.name1 = name
      self.followers = 1
      self.following = 3
   def follow(self, user):
      user.followers += 1
      self.following += 1

user1 = User('1','roma')
user2 = User('2','ufo')

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)