# SDN-Based Firewall using POX

## Problem Statement
Design and implement an SDN-based firewall using a controller (POX) and Mininet. The firewall should allow or block traffic between hosts based on predefined rules using OpenFlow.

---

## Setup / Execution Steps

### Step 1: Start POX Controller
cd pox  
./pox.py firewall  

### Step 2: Start Mininet (new terminal)
sudo mn --topo single,3 --controller remote  

---

## Expected Output

- h1 ping h2 → Blocked  
- h1 ping h3 → Allowed  
- h2 ping h3 → Blocked  

---

## Proof of Execution

### 1. Blocked Traffic
Command:
h1 ping h2  
Result: Packet loss (communication blocked)

### 2. Allowed Traffic
Command:
h1 ping h3  
Result: Successful ping

### 3. Additional Rule
Command:
h2 ping h3  
Result: Packet blocked

### 4. Controller Logs
Shows:
- BLOCKED: 10.0.0.1 → 10.0.0.2  
- ALLOWED traffic logs  

### 5. Flow Table

Command:
sudo ovs-ofctl dump-flows s1  

Output shows flow rules installed in switch.

---

## Tools Used
- Mininet  
- POX Controller  
- OpenFlow  
