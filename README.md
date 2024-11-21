# Instrucciones 
Para ejecutar los programas primero es necesario crear un cluster HDFS y subir los archivos de datos.
## Prerequisitos:
- Hadoop (versión 3.3 o superior)
- Apache Spark (versión comparible con Spark 3.3 o superior, para desarrolló se uso Spark 3.4.4)
- Configurar Spark para integrarlo con Hadoop

## Instrucciones:
1. Clonar el respositorio: `git clone https://github.com/francoAgustin2023/tpFinalBaseDatos2.git`
2. Descargar las dependencias de Python necesarias: `pip install -r requirements.txt`
3. Crear un directorio en HDFS:
```
hdfs dfs -mkdir /formula1
```
4. Copiar los archivos de datos dentro del direcorio:
```
hdfs dfs -put <ruta-al-proyecto>/datafile/pilotos.csv /formula1
```
5. Ejecutar el programa. Se creara un archivo dentro de /formula1 llamado resultado_pilotos.csv.
```
spark-submit --master yarn race_results_analysis.py
```
6. Utilizar la consola interactiva de pyspark para verificar los resultados.


