# 📘 Manual de uso: `escaner_red.py`

---

## 🧠 ¿Qué hace este script?

`escaner_red.py` es una herramienta que te permite analizar una página web y obtener toda la información relacionada con sus direcciones IP. Detecta tanto IPs **internas** (de red local) como **externas** (públicas), te dice si están activas, si son accesibles por internet y qué tipo de red usan.

---

## 🎯 ¿Para qué sirve?

* Ver si una página web está funcionando desde dentro y fuera de tu red.
* Detectar si una IP es pública o privada.
* Saber si un servidor responde a **ping** o a conexiones seguras por **HTTPS (puerto 443)**.
* Comprobar accesibilidad de sitios internos o gubernamentales.

---

## ✅ Requisitos antes de usar

1. Tener **Python 3** instalado. Puedes verificarlo escribiendo:

   ```bash
   python3 --version
   ```

2. Tener instalado `dig`. En la mayoría de sistemas Linux ya viene instalado. Si no, lo puedes instalar así:

   * En Ubuntu/Debian:

     ```bash
     sudo apt install dnsutils
     ```
   * En Fedora:

     ```bash
     sudo dnf install bind-utils
     ```
   * En Arch:

     ```bash
     sudo pacman -S bind
     ```

3. Guarda el archivo `escaner_red.py` en tu computadora, por ejemplo en tu Escritorio.

---

## 🚀 Cómo usarlo

### 📍 Opción 1: Modo interactivo (recomendado para principiantes)

```bash
python3 escaner_red.py
```

Verás un mensaje como este:

```bash
Introduce la URL (ej: https://ejemplo.com/login):
```

Aquí debes pegar la dirección completa de la página que quieres analizar. Por ejemplo:

```
https://innovacion.finanzas.cdmx.gob.mx/sinpapel/
```

El programa te mostrará una lista de todas las IPs asociadas, y te dirá:

* Si son públicas o privadas.
* Si responden a `ping`.
* Si aceptan conexiones por el puerto 443 (HTTPS).
* Si son internas o externas.

---

### 📍 Opción 2: Modo automático (sin preguntas)

Si ya sabes la URL, puedes ejecutarlo directamente así:

```bash
python3 escaner_red.py https://ejemplo.com -a
```

---

### 📍 Opción 3: Guardar resultados en archivo de texto

Puedes guardar la salida en un archivo `.txt` así:

```bash
python3 escaner_red.py https://ejemplo.com -a -Og resultados.txt
```

El archivo `resultados.txt` se creará en el mismo directorio.

---

## ❓ Preguntas frecuentes

### 🔸 ¿Por qué me da una IP privada?

Porque estás dentro de una red privada (como una empresa o gobierno). Algunas páginas internas sólo se ven desde adentro.

### 🔸 ¿Por qué algunas IPs dicen “Conectividad: Ninguna”?

Eso significa que el servidor no respondió ni a ping ni al puerto 443 (posiblemente están bloqueados por firewall).

### 🔸 ¿Puedo usar esto en Windows?

Sí, si tienes Python y dig instalados, también funcionará.

---

## 🛠 Recomendaciones

* Si vas a compartir los resultados, usa la opción `-Og` para guardar el informe.
* Úsalo en redes donde tengas permiso de análisis.
* Si alguna IP no responde, no significa que no esté en uso, sólo que no responde a ping o HTTPS.

---
