from Parser import NatalyParser
from Parser import TDElenaParser
from repository import Repository
import Parser.Config.NatalyConfig as ConfigNataly

if __name__ == '__main__':

    TDElena_parser = TDElenaParser.Parser_TDElena(ConfigNataly.women_articles.TD_Elena)
    TDElena_parser.run()

    Nataly_parser = NatalyParser.Parser_Nataly()
    Nataly_parser.run()

    repo_nataly = Repository(TDElena_parser.result_tdelena, Nataly_parser.result_nataly, ConfigNataly.women_articles.TD_Elena,
                      ConfigNataly.women_articles.Nataly)
    repo_nataly.run()



