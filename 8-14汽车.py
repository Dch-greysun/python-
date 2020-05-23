def make_car(maker, t_name, **other_info):
    profile = {}
    profile['maker_name'] =maker.title()
    profile['type_name'] =t_name.title()
    for key,value in other_info.items():
        profile[key] = value
    return profile
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
