class Exercise02:

    @staticmethod
    def word_count(file_path, sc):
        rdd = sc.textFile(file_path) \
            .flatMap(lambda x: x.split(" ")) \
            .map(lambda x: (x, 1)) \
            .reduceByKey(lambda x, y: x + y)
        return rdd
