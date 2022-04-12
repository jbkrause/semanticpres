import hashlib
import sys
import os

id = sys.argv[1]

# id must not contain linereturns and must be in bytes
id = id.replace('\r','').replace('\n','')
id = id.encode('utf-8')
id = b'info:fedora/' + id

# compute sha256 digest
m = hashlib.sha256()
m.update(id)
hd = m.hexdigest()

# print out results
print('Fedora ID:', id)
print('Hexdigest:', hd )
print('Storage path:', hd[0:3]+ os.sep + hd[3:6] + os.sep + hd[6:9] + os.sep + hd )