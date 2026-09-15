from halo import Halo
import time

spinner = Halo(text='Loading', spinner='dots')
spinner.start()

# Run time consuming work here
time.sleep(15) #wait 15 seconds
# You can also change properties for spinner as and when you want

spinner.stop()