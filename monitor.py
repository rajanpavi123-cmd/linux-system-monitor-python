import psutil

print("Linux System Monitoring Tool")

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')

print("CPU Usage:", cpu, "%")
print("Memory Usage:", memory.percent, "%")
print("Disk Usage:", disk.percent, "%")
