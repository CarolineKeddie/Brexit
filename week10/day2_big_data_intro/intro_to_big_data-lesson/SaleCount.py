from mrjob.job import MRJob
class SaleCount(MRJob):
    def mapper(self, _, line):
        if line.startswith('#'):
            return
        fields = line.split()
        state = fields[3]
        yield (state, 1)
    def reducer(self, state, count): 
        yield (state, sum(count))
if __name__ == '__main__': 
    SaleCount.run()