<div align="center">

# Instituto Politécnico Nacional

## Escuela Superior de Cómputo

<br><br><br><br>

# Copiloto Inteligente para Troubleshooting y Análisis de Causa Raíz en Redes 5G

<br><br><br><br><br>

### Estudiante

Emilio García Lopez

### Grupo

7BV1

<br><br><br><br><br>

**Unidad de Aprendizaje:** Temas Selectos de Inteligencia Artificial  

**Fecha de entrega:** 07 de septiembre de 2026

</div>

## Objetivo

Diseñar e implementar un copiloto inteligente para asistir a ingenieros de
telecomunicaciones durante actividades de troubleshooting y análisis de causa
raíz en redes 5G, mediante recuperación de conocimiento técnico, análisis
asistido por modelos de lenguaje y ejecución controlada de herramientas.

El sistema buscará reducir el esfuerzo requerido para localizar, interpretar
y relacionar información técnica durante el diagnóstico de incidentes,
manteniendo al ingeniero como responsable de las decisiones operacionales.

## Estado Actual

Durante actividades de troubleshooting y análisis de causa raíz en
telecomunicaciones, los ingenieros deben consultar manualmente múltiples
fuentes de información, incluyendo documentación técnica, procedimientos,
logs, alarmas, especificaciones y reportes históricos.

La información necesaria para analizar un incidente puede encontrarse
distribuida entre diferentes fuentes y formatos. Como consecuencia, parte
del tiempo de diagnóstico se consume buscando, leyendo, relacionando y
validando información antes de poder establecer una hipótesis sobre la
causa raíz del problema.

## Estado Ideal

Los ingenieros deberán disponer de un sistema capaz de acceder de manera
centralizada al conocimiento técnico relacionado con un incidente y
recuperar automáticamente la información relevante de acuerdo con su
contexto.

El sistema deberá asistir al ingeniero durante el análisis, proporcionar
evidencia verificable, generar hipótesis y documentación técnica, y apoyar
la ejecución controlada de tareas de diagnóstico.

Las decisiones críticas continuarán bajo supervisión del ingeniero,
manteniendo un esquema Human-in-the-Loop.

## Propuesta de Solución

Se propone desarrollar un copiloto inteligente para ingeniería de
telecomunicaciones basado en una arquitectura compuesta por:

- una base de conocimiento centralizada;
- mecanismos de ingestión y procesamiento de documentación, logs y casos históricos;
- Retrieval-Augmented Generation (RAG);
- un Large Language Model (LLM) para razonamiento y generación;
- un agente encargado de seleccionar y utilizar herramientas;
- ejecución controlada de scripts y herramientas de diagnóstico;
- generación de reportes técnicos;
- trazabilidad de fuentes, acciones y errores;
- supervisión humana para acciones críticas.

### Knowledge Base

Centralizará documentación técnica, estándares, procedimientos,
logs e incidentes históricos.

### RAG

Recuperará evidencia relevante de acuerdo con el contexto del incidente
antes de proporcionar información al modelo.

### LLM

Interpretará el incidente y la evidencia recuperada para generar
explicaciones, hipótesis y documentación técnica.

### Agent

Seleccionará las herramientas necesarias para realizar tareas de
diagnóstico, búsqueda o procesamiento.

### Human-in-the-Loop

El ingeniero deberá revisar y aprobar decisiones o acciones que puedan
afectar infraestructura operacional.

## MVP

La primera versión del sistema validará el flujo principal:

Incident  
    ↓  
Knowledge Retrieval  
    ↓  
RAG  
    ↓  
LLM Analysis  
    ↓  
Root Cause Hypothesis  
    ↓  
Evidence  
    ↓  
Engineer Validation  

El MVP será evaluado utilizando incidentes históricos con causa raíz conocida.

El objetivo inicial será comprobar que el sistema puede:

- recuperar documentación y evidencia relevante para un incidente;
- generar una hipótesis de causa raíz sustentada en las fuentes recuperadas;
- proporcionar trazabilidad de la información utilizada;
- asistir al ingeniero sin ejecutar acciones críticas de forma autónoma.

Los resultados serán comparados contra la información y resolución histórica
del incidente.

## Resultados Esperados

Se espera obtener un prototipo funcional capaz de asistir en escenarios
controlados de troubleshooting 5G mediante recuperación contextual de
información técnica y generación de análisis sustentados en evidencia.

El proyecto permitirá evaluar:

- relevancia de la información recuperada;
- calidad y trazabilidad de las respuestas generadas;
- precisión de las hipótesis de causa raíz;
- tiempo requerido para recuperar información y producir un análisis;
- consumo de recursos computacionales;
- comportamiento del agente durante la utilización de herramientas.

Los resultados obtenidos durante el MVP determinarán la viabilidad de
extender posteriormente el sistema hacia escenarios más complejos,
integraciones adicionales y capacidades de automatización controlada.