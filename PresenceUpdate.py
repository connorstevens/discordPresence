from pypresence import Presence, Activity
import time
import config

RPC = Presence(config.client_id)
RPC.connect()
ac = Activity(RPC, state=config.state, details=config.details, large_image=config.large_image, large_text=config.large_text)

ac.start = int(time.time())

while True:
    print('Status updated to configured options.')
    time.sleep(15)