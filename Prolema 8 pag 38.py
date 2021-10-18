a='A B C D E F G H I J  L M N O P Q R S T U V W Y Z'
p1=''
p2=''
p3=''

for i in a:
    b=chr(ord(i)+1)
    p1+=b
    c=p1.replace('!',' ')
    d=c.replace('[','A')

print('Pimul punct:',d)

p2=d
for i in a:
    e=p2.replace(('Z'),('A'))
    f=p2.replace('!',' ')
    g=d.replace('[','A')
print('Al doilea punct',g)

print('Al treilea punct',a.replace(' ','-',len(a)))