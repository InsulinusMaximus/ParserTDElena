from Parser import NatalyParser
from Parser import config
from save import Save_Results

if __name__ == '__main__':
    parser = NatalyParser.Parser_Nataly()
    parser.run()

    for block in parser.result:
        print(block)

    save = Save_Results(parser.result)
    save.run()


