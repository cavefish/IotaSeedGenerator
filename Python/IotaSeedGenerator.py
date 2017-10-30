from sys import argv, exit
from random import Random


class IotaSeedGenerator(object):

    token_library = "ABCDEFGHIJKLMNOPQRSTUVXYWZ9"
    random_generator = Random()

    def get_next_token(self):
        return self.random_generator.choice(self.token_library)

    @classmethod
    def creata_seed(cls, key_size):
        generator = IotaSeedGenerator()
        return ''.join([generator.get_next_token() for _ in range(0, key_size)])


if __name__ == '__main__':
    key_size = int(argv[1]) if len(argv) > 1 else 0
    if key_size < 31 or key_size > 81:
        print("key_size must be grater than 30, lower than 82")
        exit(1)
    print(IotaSeedGenerator.creata_seed(key_size))
