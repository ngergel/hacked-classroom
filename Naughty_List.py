f = open('newmaster_dict.txt', 'r')
data = f.read()
exec('master = '+data)

g = open('naughtylist.txt', 'r')
naughtydata = g.read()
exec('naughtylist = ' +naughtydata)

for naughty in naughtylist:
    try:
        del master['(' + naughty + ')']
        print(naught + " was DELETED!")
    except KeyError:
        print(naughty + " was not found")



f = open('newmaster_dict.txt', 'w')
f.write(str(master))
f.close()