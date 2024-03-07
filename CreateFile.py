import xmlStuff
import zipfile
import os
def CreateFile(Path, Dest):
	Game = Path
	with zipfile.ZipFile("game.bsc", "r") as ZIP:
	    ZIP.extractall("decomp")
	Tree = xmlStuff.UltraTree(3)
	with open("decomp/gamebox.weapons", "wb") as f:
		Tree.write(f)
	def zipdir(path, ziph):
		for root, dirs, files in os.walk(path):
			for file in files:
				ziph.write(os.path.join(root, file), 
				os.path.relpath(os.path.join(root, file), 
				os.path.join(path, "..")))
	with open(Dest, "w") as f:
		f.write("")
	with zipfile.ZipFile(Dest, "w", zipfile.ZIP_DEFLATED) as zipf:
		zipdir("decomp", zipf)