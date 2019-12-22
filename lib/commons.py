import hashlib
import uuid

def create_uuid():
    return str(uuid.uuid1())

def md5(string):
    m = hashlib.md5()
    m.update(bytes(string,'utf8'))
    return m.hexdigest()




if __name__ == "__main__":
    res = md5('123')
    u = create_uuid()
    print(res)
    print(u,type(u))