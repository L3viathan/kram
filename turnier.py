#!/usr/bin/python3
def p(l):
	r=[]
	while len(l)>1:
		r+=[(l.pop(),l.pop())]
	return r if not l else r+[(l[0],l[0])]
a=[]
while True:
	i=input("Neuer Spieler? Name: ")
	if not i: break
	a+=[i]
while len(a)>1:
	(m,a)=(p(a),[])
	for (o,t) in m:
		if o==t:
			a+=[o]
			continue
		print(o,"spielt gegen",t)
		a+=[input("Wer hat gewonnen? Name: ")]
if a: print("Gewinner:",a[0])
