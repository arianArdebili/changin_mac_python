import subprocess

if __name__ == "__main__":
    interface = "eth0"
    new_mac = "11:22:33:44:55:66"

    print("Shutting down interface...")
    subprocess.run(["ifconfig", interface, "down"])

    print("Changing MAC address...")
    subprocess.run(["macchanger", "-m", new_mac, interface])

    print("Turning the interface back on...")
    subprocess.run(["ifconfig", interface, "up"])

    print(f"MAC address changed to {new_mac}")
