from phone import Phone

item1 = Phone("jscphone", 1000, 3)

item1.apply_increment(0.2)
print(item1.price)
item1.send_email()

# for instance in Item.all:
#     print(instance.name)

""" item1.apply_discount()
print(item1.price) """


""" item2.pay_rate=0.7
item2.apply_discount()
print(item2.price) """


# print(Item.__dict__) #All the attributes for the class level.
# print(item1.__dict__) #All the attributes for the instance level.

""" print(item1.calc_total_price)
print(item2.calc_total_price) """


# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
