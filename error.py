import subprocess
with open("output.txt", "wb") as f:
    subprocess.check_call(["python", "menu.py"], stdout=f)
