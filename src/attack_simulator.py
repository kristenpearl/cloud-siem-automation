import time
import random
import logging

logging.basicConfig(
    filename='src/auth.log',
    level=logging.INFO,
    format='%(asctime)s localhost sshd[12345]: %(message)s',
    datefmt='%b %d %H:%M:%S'
)

ATTACKERS = ["192.168.1.50", "10.0.0.12", "172.16.5.99"]
USERNAMES = ["root", "admin", "user", "oracle", "ftpuser"]

def simulate_normal_traffic():
    ip = f"192.168.1.{random.randint(100, 200)}"
    logging.info(f"Accepted password for validuser from {ip} port 54321 ssh2")

def simulate_brute_force():
    attacker_ip = random.choice(ATTACKERS)
    target_user = random.choice(USERNAMES)
    print(f"[!] Simulating Brute-Force Attack from {attacker_ip} targeting '{target_user}'...")

    for _ in range(7):
        logging.info(f"Failed password for {target_user} from {attacker_ip} port {random.randint(40000, 60000)} ssh2")
        time.sleep(0.2)

if __name__ == "__main__":
    print("[*] Starting Security Log Generation Simulator...")
    try:
        while True:
            choice = random.choices(['normal', 'attack'], weights=[0.85, 0.15])[0]
            if choice == 'normal':
                simulate_normal_traffic()
                time.sleep(random.randint(2, 5))
            else:
                simulate_brute_force()
                time.sleep(10)
    except KeyboardInterrupt:
        print("\n[*] Simulation halted.")
