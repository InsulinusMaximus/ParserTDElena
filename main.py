from Parser import NatalyParser
from save import Save_Results

if __name__ == '__main__':
    parser = NatalyParser.Parser_Nataly()
    parser.run()

    save = Save_Results(parser.result)
    save.run()


