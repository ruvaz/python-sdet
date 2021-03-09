import json

courses = '{ "name": "ruben","languages": ["java", "python"]}'

dict_courses = json.loads(courses)
print(dict_courses)
print(type(dict_courses))  # <class 'dict'>
print(dict_courses['name'])  # ruben
print(dict_courses['name'][0])  # r
print(dict_courses['languages'][0])  # java
print(type(json.dumps(dict_courses)))  # <class 'str'>
print(json.dumps(dict_courses))  # {"name": "ruben", "languages": ["java", "python"]}

languages = dict_courses['languages']
for lan in languages:
    print(lan)

print("------------------")

with open('json.txt') as f:
    data = json.load(f)
    print(data)
    print("-------------")
    print("glossary:", data['glossary'])

    print("title:", data['glossary']['title'])
    print("GlossEntry:")
    print(data['glossary']['GlossEntry'])
    print(data['glossary']['GlossEntry']['ID'])
    print(data['glossary']['GlossEntry']['GlossSeeAlso'])
    print(data['glossary']['GlossEntry']['GlossSeeAlso'][0])
    print(data['glossary']['GlossEntry']['GlossSeeAlso'][1])

    for gloss in data['glossary']['GlossEntry']['GlossSeeAlso']:
        print(gloss)
        assert gloss != "-XML"

with open("json2.json") as f2:
    data2 = json.load(f2)
    # print(data == data2)
    assert data == data2
