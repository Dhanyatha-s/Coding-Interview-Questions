class PasswordSecurity:
    def __init__(self, PWT):
        self.PWT = PWT

    def min_flips_to_secure(self):
        flips = 0

        # Process the string in pairs
        for i in range(0, len(self.PWT) - 1, 2):
            if self.PWT[i] != self.PWT[i + 1]:
                flips += 1

        return flips

# Example usage:
password = "011001"
security = PasswordSecurity(password)
print(security.min_flips_to_secure())  # Output: 3
