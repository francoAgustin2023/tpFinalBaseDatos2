from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, bround

spark = SparkSession.builder \
    .appName("Race results analysis") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") \
    .getOrCreate()

# Leer el archivo desde HDFS
hdfs_path = "hdfs://localhost:9000/formula1/pilotos.csv" 
df = spark.read.csv(hdfs_path, header=True, inferSchema=True)

# Castear Pos a entero
df = df.withColumn("Pos", col("Pos").cast("int"))
df = df.filter(col("Driver").isNotNull() & col("Pos").isNotNull() & col("year").isNotNull())

# Filtrar temporadas del 2010 al 2023 (sistema de puntación actual excluyendo 2024 pq todavía no se define)
df = df.filter((col("year") >= 2010) & (col("year") <= 2023))

# Contar total de campeonatos por piloto
total_campeonatos = df.groupBy("Driver").agg(count("*").alias("total_campeonatos"))

# Filtrar top 3 y contar las temporadas en top 3 por piloto
campeonatos_top3 = df.filter(col("Pos") <= 3).groupBy("Driver").agg(
    count("*").alias("campeonatos_top3"),
    bround(avg("PTS"), 2).alias("promedio_pts_top3")
)

# Combinar ambos resultados y filtra unicamente a los pilotos que estuvieron en el top 3
resultado = total_campeonatos.join(campeonatos_top3, "Driver", "left").fillna(0)
resultado = resultado.filter(col("campeonatos_top3") > 0)

# Guardar el resultado en un archivo CSV en HDFS
output_path = "hdfs://localhost:9000/formula1/resultado_pilotos.csv"
resultado.write.option("header", "true").csv(output_path)

spark.stop()