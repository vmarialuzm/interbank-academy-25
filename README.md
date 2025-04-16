# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción:

Desarrolla una aplicación de línea de comandos (CLI) que procese un archivo CSV con transacciones bancarias y genere un reporte que incluya:

- **Balance Final:**  
  Suma de los montos de las transacciones de tipo "Crédito" menos la suma de los montos de las transacciones de tipo "Débito".

- **Transacción de Mayor Monto:**  
  Identificar el ID y el monto de la transacción con el valor más alto.

- **Conteo de Transacciones:**  
  Número total de transacciones para cada tipo ("Crédito" y "Débito").

---

## Instrucciones de ejecución

1. **Clone the repository**  

```git
git clone git@github.com:vmarialuzm/interbank-academy-25.git
```
   
2. **Start the development server**

```bash
python main.py
```

---

## Enfoque y Solución

Use programación orientada a objetos, creé 2 objetos, uno de Transaction y otro Bank con sus respectivos métodos.

---

## Estructura del Proyecto
- .gitignore : Ignora ciertos archivos
- main.py : Archivo principal, donde se ubica el script y su lógica.
- data.csv : Donde está la data de transacciones bancarias.
- README.md : Breve introducción del proyecto e instrucciones de ejecución de éste.


   
