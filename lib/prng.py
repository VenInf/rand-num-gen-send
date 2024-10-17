
class PRNG():
    def __init__( self,
                  upper_bound = 2147483647,
                  X = 31415926535,
                  Y = 89793238462,
                  Z = 64338327950,
                  W = 28841971693
                ):

        self.upper_bound = upper_bound

        self.X = X % self.upper_bound
        self.Y = Y % self.upper_bound
        self.Z = Z % self.upper_bound
        self.W = W % self.upper_bound


    def xor_shift(self):
        t = self.W

        s = self.X
        self.W = self.Z
        self.Z = self.Y
        self.Y = self.X

        t ^= (t << 11) % self.upper_bound
        t ^= (t >> 8) % self.upper_bound
        self.X = (t ^ s ^ (s >> 19)) % self.upper_bound

        return self.W

    def get_random(self):
        self.xor_shift()
        return self.W

