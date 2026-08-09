# Estructura del Proyecto

## 1. Identificadores Básicos del Paciente
- **Fecha de Nacimiento:** Necesaria para el cálculo de la edad y segmentación de tablas de referencia.
- **Sexo Biológico:** Requerido para la determinación de percentiles antropométricos.
  
## 2. Antropometría y Cribado Nutricional
### A. MUAC (Circunferencia Media del Brazo)
El MUAC se mide en milímetros (mm)

| Valor MUAC | Estado Nutricional | Decisión Quirúrgica|
|------------|--------------------|--------------------|
|<115 mm     |Desnutrición Aguda Severa | NO DEFINITIVO
|115 mm $\le$ x $<$ 125 mm| Desnutrición Moderada | Condicional (Depende del exámen de Albúmina + PCR)
|$\ge$ 115 mm (con PCR $<$ 1)| Estado Nutricional Aceptable| SI (Apto)

#### Interacción Albúmina y PCR (Inflamación)
La albúmina mide las reservas proteicas en sangre, pero se invalida en presencia de inflamación activa.
- **Condición de Validez:** La albúmina es válida si y solo si PCR $<$ $1mg/dL$.
- Si la PCR $\ge$ 1 $mg/dL$: se invalida el resultado de la albúmina por fase aguda inflamatoria.
#### Valores de Referencia para Albúmina (Cuando PCR < 1):
|Edad|$g/dL$ esperados|
|-|-|
| $<$ 1 año| $2.5$ a $3.4g/dL$
| 1 a 4 años| $3.9$ a $5.0g/dL$
| 5 a 19 años| $4.0$ a $5.3g/dL$

Notar que si la albúmina es menor a 2.5g/dL, se trata de una alerta y por lo tanto es un NO DEFINITIVO.

