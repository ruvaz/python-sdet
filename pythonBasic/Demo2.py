# lists
# values = []
values = [1, 2, "ruben", 4, 5]
print(values)
print(values[2])  # Ruben
print(values[3])  # 4

# last in the list
print(values[-1])  #

# between 1 & 3  =  1,2
print(values[1:3])  # [2, 'ruben']

# Insert in a position
values.insert(3, "Daniel")  # [1, 2, 'ruben', 'Daniel', 4, 5]
print(values)

# add at end
values.append("end")  # [1, 2, 'ruben', 'Daniel', 4, 5, 'end']
print(values)

# update a values
values[2] = "GADI"
print(values)  # [1, 2, 'GADI', 'Daniel', 4, 5, 'end']

# delete values
del values[0]  # [2, 'GADI', 'Daniel', 4, 5, 'end']
print(values)

values.remove("Daniel")  # [2, 'GADI', 4, 5, 'end']
print(values)
#  Tuplas --------same has list but inmutable -> no se puede reasisgnar algo de nuevo, no puede cambiar de valor -------

tupla = (1, 2, "ruben", 4.5)
print(tupla)

# no se puede hacer
# tupla[2] = "GADI"  # TypeError: 'tuple' object does not support item assignment


# diccionario

dic = {
    "key": "value",
    "a": "b",
    4: "12",
    5: 6,
    "abc": "1234567",
    tupla: "tupla key",
    "tuplas": tupla,
    "lista": values
}
print(dic)
print(dic[tupla])  # tupla key
print(dic["abc"])  # 1234567
print(dic[5])  # 6
print(dic["lista"])  # [2, 'GADI', 4, 5, 'end']
print(dic.values())
# dict_values(['value', 'b', '12', 6, '1234567', 'tupla key', (1, 2, 'ruben', 4.5), [2, 'GADI', 4, 5, 'end']])

print(dic.items())
# dict_items([('key', 'value'), ('a', 'b'), (4, '12'), (5, 6), ('abc', '1234567'), ((1, 2, 'ruben', 4.5), 'tupla key'), ('tuplas', (1, 2, 'ruben', 4.5)), ('lista', [2, 'GADI', 4, 5, 'end'])])

