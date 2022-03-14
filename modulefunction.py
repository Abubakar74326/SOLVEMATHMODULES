
# Below code return the factorial,square,cube,square root of the number.
class Mathematics:
    """this is main class whose name is mathematics"""
    def __init__(self, num):
        """
        :param num: number
        """
        self.num = num
        self.num_copy = num

    def factorial(self):
        """
        this factorial function return the factorial of a number
        :return:number
        """
        if self.num_copy != 0:
            self.num_copy -= 1
        if self.num_copy == 0:
            return 1
        else:
            return (self.num_copy + 1) * self.factorial()

    @property
    def square(self):
        """
         this function return the square of
        number that is entered in URL by user
        :return: number
        """

        return self.num * self.num

    def cube(self):
        """
        this cube function take number and return cube of number
        :return: number
        """
     return self.num * self.num * self.num

    def square_root(self):
         """
        :return:number
        """
      return self.num ** 0.5