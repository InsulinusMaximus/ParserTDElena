from parser import Parser_Nataly_Futbolki
from save import Save_Results

if __name__ == '__main__':
    parser = Parser_Nataly_Futbolki()
    parser.run()

    for block in parser.result:
        print(block)

    save = Save_Results(parser.result)
    save.run()


