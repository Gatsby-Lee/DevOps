#!python3
# https://stackoverflow.com/questions/17912307/u-ufeff-in-python-string
# coding: utf8
u = 'ABC'
e8 = u.encode('utf-8')        # encode without BOM
e8s = u.encode('utf-8-sig')   # encode with BOM
e16 = u.encode('utf-16')      # encode with BOM
e16le = u.encode('utf-16le')  # encode without BOM
e16be = u.encode('utf-16be')  # encode without BOM
print('utf-8     %r' % e8)
print('utf-8-sig %r' % e8s)
print('utf-16    %r' % e16)
print('utf-16le  %r' % e16le)
print('utf-16be  %r' % e16be)
print
print('utf-8  w/ BOM decoded with utf-8     %r' % e8s.decode('utf-8'))
print('utf-8  w/ BOM decoded with utf-8-sig %r' % e8s.decode('utf-8-sig'))
print('utf-16 w/ BOM decoded with utf-16    %r' % e16.decode('utf-16'))
print('utf-16 w/ BOM decoded with utf-16le  %r' % e16.decode('utf-16le'))
