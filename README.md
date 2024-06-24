## AMBER-B1-Robotic-Arm_V2
Important: Please read our [Quick Start Guide] in advance if you're new to AMBER Robotic Arm(https://github.com/MrAsana/AMBER_B1_Robotic_Arm_V2/blob/main/Robotic%20Arm%20Hardware%20Quickstart%20%26%20Robot%20Studio%20Manual%20V0.0.11.pdf) 

Important: Please reset the robotic arm to the initial position before it's powered on.
![Initial positon](https://raw.githubusercontent.com/MrAsana/AMBER_B1_Robotic_Arm_V2/main/initial-position.png)

##Faq

** How to re-enable mini-hub working with the robotic if you pull out the Mini-Hub wires from the Master Control Unit?

For the version before 05/01/2024, please update the initCAN.sh by the link first，https://github.com/MrAsana/AMBER_B1_Robotic_Arm_V2/blob/main/scripts/initCAN.sh. 

Step 1, Terminal the backend service as below.

`sudo killall wave waved `

Step 2, Run Minihub initizing script.

For 6-axis AMBER C1 model, 

`cd /home/amber/amber_core_6`

For 7-axis L1/B1 model,

`cd /home/amber/amber_core_7`

And then
*Make sure you have download and update the initCAN.sh script, that's located at /home/amber.

`bash initCAN.sh`

Step 3 Launch Core Control System

`nohup ./amber_core >core.log 2>&1 &`

## AMBER Robotic ARM API based on UDP Protocol
https://github.com/MrAsana/UDP-Protocol-API 
