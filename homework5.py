immutable_var = 5,8,10,False,"Privet"
print(immutable_var)
# Кортежи в Python являются неизменяемыми структурами данных, поэтому при попытке их изменить будет выдавать ошибку.
mutable_list = [12,7,True,"Yes"]
print(mutable_list)
mutable_list[0] = 6
mutable_list[1] = 54
mutable_list[2] = False
mutable_list[3] = "No"
print(mutable_list)