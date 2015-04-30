#[Double Gold Star] Define a procedure, involved(courses, person), that takes as
#input a courses structure and a person and returns a Dictionary that describes
#all the courses the person is involved in.  A person is involved in a course if
#they are a value for any property for the course.  The output Dictionary should
#have hexamesters as its keys, and each value should be a list of courses that
#are offered that hexamester (the courses in the list can be in any order).

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }

#For the following questions, you will find the
#        for <key> in <dictionary>:
#                   <block>
#construct useful.  This loops through the key values in the Dictionary.  For
#example, this procedure returns a list of all the courses offered in the given
#hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res
    
    
def involved(courses, person):
    result = {}
    for key in courses.keys():
        subDictionary = courses[key]
        coursesList=[]
        for k in subDictionary.keys():
            subSub = subDictionary[k]
            for ke in subSub.keys():
                if subSub[ke] == person:
                    coursesList.append(k)
        if coursesList: #is not empty
            result[key]=coursesList
            
    return result
    
