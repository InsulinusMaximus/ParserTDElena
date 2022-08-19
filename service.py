from dataclasses import dataclass, astuple
from typing import Any
from Parser import TDElenaParser, NatalyParser, GomanyParser
from repository import Repository
from Parser.ArticlesFilter import article_filtering
import Parser.Config.NatalyConfig as ConfigNataly
import Parser.Config.GomanyConfig as ConfigGomany


@dataclass
class general_data:
    td_elena_goods_names: Any = ''
    td_elena_articles: Any = ''
    td_elena_prices: Any = ''
    nataly_articles: Any = ''
    nataly_prices: Any = ''
    nataly_links: Any = ''
    gomany_articles: Any = ''
    gomany_prices: Any = ''
    gomany_links: Any = ''


class Service:

    def __init__(self):
        # Initialization of site parsing TD Elena
        self.TDElena_parser = TDElenaParser.Parser_TDElena()

        # Announcement of parsers of other companies
        self.Nataly_parser = NatalyParser.Parser_Nataly()
        self.Gomany_parser = GomanyParser.Parser_Gomany()

        self.repo = Repository()

    # WOMEN SERVICE

    def run_women_service(self):
        self.TDElena_parser.run_women_parsing()

        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          article_data=ConfigNataly.women_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          article_data=ConfigGomany.women_articles_dict.keys()
                          )

        self.Nataly_parser.run_women_parsing()
        self.Gomany_parser.run_women_parsing()

        general_company_women_result = self.Nataly_parser.result_nataly_women + self.Gomany_parser.result_gomany_women
        general_tdelena_women_result = self.TDElena_parser.result_tdelena_women
        overall_women_articles_dict = ConfigNataly.women_articles_dict | ConfigGomany.women_articles_dict

        final_list = []

        for tdelena_data in general_tdelena_women_result:

            final_data = general_data(tdelena_data.goods_name, tdelena_data.article, tdelena_data.price)

            list_for_values_of_the_current_item_td_elena = []

            tuple_of_company_articles = overall_women_articles_dict[tdelena_data.article]
            for company_data in general_company_women_result:
                if company_data.article in tuple_of_company_articles:
                    list_for_values_of_the_current_item_td_elena.append(company_data)

            for company in list_for_values_of_the_current_item_td_elena:
                if 'NATALY' in company.__class__.__name__:
                    final_data.nataly_articles = company.article
                    final_data.nataly_prices = company.price
                    final_data.nataly_links = company.url

                if 'GOMANY' in company.__class__.__name__:
                    final_data.gomany_articles = company.article
                    final_data.gomany_prices = company.price
                    final_data.gomany_links = company.url

            if any((final_data.nataly_articles, final_data.gomany_articles)):
                final_list.append(astuple(final_data))

        self.repo.run(final_list)

    # MEN SERVICE

    def run_men_service(self):
        self.TDElena_parser.run_men_parsing()

        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          article_data=ConfigNataly.men_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          article_data=ConfigGomany.men_articles_dict.keys()
                          )

        self.Nataly_parser.run_men_parsing()
        self.Gomany_parser.run_men_parsing()

        general_company_men_result = self.Nataly_parser.result_nataly_men + self.Gomany_parser.result_gomany_men
        general_tdelena_men_result = self.TDElena_parser.result_tdelena_men
        overall_men_articles_dict = ConfigNataly.men_articles_dict | ConfigGomany.men_articles_dict

        final_list = []

        for tdelena_data in general_tdelena_men_result:

            final_data = general_data(tdelena_data.goods_name, tdelena_data.article, tdelena_data.price)

            list_for_values_of_the_current_item_td_elena = []

            tuple_of_company_articles = overall_men_articles_dict[tdelena_data.article]
            for company_data in general_company_men_result:
                if company_data.article in tuple_of_company_articles:
                    list_for_values_of_the_current_item_td_elena.append(company_data)

            for company in list_for_values_of_the_current_item_td_elena:
                if 'NATALY' in company.__class__.__name__:
                    final_data.nataly_articles = company.article
                    final_data.nataly_prices = company.price
                    final_data.nataly_links = company.url

                if 'GOMANY' in company.__class__.__name__:
                    final_data.gomany_articles = company.article
                    final_data.gomany_prices = company.price
                    final_data.gomany_links = company.url

            if any((final_data.nataly_articles, final_data.gomany_articles)):
                final_list.append(astuple(final_data))

        self.repo.run(final_list)


    '''
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
    # def run_gomany_women_service(self):

    def run_gomany_men_service(self):


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
    '''
