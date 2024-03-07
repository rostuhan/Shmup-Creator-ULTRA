import xmlStuff
Tree = xmlStuff.UltraTree(3)
with open("Tree.txt", "wb") as f:
	Tree.write(f)