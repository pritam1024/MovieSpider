set x = createobject("wscript.shell")
movie = wscript.Arguments(0)
x.run("mplayerc.exe "&movie)