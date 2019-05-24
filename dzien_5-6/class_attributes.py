class ClassWithClassAttributes:

    c = "I'm a class attribute and I'm proud of it!"

    def print_attribute(self):
        print("***")
        print(c)

print(ClassWithClassAttributes.c)
c1 = ClassWithClassAttributes()
print(c1.c)
c1.print_attribute()

# c1.c = "New class attribute"
# print(ClassWithClassAttributes.c)
# ClassWithClassAttributes.c = "New class attribute"
# print(ClassWithClassAttributes.c)
# print(c1.c)
