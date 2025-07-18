import socket
import argparse
import ipaddress
import platform
import subprocess
import re

def obtener_dominio(url):
    if not url.startswith("http"):
        url = "http://" + url
    dominio = re.findall(r"https?://([^/]+)", url)
    return dominio[0] if dominio else None

def resolver_ips_locales(dominio):
    try:
        _, _, ip_list = socket.gethostbyname_ex(dominio)
        return list(set(ip_list))
    except socket.gaierror:
        return []

def resolver_ips_publicas_con_dig(dominio):
    try:
        resultado = subprocess.run(["dig", "+short", dominio, "@8.8.8.8"], stdout=subprocess.PIPE, text=True)
        ips = resultado.stdout.strip().split("\n")
        return [ip for ip in ips if re.match(r"\d+\.\d+\.\d+\.\d+", ip)]
    except Exception:
        return []

def explicar_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        primer_octeto = int(ip.split('.')[0])
        clase = (
            'Clase A' if primer_octeto < 128 else
            'Clase B' if primer_octeto < 192 else
            'Clase C' if primer_octeto < 224 else
            'Clase D (Multicast)' if primer_octeto < 240 else
            'Clase E (Experimental)'
        )
        tipo = 'Privada' if ip_obj.is_private else 'Pública'
        return f"Clase: {clase}, Tipo: {tipo}"
    except ValueError:
        return "IP inválida"

def verificar_conectividad_ping(ip):
    sistema = platform.system()
    comando = ["ping", "-n", "1", ip] if sistema == "Windows" else ["ping", "-c", "1", ip]
    try:
        resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return resultado.returncode == 0
    except Exception:
        return False

def verificar_conectividad_https(ip):
    try:
        with socket.create_connection((ip, 443), timeout=3):
            return True
    except Exception:
        return False

def analizar_url(url):
    salida = []
    dominio = obtener_dominio(url)
    if not dominio:
        return "❌ No se pudo extraer el dominio desde la URL.\n"

    ips_locales = resolver_ips_locales(dominio)
    ips_publicas = resolver_ips_publicas_con_dig(dominio)
    todas_ips = list(set(ips_locales + ips_publicas))

    salida.append(f"🔗 URL: {url}")
    salida.append(f"🌐 Dominio: {dominio}")
    salida.append(f"📡 IPs encontradas: {', '.join(todas_ips) if todas_ips else 'Ninguna'}")

    if not todas_ips:
        salida.append("❌ No se pudo resolver ninguna IP.")
        return "\n".join(salida)

    for ip in todas_ips:
        explicacion = explicar_ip(ip)
        origen = []
        if ip in ips_locales:
            origen.append("Interna")
        if ip in ips_publicas:
            origen.append("Pública")

        ping_ok = verificar_conectividad_ping(ip)
        https_ok = verificar_conectividad_https(ip)

        conectividad = []
        if ping_ok:
            conectividad.append("Ping")
        if https_ok:
            conectividad.append("HTTPS")
        if not conectividad:
            conectividad.append("Ninguna")

        salida.append(f" - 🧠 IP: {ip} → {explicacion}, Origen: {', '.join(origen)}, Conectividad: {', '.join(conectividad)}")

    return "\n".join(salida) + "\n"

def main():
    parser = argparse.ArgumentParser(
        description="🔍 Escáner de red para analizar URLs, obtener IPs públicas/privadas y verificar conectividad (Ping y HTTPS).",
        epilog="Ejemplo de uso: python escaner_red.py https://ejemplo.com -a -Og resultado.txt"
    )
    parser.add_argument("url", nargs="?", help="URL a analizar (ej: https://ejemplo.com)")
    parser.add_argument("-a", "--auto", action="store_true", help="Modo automático (no pregunta por entrada)")
    parser.add_argument("-Og", metavar="archivo", help="Guardar salida en archivo de texto")
    args = parser.parse_args()

    url = args.url
    if not url and not args.auto:
        url = input("Introduce la URL (ej: https://ejemplo.com/login): ").strip()

    if not url:
        print("❌ No se proporcionó una URL.")
        return

    resultado = analizar_url(url)
    print("\n" + resultado)

    if args.Og:
        try:
            with open(args.Og, "w", encoding="utf-8") as f:
                f.write(resultado)
            print(f"💾 Resultado guardado en: {args.Og}")
        except Exception as e:
            print(f"❌ Error al guardar archivo: {e}")

if __name__ == "__main__":
    main()
