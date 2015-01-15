#!/usr/bin/env python

from pysnap import Snapchat
import secrets
import os

path = os.path.dirname(os.path.realpath(__file__)) + '/tmp.jpg'

s = Snapchat()
s.login(secrets.USERNAME, secrets.PASSWORD)

for friend in [friend['name'] for friend in s.get_updates()['added_friends'] if friend['type'] == 1]:
    s.add_friend(friend)

snaps = [snap for snap in s.get_snaps() if snap['status'] == 1 and snap['media_type'] == 0]
for snap in snaps:
    with open(path, 'wb') as f:
        f.write(s.get_blob(snap['id']))
    media_id = s.upload(path)
    print s.post_story(media_id, 5)
    s.mark_viewed(snap['id'])
