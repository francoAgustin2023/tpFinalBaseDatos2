from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("contadorDePalabras").setMaster("local")
sc = SparkContext(conf=conf)

file_path = "hdfs://localhost:9000/datos/libro.txt"  
rdd = sc.textFile(file_path)

palabra = "Harry"

words = rdd.flatMap(lambda line: line.split())

filtered_words = words.filter(lambda word: word == palabra)

cuenta = filtered_words.count()

print(f"La palabra '{palabra}' aparece {cuenta} veces en el archivo.")

sc.stop()

