from __future__ import print_function
import re
import spacy

from pyclausie import ClausIE


nlp = spacy.load('en')
re_spaces = re.compile(r'\s+')


class Person(object):
    def __init__(self, name, likes=None, has=None, travels=None):
        """
        :param name: the person's name
        :type name: basestring
        :param likes: (Optional) an initial list of likes
        :type likes: list
        :param dislikes: (Optional) an initial list of likes
        :type dislikes: list
        :param has: (Optional) an initial list of things the person has
        :type has: list
        :param travels: (Optional) an initial list of the person's travels
        :type travels: list
        """
        self.name = name
        self.likes = [] if likes is None else likes
        self.has = [] if has is None else has
        self.travels = [] if travels is None else travels

    def __repr__(self):
        return self.name


class Pet(object):
    def __init__(self, pet_type, people, name=None):
        self.name = name
        self.type = pet_type
        self.people = people

    def __repr__(self):
         return '%s:%s'%(self.people,self.name)


class Trip(object):
    def __init__(self,time, name, to ):
        self.time = time
        self.name = name
        self.to = to


persons = []
pets = []
trips = []
root = None

def get_data_from_file(file_path='/Users/heli/Desktop/assignment_01_data.txt'):
    with open(file_path) as infile:
        cleaned_lines = [line.strip() for line in infile if not line.startswith(('$$$', '###', '==='))]

    return cleaned_lines


def select_person(name):
    for person in persons:
        if person.name == name:
            return person


def add_person(name):
    person = select_person(name)

    if person is None:
        new_person = Person(name)
        persons.append(new_person)

        return new_person

    return person
#add trip
def select_trip(time, name):
    for trip in trips:
        if trip.time == time and trip.name == name:
            return trip
def add_trip(time, name, to):
    trip = select_trip(time,name)
    if trip is None:
        new_trip = Trip(time, name, to)
        trips.append(new_trip)
        return new_trip
    return trip

# def get_persons_trip(person_name):
#     person = select_person(person_name)
#     for thing in person.has:
#         if isinstance(thing, Pet):
#             return thing


def select_pet(name):
    for pet in pets:
        if pet.name == name:
            return pet


def add_pet(type, people, name=None, ):
    pet = None

    if name:
        pet = select_pet(name)

    if pet is None:
           pet = Pet(type, people, name)
           pets.append(pet)

    return pet


def get_persons_pet(person_name):

    person = select_person(person_name)

    for thing in person.has:
        if isinstance(thing, Pet):
            return thing



def process_relation_triplet(triplet):
    """
    Process a relation triplet found by ClausIE and store the data
    find relations of types:
    (PERSON, likes, PERSON)
    (PERSON, has, PET)
    (PET, has_name, NAME)
    (PERSON, travels, TRIP)
    (TRIP, departs_on, DATE)
    (TRIP, departs_to, PLACE)
    :param triplet: The relation triplet from ClausIE
    :type triplet: tuple
    :return: a triplet in the formats specified above
    :rtype: tuple
    """

    sentence = triplet.subject + ' ' + triplet.predicate + ' ' + triplet.object

    doc = nlp(unicode(sentence))
    global root
    for t in doc:
        if t.pos_ == 'VERB' and t.head == t:
            root = t
        # elif t.pos_ == 'NOUN'

    # also, if only one sentence
    # root = doc[:].root


    """
    CURRENT ASSUMPTIONS:
    - People's names are unique (i.e. there only exists one person with a certain name).
    - Pet's names are unique
    - The only pets are dogs and cats
    - Only one person can own a specific pet
    - A person can own only one pet
    """


    # Process (PERSON, likes, PERSON) relations
    if root.lemma_ == 'like':
        x = 1
        for x in doc:
            if x.text == "n't":
                x =0
        if x:
            fw_doc = nlp(unicode(triplet.object))


            if triplet.subject in [e.text for e in doc.ents if e.label_ == 'PERSON']:
               s = add_person(triplet.subject)
               for w in fw_doc.ents:
                 if w.label_=='PERSON':
                    likelist = w.text
                    o = add_person(likelist)
                    s.likes.append(o)
    if root.lemma_ == 'be' and 'friends' in triplet.object:

            # print(x)
            friends_doc = nlp(unicode(triplet.subject))
            friends_list = [e.text for e in friends_doc.ents if e.label_ == 'PERSON' or e.label_ == 'ORG']
            if len(friends_list) == 2:

                s = add_person(friends_list[0])
                b = add_person(friends_list[1])
                #print(s)
                #print(b)
                s.likes.append(b)
                b.likes.append(s)




    if root.lemma_ == 'be' and triplet.object.startswith('friends with'):

        # x=0
        # for x in doc:
        #     if x.text == "n't":
        #         x =1
        # if x != 1:


        fw_doc = nlp(unicode(triplet.object))
# fw_who = [e for e in fw_doc.ents if e.label_ == 'PERSON'][0].text

        if triplet.subject in [e.text for e in doc.ents if e.label_ == 'PERSON']:
            s = add_person(triplet.subject)
            fw_person = [str(e) for e in fw_doc.ents if e.label_ == 'PERSON']
            fw_all = ' '.join(fw_person)
            fw_last = fw_all.split(' ')
            for x in fw_last:
                o = add_person(x)
                s.likes.append(o)
                o.likes.append(s)
    #process(person, have , pet)
    if root.lemma_ == 'have'and ('dog' in triplet.object or 'cat' in triplet.object):
            if 'named' in triplet.object:

                for e in doc.ents:
                    if e.label_ == 'PERSON':
                     x = add_person(triplet.subject)
                     n = triplet.object.find('named')
                     pet_name = triplet.object[n + 6:]
                    if x.has:
                        if x.has[0].name:
                            x=0
                        else:
                            x.has[0].name = pet_name
                    else:
                        x_pet_type = 'dog' if 'dog' in triplet.object else 'cat'
                        pet = add_pet(x_pet_type, x ,pet_name)
                        x.has.append(pet)
            else:
                for e in doc.ents:
                    if e.label_ == 'PERSON':
                        x = add_person(e.text)

                        x_pet_type = 'dog' if 'dog' in triplet.object else 'cat'
                        pet = add_pet(x_pet_type, x)

                        x.has.append(pet)






# Process (PET, has, NAME)
    if triplet.subject.endswith('name') and ('dog' in triplet.subject or 'cat' in triplet.subject):
        obj_span = doc.char_span(sentence.find(triplet.object), len(sentence))

        # handle single names, but what about compound names? Noun chunks might help.
        if len(obj_span) == 1 and obj_span[0].pos_ == 'PROPN':
            name = triplet.object
            subj_start = sentence.find(triplet.subject)
            subj_doc = doc.char_span(subj_start, subj_start + len(triplet.subject))

            s_people = [token.text for token in subj_doc if token.ent_type_ == 'PERSON']
            assert len(s_people) == 1
            s_person = select_person(s_people[0])

            s_pet_type = 'dog' if 'dog' in triplet.subject else 'cat'

            pet = add_pet(s_pet_type, s_person, name)
            s_person.has.append(pet)

#

    for e in doc.ents:
             if e.label_ =='GPE':
                 place=e.text
                 #print(place)
                 time = [str(e.text) for e in doc.ents if e.label_ == 'DATE']
                 personlist = [e.text for e in doc.ents if e.label_ == 'PERSON' or e.label_ == 'ORG']
                 #print(personlist)
                 for person in personlist:
                     s = add_person(person)
                     o = add_trip(time, s.name, place)
                     s.travels.append(o)



def preprocess_question(question):
    # remove articles: a, an, the

    q_words = question.split(' ')

    # when won't this work?
    for article in ('a', 'an', 'the'):
        try:
            q_words.remove(article)
        except:
            pass

    return re.sub(re_spaces, ' ', ' '.join(q_words))


def has_question_word(string):
    # note: there are other question words
    for qword in ('who', 'what'):
        if qword in string.lower():
            return True

    return False



def main():
    sents = get_data_from_file()

    cl = ClausIE.get_instance()

    triples = cl.extract_triples(sents)

    for t in triples:
        r = process_relation_triplet(t)
        # print(r)
    #print(persons)
    #print(pets)
    question = ' '
    while question[-1] != '?':
        question = raw_input("Please enter your question: ")

        if question[-1] != '?':
            print('This is not a question... please try again')
    answer_question(question)
    # q_trip = cl.extract_triples([preprocess_question(question)])[0]

    # (WHO, has, PET)
    # here's one just for dogs
   # if q_trip.subject.lower() == 'who' and q_trip.object == 'dog':
        #answer = '{} has a {} named {}.'

        # for person in persons:
        #     pet = get_persons_pet(person.name)
        #     if pet and pet.type == 'dog':
        #         print(answer.format(person.name, 'dog', pet.name))

def answer_question(question_string):
    if 'What' in question_string:
       e_doc = nlp(unicode(question_string))
       for e in e_doc.ents:
           #print(9)
           if e.label_ == 'PERSON':
                person = e.text
                #print(person)
                for x in persons:
                    if x.name == person:
                        for e in x.has:
                            #print(e.name)
                            if e.name != None:
                             print(e.name)


    else:
        cl = ClausIE.get_instance()
        # q1
        q_trip = cl.extract_triples([preprocess_question(question_string)])[0]
        sentence = q_trip.subject + ' ' + q_trip.predicate + ' ' + q_trip.object

        doc = nlp(unicode(sentence))
        # print(q_trip.object)
        # print(q_trip.predicate)
        # print(q_trip.subject)
        if q_trip.subject.lower() == 'who' and ('dog' in q_trip.object or 'cat' in q_trip.object):

            answer = '{} has a {}.'

            pet_type = 'dog' if 'dog' in q_trip.object else 'cat'
            for person in persons:
                pet = get_persons_pet(person.name)
                if pet:
                    if pet.type == pet_type:
                        print(answer.format(person.name, pet_type, pet.name))
        # q2
        if q_trip.subject.lower() == 'who' and (root.lemma_ == 'go' or 'fly' or 'travel'):
            answer = '{} is going to {}, time:{}'

            place_doc = nlp(unicode(q_trip.object))
            for e in place_doc.ents:
                if e.label_ == 'GPE':

                    place = e.text
                    # print(place)
                    for trip in trips:
                        if trip.to == place and len(trip.time) > 0:
                            print(answer.format(trip.name, trip.to, trip.time))
        # q3
        if 'does' in q_trip.subject.lower():
            # answer = '{} likes {}'
            sent = q_trip.subject + ' ' + q_trip.predicate + ' ' + q_trip.object

            e_doc = nlp(unicode(sent))
            list = [str(e) for e in e_doc.ents if e.label_ == 'PERSON' or e.label_ == 'ORG']
            x = 0
            # print(list)
            subject = list[0]
            object = q_trip.object

            for person in persons:
                # print(9)
                if person.name == subject:
                    for personA in person.likes:
                        # print(personA.name)
                        if personA.name == object:
                            x = 1
                        # print(x)
            if x:
                print("y")
            else:
                print("N")
        # q4
        if 'when' in q_trip.object and (root.lemma_ == 'go' or root.lemma_ == 'fly' or root.lemma_ == 'travel'):
            answer = '{} is going to {}, time:{}'

            e_doc = nlp(unicode(q_trip.object))
            for e in e_doc.ents:
                if e.label_ == 'GPE':

                    place = e.text
                    # print(place)
                    for trip in trips:
                        if trip.to == place and len(trip.time) > 0:
                            print(answer.format(trip.name, trip.to, trip.time))

        # q5
        if 'who' in q_trip.subject.lower():
            answer = '{} likes {}'
            # e_doc = nlp(unicode(q_trip.object))

            for e in doc.ents:

                if e.label_ == 'PERSON':

                    person1 = e.text
                    #print(person1)
                    for person in persons:

                        for e in person.likes:
                            if e.name == q_trip.object:
                                print(person.name)

        # q6
        if root.lemma_ == 'like':
            x = 1
            for x in doc:
                if x.text == "n't":
                    x = 0
            if x:
                fw_doc = nlp(unicode(q_trip.object))

                if 'who' in q_trip.object.lower():
                 answer = '{} likes {}'

                e_doc = nlp(unicode(question_string))
                for e in e_doc.ents:

                  if e.label_ == 'PERSON':
                    person = e.text

                    for person in persons:
                        #print(person)
                        if person.name == q_trip.subject:
                            for e in person.likes:
                                print(e.name)

    #



if __name__ == '__main__':
    main()
