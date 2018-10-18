class Exercise01:

    @staticmethod
    def square_of_even(numbers, sc):
        rdd = sc.parallelize(numbers) \
            .filter(lambda x: x % 2 == 0) \
            .map(lambda x: x * x)
        return rdd
