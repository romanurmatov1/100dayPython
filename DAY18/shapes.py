import turtle as t

tim = t.Turtle()

for a in range(3,20):

   b = 360/a
   for i in range(a):
      tim.forward(100)
      tim.left(b)
   
# print