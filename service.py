from Parser import TDElenaParser
from Parser import NatalyParser
from repository import Repository
import Parser.Config.NatalyConfig as ConfigNataly
from Parser.ArticlesFilter import article_filtering


class Service:

    def __init__(self):
        # Initialization of site parsing TD Elena
        self.TDElena_parser = TDElenaParser.Parser_TDElena()
        self.TDElena_parser.run_women_parsing(ConfigNataly.women_articles_dict.keys())
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          articles_data=ConfigNataly.women_articles_dict.keys()
                          )
        self.TDElena_parser.run_men_parsing()
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          articles_data=ConfigNataly.men_articles_dict.keys()
                          )

        # Announcement of parsers of other companies
        self.Nataly_parser = NatalyParser.Parser_Nataly()

    # Nataly service
    def run_nataly_women_service(self):

        self.Nataly_parser.run_women_parsing()

        repo_nataly_women = Repository(self.TDElena_parser.result_tdelena_women,
                                       self.Nataly_parser.result_nataly_women,
                                       ConfigNataly.women_articles_dict
                                       )
        repo_nataly_women.run()

    def run_nataly_men_service(self):
        self.Nataly_parser.run_men_parsing()
        repo_nataly_men = Repository(self.TDElena_parser.result_tdelena_men,
                                     self.Nataly_parser.result_nataly_men,
                                     ConfigNataly.men_articles_dict
                                     )
        repo_nataly_men.run()

    def run_nataly_all_service(self):
        self.Nataly_parser.run_women_parsing()
        self.Nataly_parser.run_men_parsing()

        overall_result_td_elena = self.TDElena_parser.result_tdelena_women + self.TDElena_parser.result_tdelena_men
        overall_result_nataly = self.Nataly_parser.result_nataly_women + self.Nataly_parser.result_nataly_men
        overall_articles_dict = ConfigNataly.women_articles_dict | ConfigNataly.men_articles_dict

        print(overall_articles_dict)

        repo_nataly_all = Repository(overall_result_td_elena,
                                     overall_result_nataly,
                                     overall_articles_dict
                                     )
        repo_nataly_all.run()
