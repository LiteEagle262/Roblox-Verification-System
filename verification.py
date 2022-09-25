import json,requests

def gen_phrase():
  r = requests.get("https://random-word-api.herokuapp.com/word?number=15")
  phrase = r.json()
  return f"VERFICIATION: {phrase[0]} {phrase[1]} {phrase[2]} {phrase[3]} {phrase[4]} {phrase[5]} {phrase[6]} {phrase[7]} {phrase[8]} {phrase[9]} {phrase[10]} {phrase[11]} {phrase[12]} {phrase[13]} {phrase[14]}"

def phrase(user_id):
    acc = json.load(open(f"db/{user_id}.json", "r"))
    return acc['phrase']


def check(user_id):
  r = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
  jso = r.json()
  if phrase(user_id) in jso['description']:
    return True
  else:
    return False

def getid(username):
    try:
        r = requests.get(f"https://api.roblox.com/users/get-by-username?username={username}")
        jso = r.json()
        return jso['Id']
    except:
        return False

def register(username):
    user_id = getid(username)
    if user_id not False:
        json.dump({"phrase": gen_phrase()}, open(f"data/db/{user_id}.json", "x"))
        return True
    else:
        return False
