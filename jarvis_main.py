import os
import eel

# Initialize Eel with the "www" directory
eel.init("www")

# Open Microsoft Edge in app mode pointing to the correct file
os.system('start msedge.exe --app="http://localhost:8000/jarvis.html"')

# Start the Eel web server
eel.start('jarvis.html', mode=None, host='localhost', block=True)
