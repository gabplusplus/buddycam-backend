from random import choice


def lat_value():
    choices = ['14.211899931611912', '14.211834692872843', '14.211946938420407', '14.211754250374241', '14.211958162987724', '14.212055442386603']
    value = choice(choices)
    return value

def long_value():
    choices = ['121.16765544429474', '121.16784339743158', '121.16753076641989', '121.16760409966986', '121.16764848554729', '121.16777006438896']
    value = choice(choices)
    return value