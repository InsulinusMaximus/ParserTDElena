from Parser import TDElenaParser, NatalyParser, GomanyParser
from repository import Repository
from Parser.ArticlesFilter import article_filtering
import Parser.Config.NatalyConfig as ConfigNataly
import Parser.Config.GomanyConfig as ConfigGomany


class Service:

    def __init__(self):
        # Initialization of site parsing TD Elena
        self.TDElena_parser = TDElenaParser.Parser_TDElena()

        self.TDElena_parser.run_men_parsing()

        # Announcement of parsers of other companies
        self.Nataly_parser = NatalyParser.Parser_Nataly()
        self.Gomany_parser = GomanyParser.Parser_Gomany()

    # Nataly service
    def run_nataly_women_service(self):
        self.TDElena_parser.run_women_parsing(ConfigNataly.women_articles_dict.keys())
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          article_data=ConfigNataly.women_articles_dict.keys()
                          )

        self.Nataly_parser.run_women_parsing()

        repo_nataly_women = Repository(self.TDElena_parser.result_tdelena_women,
                                       self.Nataly_parser.result_nataly_women,
                                       ConfigNataly.women_articles_dict
                                       )
        repo_nataly_women.run()

    def run_nataly_men_service(self):
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          article_data=ConfigNataly.men_articles_dict.keys()
                          )

        self.Nataly_parser.run_men_parsing()

        repo_nataly_men = Repository(self.TDElena_parser.result_tdelena_men,
                                     self.Nataly_parser.result_nataly_men,
                                     ConfigNataly.men_articles_dict
                                     )
        repo_nataly_men.run()

    def run_nataly_all_service(self):
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          article_data=ConfigNataly.women_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          article_data=ConfigNataly.men_articles_dict.keys()
                          )
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

    # Gomany service
    def run_gomany_women_service(self):
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          article_data=ConfigGomany.women_articles_dict.keys()
                          )

        self.Gomany_parser.run_women_parsing()

        repo_nataly_women = Repository(self.TDElena_parser.result_tdelena_women,
                                       self.Gomany_parser.result_gomany_women,
                                       ConfigGomany.women_articles_dict
                                       )
        repo_nataly_women.run()

    def run_gomany_men_service(self):
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          article_data=ConfigGomany.men_articles_dict.keys()
                          )

        self.Gomany_parser.run_men_parsing()

        repo_nataly_men = Repository(self.TDElena_parser.result_tdelena_men,
                                     self.Gomany_parser.result_gomany_men,
                                     ConfigGomany.men_articles_dict
                                     )
        repo_nataly_men.run()

    def run_gomany_all_service(self):
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          article_data=ConfigGomany.women_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          article_data=ConfigGomany.men_articles_dict.keys()
                          )

        self.Gomany_parser.run_women_parsing()
        self.Gomany_parser.run_men_parsing()

        overall_result_td_elena = self.TDElena_parser.result_tdelena_women + self.TDElena_parser.result_tdelena_men
        overall_result_gomany = self.Gomany_parser.result_gomany_women + self.Gomany_parser.result_gomany_men
        overall_articles_dict = ConfigGomany.women_articles_dict | ConfigGomany.men_articles_dict

        print(overall_articles_dict)

        repo_nataly_all = Repository(overall_result_td_elena,
                                     overall_result_gomany,
                                     overall_articles_dict
                                     )
        repo_nataly_all.run()


