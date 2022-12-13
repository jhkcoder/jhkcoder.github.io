def print_last_info(**data):

    for key, value in data.items():
        string = ("{} is {}".format(key,value))
    return string

ans8a = print_last_info(Name= "Rosie", Age= 33, Profession= "Data Scientist")

print(ans8a)
