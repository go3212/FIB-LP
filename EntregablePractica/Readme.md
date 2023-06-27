# AChurchBot

AChurchBot es un bot de Telegram diseñado para ayudarte a entender y manipular expresiones de Cálculo Lambda. El Cálculo Lambda es un sistema formal para la lógica matemática que es fundamental para el funcionamiento de las computadoras modernas.

## Cómo se usa

Para utilizar el bot, debes mandar un mensaje a @AChurchBot con una expresión de Cálculo Lambda. El bot procesará tu expresión y te devolverá el árbol semántico correspondiente y el resultado de la evaluación de la expresión.

Aquí tienes una lista de los comandos que puedes utilizar con el bot:

- `/start`: Inicia la interacción con el bot.
- `/author`: Muestra la información del autor del bot.
- `/help`: Muestra la lista de comandos disponibles.
- `/macros`: Muestra las macros definidas en el sistema.
- Al enviar un mensaje con una expresión en Cálculo Lambda, el bot la procesará y te devolverá el resultado acompañada de unos graficos.

## Requisitos

Para poder utilizar el bot, necesitarás tener instalado Python 3.7 o superior, así como las siguientes librerías de Python:

- `antlr4-python3-runtime`
- `python-telegram-bot`
- `pydot`
- `dataclasses`
- `uuid`
- `types`

Puedes instalar estas librerías utilizando el siguiente comando:

```sh
pip install antlr4-python3-runtime python-telegram-bot pydot dataclasses uuid types
```

Es posible que necesites generar los ficheros de antlr, lo puedes hacer con el siguiente comando, la version de antlr recomendada es la 4.13.0
```sh
antlr4 -Dlanguage=Python3 -visitor LambdaCalculus.g4
```

## Arquitectura del programa

El bot utiliza una gramática definida en ANTLR4 para generar el árbol semántico correspondiente a las expresiones de Cálculo Lambda enviadas por los usuarios.

El bot procesa las expresiones utilizando una serie de visitantes, que recorren el árbol generado por ANTLR4 y crean el árbol semántico correspondiente. También utiliza un evaluador que realiza reducciones beta y alfa en las expresiones para simplificarlas.

Las funciones del bot están divididas en varias clases y funciones de Python. La clase `MyVisitor` se utiliza para crear el árbol semántico, mientras que la función `process` toma una cadena de texto que representa una expresión y devuelve el árbol semántico correspondiente.

La clase `Evaluator` se utiliza para evaluar las expresiones, realizando reducciones beta y alfa cuando es posible. Esta clase también contiene métodos para determinar si una variable ocurre en una expresión, obtener todas las variables en una expresión y sustituir una variable por otra en una expresión.

Finalmente, el bot utiliza la librería `python-telegram-bot` para interactuar con los usuarios a través de la plataforma de mensajería de Telegram. Las interacciones del bot con los usuarios están controladas por la función `telegram_bot`, que toma como entrada el token de un bot de Telegram y utiliza varias funciones de manejo de comandos para responder a los comandos y mensajes de los usuarios.

En resumen, el AChurchBot es una herramienta educativa diseñada para ayudar a los usuarios a entender y trabajar con el Cálculo Lambda, un concepto fundamental en la informática y las matemáticas.