def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile
user_profile = build_profile('kate', 'may', language='chinese', gender='female')
print(user_profile)
