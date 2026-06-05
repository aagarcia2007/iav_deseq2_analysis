# Uso responsable de IA en el proyecto (chatgpt/pyLIA)

## Propósito del documento

Este documento describe cómo se utilizó inteligencia artificial como apoyo durante
el desarrollo del proyecto `iav_deseq2_analysis`.

La IA fue usada como herramienta de colaboración para analizar el problema,
organizar el proyecto, revisar buenas prácticas y mejorar la documentación.

No fue usada para copiar código sin entenderlo. Cada propuesta fue revisada,
probada y aceptada después de verificar que cumpliera con los requisitos del
proyecto.

## Formas en que se utilizó la IA

Durante el desarrollo del proyecto, la IA se utilizó para:

1. Analizar el problema bioinformático relacionado con resultados de DESeq2.
2. Separar el proyecto en fases pequeñas y manejables.
3. Organizar la estructura del repositorio.
4. Proponer una división del programa en funciones con responsabilidades claras.
5. Revisar el diseño antes de implementar el código.
6. Sugerir casos de prueba manuales.
7. Revisar el manejo de errores para archivos inexistentes.
8. Revisar validaciones para thresholds configurables.
9. Mejorar la claridad del README.
10. Documentar el uso responsable de IA.

## Decisiones revisadas manualmente

Antes de aceptar las propuestas, se revisó que:

- La solución coincidiera con los requisitos del proyecto.
- El código pudiera explicarse línea por línea.
- Las funciones tuvieran una sola responsabilidad.
- Los nombres siguieran estilo `snake_case`.
- Las funciones incluyeran docstrings.
- El programa funcionara con thresholds por defecto.
- El programa funcionara con thresholds personalizados.
- El programa mostrara mensajes claros ante errores.
- Los comandos documentados realmente pudieran ejecutarse.

## Buenas prácticas reforzadas con IA

| Buena práctica | Cómo se aplicó en el proyecto |
|---|---|
| Documentar antes de programar | Se crearon `context.md`, `design.md` y `test_cases.md` antes de completar el código |
| Separar responsabilidades | El programa se dividió en funciones pequeñas |
| Usar docstrings | Cada función importante fue documentada |
| Usar CLI clara | Se implementaron argumentos con `argparse` |
| Manejar errores | Se agregaron mensajes claros para archivo inexistente y thresholds inválidos |
| Probar progresivamente | Se ejecutaron pruebas manuales después de cada parte |
| Usar Git de forma ordenada | Se realizaron commits pequeños con prefijos claros |

