for n in list(map(str,range(99,0,-1)))+["no more"]:
	A,B=" bottle%s of beer"%(["","s"][n!='1'])," on the wall"
	print((n+A+B+".\n\n")*(n!='99')+n.capitalize()+A+B+",",n+A+".\nTake one down and pass it around, "*(n!="no more")+(".\nGo to the store and buy some more, 99"+A+B+".")*(n=="no more"),end="")