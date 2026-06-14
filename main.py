import time
import subprocess

from database import init_db, device_exists, add_device, update_device, delete_device, get_all_devices


def scan_network():
    result = subprocess.run(
        ["sudo", "arp-scan", "--localnet", "--plain"],
        capture_output=True,
        text=True,
    )

    lines = result.stdout.splitlines()
    devices = []

    for line in lines:
        parts = line.split()
        if len(parts) < 2:
            continue

        mac = parts[1]
        ip = parts[0]
        vendor = " ".join(parts[2:])

        devices.append({
            "mac": mac,
            "ip": ip,
            "vendor": vendor,
        })

    return devices


def sync_devices(devices):
    current_macs = {d["mac"] for d in devices}
    stored_devices = get_all_devices()

    for stored in stored_devices:
        if stored["mac"] not in current_macs:
            delete_device(stored["mac"])
            print("Appareil supprimé:", stored.get("vendor", stored["mac"]))

    new_device = False
    for d in devices:
        if device_exists(d["mac"]):
            update_device(d["mac"], d["ip"])
        else:
            add_device(d["mac"], d["ip"], d["vendor"])
            print("Nouvel appareil:", d["vendor"])
            new_device = True

    if not new_device:
        print("Aucun nouvel appareil détecté.")

    print("Appareils détectés:", len(devices))


def main():
    init_db()

    while True:
        try:
            devices = scan_network()
            sync_devices(devices)
        except Exception as err:
            print("Erreur pendant le scan:", err)

        time.sleep(300)


if __name__ == "__main__":
    main()
