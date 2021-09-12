import subprocess

# Search for the wacom tablet ID, grab and store that ID in the pad_ID variable

wacom_pad = subprocess.run(["xsetwacom", "--list", "devices"], capture_output=True, text=True)

PAD = subprocess.run(["grep", "PAD"], capture_output=True, text=True, input=wacom_pad.stdout)

pad_ID = subprocess.run(["awk", "{print $7}"], capture_output=True, text=True, input=PAD.stdout)

pad_ID = int(pad_ID.stdout)

# Set the command with the correct pad_ID and preffered shortcut

write_draw = f'xsetwacom --set {pad_ID} button 1 \"key super alt D\"'

write_erase = f'xsetwacom --set {pad_ID} button 2 \"key super alt E\"'

write_undo = f'xsetwacom --set {pad_ID} button 3 \"key ctrl Z\"'

write_rect = f'xsetwacom --set {pad_ID} button 8 \"key ctrl R\"'

# Run the above command to map buttons 

draw = subprocess.run(args=write_draw, shell=True, text=True)

erase = subprocess.run(args=write_erase, shell=True, text=True)

undo = subprocess.run(args=write_undo, shell=True, text=True)

rect = subprocess.run(args=write_rect, shell=True, text=True)
