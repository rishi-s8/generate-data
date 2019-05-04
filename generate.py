import random
import string

n = 1000000

table = "dept"
schema = ["did", "name", "budget", "managerid"]
datatypes = [int, str, int, int]
for i in range(n):
    data = []
    for index, z  in enumerate(schema):
        if datatypes[index] == str:
            s = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
            data.append("\'{}\'".format(s))
        else:
            data.append("{}".format(random.randint(0,1000000000)))
    prefix = "INSERT INTO {}({}) VALUES({});".format(table, ', '.join(map(str,schema)), ', '.join(map(str,data)))
    print(prefix)
