# README
- Programa: Compras en cafetería
- Creado por: Ghina Alexandra Garcés Rojas
- Materia: Herramientas de computación
- Fecha: 11/28/2021

Una cafetería que atiende a profesores y estudiantes ofrece diferentes descuentos a cada grupo. El programa debe obtener el número de cédula de quién va a comprar, los productos a comprar y calcular el precio aplicando el descuento adecuado. Finalmente, debe 

## Especificación del programa
- **Input:** Un rol (int) y un arreglo de productos con sus codigos y precios
- **Output:** El recibo con los items comprados y el valor con el descuento aplicado

## Modelo computacional
Este programa se implementó usando programación funcional (basado en funciones). Debido a la sencillez de los requerimientos, se usaron estructuras de datos básicos como listas para mantener registro de la información.

## Implementación
- **Productos:** Los productos se guardan en un arreglo global 2D en el que se guarda el nombre y el precio de cada producto y el código equivale a su índice dentro del arreglo mayor. De esta manera podemos acceder fácilmente a la información relacionada con cada producto y permite hacer cambios de manera sencilla. 
- **Roles**: Los roles también se guardan en un arreglo global que permite acceder a la información de cada rol, junto con su porcentaje de descuento, de manera sencilla.

La información de cada compra se guarda en variables y arreglo locales. Se obtiene la cedula y el rol de la persona que está comprando para usar en el recibo y sacar el porcentaje de descuento. 

Posteriormente, se realiza un ciclo para tomar cuantos productos la persona quiera comprar con su cantidad correspondiente. Estos se guardan en un arreglo para al final calcular el costo de cada item y el costo total de la compra.

Ya con esta información, usamos prints para imprimir en consola lo que sería el recibo de compra de la persona donde se especifica los items que compro, el precio individual y el precio total a pagar.

