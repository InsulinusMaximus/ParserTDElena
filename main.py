from Parser import NatalyParser
from Parser import TDElenaParser
from save import Save_Results

if __name__ == '__main__':
    TDElena_parser = TDElenaParser.Parser_TDElena()
    TDElena_parser.run()

    #Nataly_parser = NatalyParser.Parser_Nataly()
    #Nataly_parser.run()



    save = Save_Results(TDElena_parser.result)
    save.run()


