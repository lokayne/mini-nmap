# mii nmap tool
import sys
import socket

def get_inputs():
  print("===== MINI NMAP TOOL TO FIND OPEN PORTS =====")
  target = input("Enter Target IP/Domain: ").strip()
  if not target:
    print("***TARGET CANNOT BE EMPTY***")
    sys.exit(1)

  print("\nSelect Scan Type: ")
