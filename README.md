# Dragonfly

Developed by: Team (Xue Vang)

# Distributed Web Scraper for Pokemon Data
This project demonstrates a distributed web scraper that collects Pokemon data (name, height, weight, experience, and sprite URLs) using the Ray distributed system. The data is gathered from PokeAPI (https://pokeapi.co/). 

## Prerequisites
- Google Cloud account with credits
- Python 3.11 installed on all nodes (head and workers)
- Required Packages: Ray, Requests, BeautifulSoup4

## Project Setup
1. Create Google Cloud VMs: Set up one head node and at least one worker node all within the same network and region.
    a) In my case I created several VMs in the same zone as Linux/Ubuntu and as e-2 instances
2. Firewall Configuration: Create a rule to allow for inbound traffic on port 6739 (or whatever the user wishes to set the used port for)
3. Install Dependencies: SSH into each node (I just opened them in the browser from Google Cloud) and install and run:
    a) update: sudo apt update
    b) install pip: sudo apt install python3-pip -y
    c) install python virtual environment: sudo apt install python3.11-venv
    d) set up virtual environment: python3 -m venv .
    d) activate the virtual environment: source bin/activate
    e) install depencies: pip install ray requests beautifulsoup4

## Configuration
1) Initiate Ray on head node: ray start --head --port=6379
2) For the worker nodes: ray start --address='<head-ip-address>:6379'

## Running Project
1) From the head node, run the python file: "python3 PokeAPI_Ray.py"