import socket

def port_scan(target):
    print("=" * 40)
    print(f"Taranan hedef: {target}")
    print("=" * 40)

    open_ports = []

    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        result = s.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)
            print(f"[+] Port {port} açık")
        s.close()

    print("\nTarama tamamlandı!")
    if open_ports:
        print(f"Açık portlar: {open_ports}")
    else:
        print("Hiç açık port bulunamadı.")

# Kullanıcıdan hedef IP al ve fonksiyonu çalıştır
if __name__ == "__main__":
    target_ip = input("Hedef IP gir: ")
    port_scan(target_ip)