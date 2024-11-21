# Instrucciones 
Para ejecutar los programas primero es necesario crear un cluster HDFS y subir los archivos de datos.
## Prerequisitos:
- Hadoop (versión 3.3 o superior)
- Apache Spark (versión comparible con Spark 3.3 o superior, para desarrolló se uso Spark 3.4.4)
- Configurar Spark para integrarlo con Hadoop

## Instrucciones:
1. Clonar el respositorio:
   ```
   git clone https://github.com/francoAgustin2023/tpFinalBaseDatos2.git
   ```
3. Descargar las dependencias de Python necesarias:
   ```
   pip install -r requirements.txt
   ```
5. Crear un directorio en HDFS:

   ```
   hdfs dfs -mkdir /datos
   ```

4. Copiar los archivos de datos dentro del directorio:
   ```
   hdfs dfs -put <ruta-al-proyecto>/data_files libro.txt /datos
   ```
   ```
   hdfs dfs -put <ruta-al-proyecto>/data_files pilotos.csv /datos
   ```

5. Ejecutar el programa deseado. 
   
   a. Programa simple que procesa datos distribuidos usando como base el libro en txt: 
   
   ```
   spark-submit programa.py
   ```
   b. Programa que trabaja con operaciones básicas como map, filter y reduce. Usa tambien el libro:

   ```
   spark-submit operacionesBasicas.py
   ```
   c. Programa que realiza un análisis simple de un conjunto de datos de muestra. Usa un CCV con datos de Fórmula 1

   ```
   spark-submit race_results_analysis.py
   ```
   Se creara un archivo dentro de /formula1 llamado resultado_pilotos.csv.
6. Utilizar la consola interactiva de pyspark para verificar los resultados.


