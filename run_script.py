import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(description='Run scripts from different countries.')
parser.add_argument('continent', type=str, help='Continent to run script from')
parser.add_argument('region', type=str, help='Region to run script from')
parser.add_argument('country', type=str, help='Country of the script to run')

args = parser.parse_args()
command = f"python {args.continent}/{args.region}/{args.country}.py"
print(f"Running command: {command}")

subprocess.run(command, shell=True)