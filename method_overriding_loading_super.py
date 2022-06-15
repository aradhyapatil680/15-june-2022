# #method overloading
# class Method_Over:
#     def multiopp(self, a=None, b=None, c=None):
#         if a!=None and b!=None and c!=None:
#             m = a+b+c
#             print("Addition = ",m)
#         elif a!=None and b!=None:
#             m = a*b
#             print("Multiplication = ",m)
#         else:
#             print("ERROR, Pls Enter Proper Value ")
#         return m
# obj=Method_Over()
# print(obj.multiopp(10))

# #method overiding
# class Method_Ride:
#     def sum (self, a, b):
#         m = a+b
#         return m
#
# class Method_iddd(Method_Ride):
#     def sum(self, a, b):
#         m = a*b
#         return m
#
# obj=Method_iddd()
# print(obj.sum(10,20))


#Super method overiding
class Method_Ride:
    def sum (self, a, b):
        m = a+b
        print("addition = ", m)

class Method_iddd(Method_Ride):
    def sum(self, a, b):
        super().sum(a,b)
        m = a*b
        print("multiplication = ", m)

obj=Method_iddd()
print(obj.sum(10,20))