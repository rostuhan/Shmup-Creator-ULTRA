def UltraTree(Amount):
	import xml.etree.ElementTree as ET
	import copy
	File = "decomp/old.weapons"
	with open(File, "r") as f:
		Tree = ET.fromstring("<root>" + f.read() + "</root>")
		Tree = ET.ElementTree(Tree)
	for i in Tree.iter("weapon"):
		Repeater = i.find("repeater")
		Gameplay = i.find("Gameplay")
		try:
			if Gameplay.get("isPlayerUsingAI") == "false":
				if Repeater.get("repeater_angle") == "360" and Repeater.get("repeater_number") == "1":
					Repeater.set("repeater_angle", "30")
				Repeater.set("repeater_number", str(round(int(Repeater.get("repeater_number")) * 3)))
		except:
			pass
	return Tree