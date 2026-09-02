# 🩺 Calculadora de Índice de Masa Corporal (IMC)

Aplicación web desarrollada para calcular el **Índice de Masa Corporal (IMC)** de una persona a partir de su peso y altura.

El objetivo del proyecto es crear una herramienta sencilla, intuitiva y accesible que permita a los usuarios conocer su clasificación según su IMC, teniendo en cuenta que este indicador es una referencia general y no sustituye una evaluación médica profesional.

---

## 📌 Características

- ✅ Cálculo del Índice de Masa Corporal.
- ✅ Conversión entre diferentes unidades de medida:
  - Peso:
    - Kilogramos (kg)
    - Libras (lb)
  - Altura:
    - Centímetros (cm)
    - Metros (m)
    - Sistema imperial (pies/pulgadas) *(próximamente)*
- ✅ Clasificación del resultado:
  - Bajo peso
  - Peso saludable
  - Sobrepeso
  - Obesidad
- ✅ Diseño responsive adaptado a dispositivos móviles y escritorio.
- ✅ Validación de datos introducidos por el usuario.
- ✅ Interfaz limpia orientada a una buena experiencia de usuario.

---

# 🖥️ Vista previa

*(Añadir aquí capturas de pantalla del proyecto terminado)*

---

# 🛠️ Tecnologías utilizadas

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- Python
- Flask

## Herramientas

- Git
- GitHub
- Visual Studio Code

---

# 📐 Funcionamiento

El cálculo del IMC se realiza mediante la fórmula:


```
IMC = peso (kg) / altura² (m)
```


Ejemplo:

Una persona con:

```
Peso: 70 kg
Altura: 1.75 m
```

Obtiene:

```
IMC = 70 / (1.75²)

IMC = 22.86
```


El resultado se clasifica según los valores establecidos por la Organización Mundial de la Salud (OMS).

---

# 📂 Estructura del proyecto

```
IMC-App/

│
├── app.py                 # Aplicación principal Flask
│
├── requirements.txt       # Dependencias del proyecto
│
├── templates/
│   └── index.html         # Interfaz principal
│
├── static/
│   │
│   ├── css/
│   │   └── style.css      # Estilos de la aplicación
│   │
│   └── js/
│       └── script.js      # Lógica del frontend
│
└── README.md
```

---

# ⚙️ Instalación y ejecución

## 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/IMC-App.git
```

Entrar al directorio:

```bash
cd IMC-App
```

---

## 2. Crear un entorno virtual

Linux / macOS:

```bash
python3 -m venv venv
```

Windows:

```bash
python -m venv venv
```

Activar entorno virtual:

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Ejecutar la aplicación

```bash
python app.py
```

La aplicación estará disponible en:

```
http://127.0.0.1:5000
```

---

# 🔄 Flujo de la aplicación

1. El usuario introduce su peso y altura.
2. Selecciona las unidades correspondientes.
3. El sistema convierte los valores al sistema métrico estándar.
4. Flask procesa los datos.
5. Se calcula el IMC.
6. Se muestra el resultado y la clasificación correspondiente.

---

# 🧮 Clasificación del IMC

| IMC | Clasificación |
|---|---|
| Menor de 18.5 | Bajo peso |
| 18.5 - 24.9 | Peso saludable |
| 25 - 29.9 | Sobrepeso |
| Mayor o igual a 30 | Obesidad |

---

# 🚀 Próximas mejoras

- [ ] Apartado de cálculo de peso ideal.
- [ ] Historial de cálculos realizados.
- [ ] Creación de perfiles de usuario.
- [ ] Gráficos de evolución del peso.
- [ ] Modo oscuro.
- [ ] API REST para consumir los cálculos desde otras aplicaciones.
- [ ] Base de datos para almacenamiento de información.

---

# 🎯 Objetivo del proyecto

Este proyecto forma parte de mi aprendizaje en desarrollo web utilizando Python y Flask.

El propósito es aplicar conceptos como:

- Desarrollo frontend.
- Creación de APIs y rutas con Flask.
- Manejo y validación de datos.
- Diseño responsive.
- Organización profesional de proyectos.

---

# ⚠️ Aviso médico

El Índice de Masa Corporal es una herramienta orientativa utilizada para evaluar la relación entre peso y altura.

No tiene en cuenta factores como:

- Masa muscular.
- Distribución de grasa corporal.
- Edad.
- Sexo.
- Condiciones médicas.

Para una evaluación completa se recomienda consultar con un profesional de la salud.

---

# 👨‍💻 Autor

**Yan Carlos**

Proyecto desarrollado con fines educativos y de aprendizaje.
