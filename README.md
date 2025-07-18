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

### ⚙️ Descarga

## 🟢 Opción 1: Descargar el archivo directamente (para principiantes)

1. Abre este enlace en tu navegador:
   👉 [https://github.com/Alejandro609x/Escaner\_Red](https://github.com/Alejandro609x/Escaner_Red)

2. Haz clic en el archivo `escaner_red.py`.

3. Luego haz clic en el botón **“Raw”** (arriba a la derecha del código).

4. Presiona clic derecho y elige **“Guardar como…”**.

5. Guarda el archivo con el nombre `escaner_red.py` en tu computadora.

---

## 🟡 Opción 2: Descargar el repositorio completo como ZIP

1. Entra a:
   👉 [https://github.com/Alejandro609x/Escaner\_Red](https://github.com/Alejandro609x/Escaner_Red)

2. Haz clic en el botón verde **“Code”** y selecciona **“Download ZIP”**.

3. Extrae el archivo `.zip` en tu computadora.

4. El script estará en la carpeta descomprimida con el nombre `escaner_red.py`.

---

## 🔵 Opción 3: Descargar con `wget` desde la terminal (Linux/macOS)

Puedes descargarlo desde la línea de comandos así:

```bash
wget https://raw.githubusercontent.com/Alejandro609x/Escaner_Red/main/escaner_red.py
```

Esto guardará el archivo en tu carpeta actual como `escaner_red.py`.

---

## 🔴 Opción 4: Clonar el repositorio

```bash
git clone https://github.com/Alejandro609x/Escaner_Red.git
cd Escaner_Red
python3 escaner_red.py
```

---
