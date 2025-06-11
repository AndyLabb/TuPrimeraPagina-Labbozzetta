# TuPrimeraPagina+Labbozzetta

Proyecto web desarrollado como entrega final para el curso de Django de Coderhouse.  
Este sitio simula una plataforma de gestión para una escuela de ski y snowboard, utilizando el patrón arquitectónico MVT de Django.

---

## 🚀 Descripción

Esta aplicación permite gestionar los aspectos básicos de una escuela de ski:

- Registrar y listar alumnos e instructores.
- Asignar turnos a los alumnos.
- Buscar turnos por nombre de alumno.
- Editar perfil de usuario y cargar avatar.
- Enviar mensajes al administrador de la escuela.
- Panel de administración para gestionar modelos.

El diseño utiliza herencia de plantillas y está basado en el tema **Grayscale** de StartBootstrap, adaptado con estilos propios.

---

## ✅ Funcionalidades principales

- ✅ Herencia de HTML con `base.html`.
- ✅ Tres modelos principales: `Alumno`, `Instructor`, `Turno`.
- ✅ Formularios de carga para cada modelo (`AlumnoForm`, `InstructorForm`, `TurnoForm`).
- ✅ Formulario de búsqueda de turnos por nombre de alumno.
- ✅ Registro, login, logout y perfil de usuario editable.
- ✅ Avatares personalizados por usuario.
- ✅ Sistema de mensajería (usuarios pueden dejar mensajes al administrador).
- ✅ Administración completa vía `/admin`.

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Django**
- **Bootstrap 5** 
- **HTML5 + CSS3**
- **SQLite3** 
- **CKEditor** 

---

## ⚙️ Instalación y ejecución local

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/TU_USUARIO/TuPrimeraPagina-Labbozzetta.git
   cd TuPrimeraPagina-Labbozzetta
