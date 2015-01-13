#!/usr/bin/env python

from pysnap import Snapchat
import secrets

s = Snapchat()
s.login(secrets.USERNAME, secrets.PASSWORD)

friends_to_add = [friend['name'] for friend in s.get_updates()['added_friends'] if friend['type'] == 1]
for friend in friends_to_add:
    s.add_friend(friend)

snaps = [snap['id'] for snap in s.get_snaps() if snap['status'] == 1 and snap['media_type'] == 0]
for snap in snaps:
    with open('tmp.jpg', 'wb') as f:
        f.write(s.get_blob(snap))
    media_id = s.upload('tmp.jpg')
    s.post_story(media_id, 5)
    s.mark_viewed(snap)
