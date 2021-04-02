class Solution:
    def reverse(self, x: int) -> int:

        my_str = str(x)
        output_str = ''
        negative = False

        if my_str[0] is '-':
            my_str = my_str[1:]
            output_str = '-' + my_str[::-1]

        else:
            output_str = my_str[::-1]

        print(output_str)

        output = int(output_str)
        if output > 2147483647 or output < -2147483648:
            return 0

        return int(output_str)
