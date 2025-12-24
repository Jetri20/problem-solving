def generate_hashtag(s):
    
    if len(s) == 0:
        return False
    
    capital = list(map(lambda i: i.capitalize(), s.split()))
    result = "#{}".format("".join(capital))
    
    return False if len(result) > 140 else result 

