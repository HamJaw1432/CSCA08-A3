"""Assignment 3: Club Recommendations - Starter code."""
from typing import List, Tuple, Dict, TextIO


# Sample Data (Used by Doctring examples)

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
       'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}

# Helper functions

def update_dict(key: str, value: str,
                key_to_values: Dict[str, List[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []

    if value not in key_to_values[key]:
        key_to_values[key].append(value)

def make_person_to_friends(profile: List[str]) -> Dict[str, List[str]]:
    """Return a dict that takes the data in the list profile and matches it by 
    taking a person and mapping all their friends.
    
    Precondtion: The List is the profiles_file TextIO after a readlines
    """
    person_to_friends = {}
    for i in range(len(profile)):
        if i == 0 or profile[i -1] == '\n':
            j = 1
            while i + j in range(len(profile)) and profile[i + j] != '\n':
                if ',' in profile[i + j]:
                    comma_i_person = profile[i].find(',')
                    key = (profile[i][comma_i_person + 2:-1] + ' ' 
                           + profile[i][:comma_i_person])
                    
                    comma_i_friend = profile[i + j].find(',')
                    value = (profile[i + j][comma_i_friend + 2:-1] + ' ' 
                             + profile[i + j][:comma_i_friend])
                    
                    update_dict(key, value, person_to_friends)
                j = j + 1
                
    return person_to_friends

def make_person_to_club(profile: List[str]) -> Dict[str, List[str]]:
    """Return a dict that takes the data in the list profile and matches it by 
    taking a person and mapping all the culbs they are in.  
    
    Precondtion: The profile List is the profiles_file TextIO after a readlines
    
    
    """
    person_to_club = {}
    for i in range(len(profile)):
        if i == 0 or profile[i -1] == '\n':
            j = 1
            while i + j in range(len(profile)) and profile[i + j] != '\n':
                if ',' not in profile[i + j]:
                    comma_i_person = profile[i].find(',')
                    key = (profile[i][comma_i_person + 2:-1] + ' ' 
                           + profile[i][:comma_i_person])
                    
                    update_dict(key, profile[i + j][:-1], person_to_club)
                j = j + 1
                
    return person_to_club

def sort_dict_value(dic: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Update the dict so that the values are in alphabetical order.
    """
    for keys in dic:
        dic[keys].sort()
        
def clubs_of_club_members(person_to_clubs: Dict[str, List[str]],
                          person: str) -> List[str]:
    """Return a list of clubs of the people that are in the at least one of the
    same club as the person using the data in person_to_clubs
    """
    clubs_of_club_members_list = []
    clubs_to_persons = invert_and_sort(person_to_clubs)
    
    if person in person_to_clubs:
        for club in person_to_clubs[person]:
            for people in clubs_to_persons[club]:
                if people != person:
                    clubs_of_club_members_list = (clubs_of_club_members_list + 
                                                  person_to_clubs[people])    
    final = []
    for club in clubs_of_club_members_list:
        if person in person_to_clubs:
            if club not in person_to_clubs[person]:
                final.append(club)
        else:
            final.append(club)                 
    final.sort()
    return final
    
# Required functions
def load_profiles(profiles_file: TextIO) -> Tuple[Dict[str, List[str]],
                                                  Dict[str, List[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file.

    NOTE: Functions (including helper functions) that have a parameter
          of type TextIO do not need docstring examples.

    """
    file_list = profiles_file.readlines()
    person_to_friends = make_person_to_friends(file_list)
    person_to_club = make_person_to_club(file_list)
    sort_dict_value(person_to_friends)
    sort_dict_value(person_to_club)
    
    return (person_to_friends, person_to_club)

def get_average_club_count(person_to_clubs: Dict[str, List[str]]) -> float:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to.

    >>> get_average_club_count(P2C)
    1.6

    """
    if len(person_to_clubs) > 0:
        total = 0
        for key in person_to_clubs:
            total = total + len(person_to_clubs[key])
            
        return total/len(person_to_clubs)
    return 0.0


def get_last_to_first(
        person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary with the people
    from the "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True

    """
    new_dict = {}
    all_names = []
    for key in person_to_friends:
        if key not in all_names:
            all_names.append(key)
        for f_name in person_to_friends[key]:
            if f_name not in all_names:
                all_names.append(f_name)                  
    for name in all_names:
        sub_names = name.split()
        value = ''
        for i in range(len(sub_names)):
            if i != (len(sub_names)-2) and i != (len(sub_names)-1):
                value = value + sub_names[i] + ' '
        value = value + sub_names[len(sub_names)-2]
        update_dict(sub_names[-1], value, new_dict)    
    sort_dict_value(new_dict)            
    return new_dict


def invert_and_sort(key_to_value: Dict[object, object]) -> Dict[object, list]:
    """Return key_to_value inverted so that each key is a value (for
    non-list values) or an item from an iterable value, and each value
    is a list of the corresponding keys from key_to_value.  The value
    lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True

    """
    new_dict = {}
    for key in key_to_value:
        for value in key_to_value[key]:
            if type(key_to_value[key]) != list:
                update_dict(key_to_value[key], key, new_dict)
            else:
                update_dict(value, key, new_dict)
            
    sort_dict_value(new_dict)
                
    return new_dict


def get_clubs_of_friends(person_to_friends: Dict[str, List[str]],
                         person_to_clubs: Dict[str, List[str]],
                         person: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']

    """
    new_list = []
    if person in person_to_friends:
        for friends in person_to_friends[person]:
            if friends in person_to_clubs:
                for clubs in person_to_clubs[friends]:
                    new_list.append(clubs)
    final = []
    for club in new_list:
        if person in person_to_clubs:
            if club not in person_to_clubs[person]:
                final.append(club)
        else:
            final.append(club)
    final.sort()
    return final

def recommend_clubs(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str,) -> List[Tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner',)
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]

    """
    recommend_clubs_final = []
    recommend_clubs_temp_one = (get_clubs_of_friends(person_to_friends,
                                                     person_to_clubs, person) + 
                                clubs_of_club_members(person_to_clubs, person))
    club_to_num = {}   
    for club in recommend_clubs_temp_one:
        if club not in club_to_num:
            club_to_num[club] = 1
        else:
            club_to_num[club] = club_to_num[club] + 1            
    highest = 0
    for club in club_to_num:
        if club_to_num[club] > highest:
            highest = club_to_num[club]
    for num in range(highest):
        recommend_clubs_temp_two = []
        for club in club_to_num:
            if club_to_num[club] == (highest - num):
                recommend_clubs_temp_two.append(club)
                recommend_clubs_temp_two.sort()
        for club in recommend_clubs_temp_two:
            recommend_clubs_final.append((club, highest - num))            
    return recommend_clubs_final

if __name__ == '__main__':
    pass
    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod() 