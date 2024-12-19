import json

"""
Requires initial .json file from Instagram as the Instagram API has limited usages.
"""

def get_following(file: str) -> list[str]:
    account_following = []
    with open(file, 'r') as f:
        data = json.load(f)
    if isinstance(data, dict):
        for v in data.values():
            for item in v:
                str_data = item.get('string_list_data')
                for f in str_data:
                    account_following.append(f.get('value'))
    elif isinstance(data, list):
        for l in data:
            str_data = l.get('string_list_data')
            for item in str_data:
                account_following.append(item.get('value'))

    return account_following

following = get_following('following.json')
followers = get_following('followers_1.json')

not_following_back = set(following) - set(followers)

with open('hello.txt', 'w') as t:
    for row in list(not_following_back):
        t.write(row + '\n')
