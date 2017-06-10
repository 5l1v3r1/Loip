import subprocess
import argparse

parser = argparse.ArgumentParser(prog="loip", description="A tool to grab local network interface cards LAN Internet protocol addresses")
parser.add_argument('NIC', help='The network card\'s ip address you wish to grab')

args = parser.parse_args()

if args is None:
	subprocess.call('loip -h', shell=True)

if args.NIC:
	nic = args.NIC
	subprocess.call(('ifconfig %s | grep "inet " | awk -F " " \'{print $2}\'' % nic), shell=True)
