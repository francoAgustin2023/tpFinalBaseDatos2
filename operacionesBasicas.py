from pyspark import SparkContext, SparkConf
from operator import add

conf = SparkConf().setAppName("OperacionesBasicas").setMaster("local")
sc = SparkContext(conf=conf)

file_path = "hdfs://localhost:9000/datos/libro.txt"
rdd = sc.textFile(file_path)

print("Contenido del archivo:")
print(rdd.collect())

# 1. Operación map: Dividir líneas en palabras
words = rdd.flatMap(lambda line: line.split())
print("Palabras individuales:")
print(words.collect())

# 2. Operación filter: Filtrar palabras mayores a 4 caracteres
long_words = words.filter(lambda word: len(word) > 4)
print("Palabras con más de 4 caracteres:")
print(long_words.collect())

# 3. Operación reduce: Contar la cantidad total de palabras
word_count = words.map(lambda word: 1).reduce(add)
print(f"Cantidad total de palabras en el archivo: {word_count}")

sc.stop()

