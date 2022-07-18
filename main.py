from Parser import NatalyParser
from Parser import TDElenaParser
from repository import Repository
import Parser.Config.NatalyConfig as ConfigNataly

if __name__ == '__main__':
    # Nataly
    TDElena_parser = TDElenaParser.Parser_TDElena()
    TDElena_parser.run_women_parsing(ConfigNataly.articles_td_elena_women)

    Nataly_parser = NatalyParser.Parser_Nataly()
    Nataly_parser.run_women_parsing()

    repo_nataly_women = Repository(TDElena_parser.result_tdelena_women, Nataly_parser.result_nataly_women,
                                   ConfigNataly.women_articles.TD_Elena,
                                   ConfigNataly.women_articles.Nataly
                                   )
    repo_nataly_women.run()

