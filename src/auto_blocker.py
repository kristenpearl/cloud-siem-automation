import time

THRESHOLD = 5

def block_ip(ip_address):
    print(f"\n[URGENT INCIDENT RESPONSE] ALERT TRIGGERED.")
    print(f"[+] Source IP '{ip_address}' exceeded {THRESHOLD} authentication failures.")
    print(f"[+] ACTION: Executed network isolation policy for {ip_address}. Traffic dropped.")

def monitor_and_remediate():
    print("[*] SOAR Automation Service Listening for SIEM Detection Triggers...")
    already_blocked = set()

    while True:
        try:
            with open("src/auth.log", "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            time.sleep(2)
            continue

        failures = {}
        for line in lines[-50:]:
            if "Failed password" in line:
                try:
                    parts = line.split("from ")
                    ip = parts[1].split(" ")[0]
                    failures[ip] = failures.get(ip, 0) + 1
                except IndexError:
                    continue

        for ip, count in failures.items():
            if count >= THRESHOLD and ip not in already_blocked:
                block_ip(ip)
                already_blocked.add(ip)

        time.sleep(2)

if __name__ == "__main__":
    monitor_and_remediate()
