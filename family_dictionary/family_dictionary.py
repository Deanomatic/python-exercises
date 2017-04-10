my_family = {
    'sister': {
        'name': 'Theresa',
        'age': 26
    },
    'mother': {
        'name': 'Necie',
        'age': 55
    },
    'father': {
    	'name': 'Rick',
    	'age': 57
    },
    'brother': {
    	'name': 'Spencer',
    	'age': 18
    },
    'other brother': {
    	'name': 'Nathan',
    	'age': 16
    },
    'other sister': {
    	'name': 'Audrey',
    	'age': 23
    }
}

for key,value in my_family.items():
    print(value["name"] + " is my " + key + " and is " + str(value["age"]) + " years old.")
