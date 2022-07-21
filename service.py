from Parser import TDElenaParser
from Parser import NatalyParser
from repository import Repository
import Parser.Config.NatalyConfig as ConfigNataly


class Service:

    def __init__(self):
        self.TDElena_parser = TDElenaParser.Parser_TDElena()
        self.Nataly_parser = NatalyParser.Parser_Nataly()

    def run_nataly_women_service(self):
        self.TDElena_parser.run_women_parsing(ConfigNataly.articles_td_elena_women)
        self.Nataly_parser.run_women_parsing()

        repo_nataly_women = Repository(self.TDElena_parser.result_tdelena_women,
                                       self.Nataly_parser.result_nataly_women,
                                       ConfigNataly.women_articles.TD_Elena,
                                       ConfigNataly.women_articles.Nataly
                                       )
        repo_nataly_women.run()

    def run_nataly_men_service(self):
        self.TDElena_parser.run_men_parsing(ConfigNataly.men_articles_dict.keys())
        self.Nataly_parser.run_men_parsing()

        repo_nataly_men = Repository(self.TDElena_parser.result_tdelena_men,
                                     self.Nataly_parser.result_nataly_men,
                                     ConfigNataly.men_articles_dict
                                     )
        repo_nataly_men.run()

    def run_nataly_all_service(self):
        self.TDElena_parser.run_women_parsing(ConfigNataly.articles_td_elena_women)
        self.Nataly_parser.run_women_parsing()
        self.TDElena_parser.run_men_parsing(ConfigNataly.articles_td_elena_men)
        self.Nataly_parser.run_men_parsing()

        overall_result_td_elena = self.TDElena_parser.result_tdelena_women + self.TDElena_parser.result_tdelena_men
        overall_result_nataly = self.Nataly_parser.result_nataly_women + self.Nataly_parser.result_nataly_men
        overall_articles_td_elena = ConfigNataly.women_articles.TD_Elena + ConfigNataly.men_articles.TD_Elena
        overall_articles_nataly = ConfigNataly.women_articles.Nataly + ConfigNataly.men_articles.Nataly

        print(type(overall_articles_td_elena))
        print(overall_articles_td_elena)

        repo_nataly_all = Repository(overall_result_td_elena,
                                     overall_result_nataly,
                                     overall_articles_td_elena,
                                     overall_articles_nataly
                                     )
        repo_nataly_all.run()
