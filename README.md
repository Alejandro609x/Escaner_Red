## 📦 Nombre del proyecto: `escaner_red.py`

### 🔍 Descripción:

**`escaner_red.py`** es un script de análisis de red en Python diseñado para resolver todas las IPs asociadas a una URL (públicas y privadas), clasificarlas, verificar su conectividad por **ping** y **puerto 443 (HTTPS)**, y ofrecer un reporte detallado.

Es ideal para administradores de red, pentesters o desarrolladores que necesiten inspeccionar el comportamiento de resolución DNS y accesibilidad desde redes internas o externas.

---

### ⚙️ Características principales:

* 🔎 Extrae el dominio desde cualquier URL.
* 🌐 Resuelve IPs internas (DNS local) y públicas (via `dig` con DNS 8.8.8.8).
* 📡 Clasifica cada IP: **Clase A/B/C**, **Pública/Privada**.
* ✅ Verifica conectividad por **ping** y **HTTPS (puerto 443)**.
* 📁 Permite guardar los resultados en un archivo (`.txt`).
* 🧠 Modo interactivo y modo automático (`-a`).
* 🆘 Ayuda integrada (`-h`) con ejemplos de uso.

---

### 💻 Requisitos:

* Python 3.6+
* Tener instalado `dig` (presente en la mayoría de distros Linux)
* (Opcional) Instalar `dnspython` si deseas usar DNS via código (no necesario con dig)

---

### 🚀 Uso:

```bash
# Modo interactivo
python escaner_red.py

# Modo automático con URL
python escaner_red.py https://ejemplo.com -a

# Guardar resultado en archivo
python escaner_red.py https://ejemplo.com -a -Og resultado.txt
```

---

### 📜 Licencia:

MIT License — libre para usar, modificar y distribuir.

---
