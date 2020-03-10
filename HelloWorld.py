print("Hello World !")

bodmasoperation='a=3\nb=8\nd=7\nc=a+b*d\nprint(c)'
performoperation=compile(bodmasoperation,"Bodmas",'exec')
exec(performoperation)

codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')

exec(codeObejct)




