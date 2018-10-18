from pyspark import SparkConf, SparkContext

from exercises.exercise_01 import Exercise01
from exercises.exercise_02 import Exercise02

if __name__ == '__main__':
    conf = SparkConf().setAppName("Notebook").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    exercise01 = Exercise01.square_of_even(range(1, 10000), sc).collect()
    exercise02 = Exercise02.word_count("data/news.txt", sc).collect()
    print("exercise01 ===> " + str(exercise01))
    print("exercise01 ===> " + str(exercise02))

