def hashtable_lookup(htable,key):
    
    #calculating in which bucket to look
    
    b=hash_string(key, len(htable))
    print (htable[b])
    
    #check if the key is in the htable
    for elem in htable[b]:
        if key in elem:
            return elem[1]
    else: 
        return None

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])


def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table
