import shutil
import os 

v = "1.0.0"
while True:
   os.system("clear")
   terminal = shutil.get_terminal_size()

   print(f"""
   ░███    ░██         ░██           ░██████      ░██     ░██           ░██████  
  ░██░██   ░██         ░██          ░██   ░██   ░██ ░██   ░██          ░██   ░██ 
 ░██  ░██  ░██         ░██         ░██         ░██   ░██  ░██         ░██        
░█████████ ░██         ░██         ░██         ░█████████ ░██         ░██        
░██    ░██ ░██         ░██         ░██         ░██    ░██ ░██         ░██        
░██    ░██ ░██         ░██          ░██   ░██  ░██    ░██ ░██          ░██   ░██ 
░██    ░██ ░████████   ░████████     ░██████   ░██    ░██ ░████████     ░██████ 


V {v}

By Denis Varga made with <3 and code in Python 3.11.4

Terminal: {terminal.columns} x {terminal.lines}

""")