f = open('newmaster_dict.txt', 'r')
data = f.read()
exec('master = '+data)

roomdel = input("What room do you want to delete?")

try:
    del master['(' + roomdel + ')']
except KeyError:
    print("Key" + roomdel + "was not found")


f = open('newmaster_dict.txt', 'w')
f.write(str(master))
f.close()