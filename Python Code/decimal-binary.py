class decimalToBinary:
    def __init__(self, decimal_number):
        self.decimal_number = decimal_number

    def convert(self):
         if self.decimal_number == 0:
             return "0"
         binary_number = ""
         number = self.decimal_number

         while number >0:
             reminder = number % 2
             binary_number += str(reminder)
             number //= 2

        return binary_number

decimal_number = 10
conversion = decimalToBinary(decimal_number)
result = conversion.convert()
print(f"Decimal number{decimal_number} in binary is {result}")


# class DecimalToBinaryConverter:
#     def __init__(self, decimal_number):
#         self.decimal_number = decimal_number

#     def convert_to_binary(self):
#         if self.decimal_number == 0:
#             return "0"
#         binary_number = ""
#         number = self.decimal_number
        
#         while number > 0:
#             remainder = number % 2
#             binary_number = str(remainder) + binary_number
#             number = number // 2
        
#         return binary_number

# # Example usage
# decimal_number = 10
# converter = DecimalToBinaryConverter(decimal_number)
# binary_result = converter.convert_to_binary()
# print(f"Binary representation of {decimal_number} is {binary_result}")
