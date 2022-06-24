from Parser import NatalyParser
from Parser import TDElenaParser
from save import Save_Results

if __name__ == '__main__':
        #parser = NatalyParser.Parser_Nataly()
        #parser.run()

    parser = TDElenaParser.Parser_TDElena()
    parser.run()

    # save = Save_Results(parser.parsing_result)
    # save.run()


