from snapchat import Snapchat
import secrets

s = Snapchat()
s.login(USERNAME, PASSWORD)

snaps = s.get_snaps()
for snap in snaps:
	print snap