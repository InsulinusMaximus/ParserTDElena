from dataclasses import astuple
from general_data import general_data as general_data
from Parser import TDElenaParser, NatalyParser, GomanyParser, TDValeriayParser, OddisParcer, ModnoParser, InstanceParser
from repository import Repository
from Parser.ArticlesFilter import article_filtering
import Parser.Config.NatalyConfig as ConfigNataly
import Parser.Config.GomanyConfig as ConfigGomany
import Parser.Config.TDValeriayConfig as ConfigTDValeriya
import Parser.Config.OddisConfig as ConfigOddis
import Parser.Config.ModnoConfig as ConfigModno
import Parser.Config.InstanceConfig as ConfigInstance


class Service:

    def __init__(self):
        # Initialization of site parsing TD Elena
        self.TDElena_parser = TDElenaParser.Parser_TDElena()

        # Announcement of parsers of other companies
        self.Nataly_parser = NatalyParser.Parser_Nataly()
        self.Gomany_parser = GomanyParser.Parser_Gomany()
        self.TDValeriay_parser = TDValeriayParser.Parser_TDValeriya()
        self.Oddis_parser = OddisParcer.Parser_Oddis()
        self.Modno_parser = ModnoParser.Parser_Modno()
        self.Instance_parser = InstanceParser.Parser_Instance()

        self.repo = Repository()

    # WOMEN SERVICE

    def run_women_service(self):
        category = 'WOMEN'
        self.TDElena_parser.run_women_parsing()

        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          article_data=ConfigNataly.women_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          article_data=ConfigGomany.women_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          article_data=ConfigTDValeriya.women_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          article_data=ConfigOddis.women_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          article_data=ConfigModno.women_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_women,
                          article_data=ConfigInstance.women_articles_dict.keys()
                          )

        self.Nataly_parser.run_women_parsing()
        self.Gomany_parser.run_women_parsing()
        self.TDValeriay_parser.run_women_parsing()
        self.Oddis_parser.run_women_parsing()
        self.Modno_parser.run_women_parsing()
        self.Instance_parser.run_women_parsing()

        general_company_women_result = (self.Nataly_parser.result_nataly_women +
                                        self.Gomany_parser.result_gomany_women +
                                        self.TDValeriay_parser.result_tdvaleriay_women +
                                        self.Oddis_parser.result_oddis_women +
                                        self.Modno_parser.result_modno_women +
                                        self.Instance_parser.result_instance_women)
        general_tdelena_women_result = self.TDElena_parser.result_tdelena_women
        overall_women_articles_dict = (ConfigNataly.women_articles_dict |
                                       ConfigGomany.women_articles_dict |
                                       ConfigTDValeriya.women_articles_dict |
                                       ConfigOddis.women_articles_dict |
                                       ConfigModno.women_articles_dict |
                                       ConfigInstance.women_articles_dict)

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

                if 'TDVALERIAY' in company.__class__.__name__:
                    final_data.td_valeriay_articles = company.article
                    final_data.td_valeriay_prices = company.price
                    final_data.td_valeriay_links = company.url

                if 'ODDIS' in company.__class__.__name__:
                    final_data.oddis_articles = company.article
                    final_data.oddis_prices = company.price
                    final_data.oddis_links = company.url

                if 'MODNO' in company.__class__.__name__:
                    final_data.modno_articles = company.article
                    final_data.modno_prices = company.price
                    final_data.modno_links = company.url

                if 'INSTANCE' in company.__class__.__name__:
                    final_data.instance_articles = company.article
                    final_data.instance_prices = company.price
                    final_data.instance_links = company.url

            if any((final_data.nataly_articles, final_data.gomany_articles, final_data.td_valeriay_articles,
                    final_data.oddis_articles, final_data.modno_articles, final_data.instance_articles)):
                final_list.append(astuple(final_data))

        self.repo.run(final_list, category)

    # MEN SERVICE

    def run_men_service(self):
        category = 'MEN'
        self.TDElena_parser.run_men_parsing()

        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          article_data=ConfigNataly.men_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          article_data=ConfigGomany.men_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          article_data=ConfigTDValeriya.men_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          article_data=ConfigOddis.men_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          article_data=ConfigModno.men_articles_dict.keys()
                          )
        article_filtering(parsing_result=self.TDElena_parser.parsing_result,
                          category_result=self.TDElena_parser.result_tdelena_men,
                          article_data=ConfigInstance.men_articles_dict.keys()
                          )

        self.Nataly_parser.run_men_parsing()
        self.Gomany_parser.run_men_parsing()
        self.TDValeriay_parser.run_men_parsing()
        self.Oddis_parser.run_men_parsing()
        self.Modno_parser.run_men_parsing()
        self.Instance_parser.run_men_parsing()

        general_company_men_result = (self.Nataly_parser.result_nataly_men +
                                      self.Gomany_parser.result_gomany_men +
                                      self.TDValeriay_parser.result_tdvaleriay_men +
                                      self.Oddis_parser.result_oddis_men +
                                      self.Modno_parser.result_modno_men +
                                      self.Instance_parser.result_instance_men)
        general_tdelena_men_result = self.TDElena_parser.result_tdelena_men
        overall_men_articles_dict = (ConfigNataly.men_articles_dict |
                                     ConfigGomany.men_articles_dict |
                                     ConfigTDValeriya.men_articles_dict |
                                     ConfigOddis.men_articles_dict |
                                     ConfigModno.men_articles_dict |
                                     ConfigInstance.men_articles_dict)

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

                if 'TDVALERIAY' in company.__class__.__name__:
                    final_data.td_valeriay_articles = company.article
                    final_data.td_valeriay_prices = company.price
                    final_data.td_valeriay_links = company.url

                if 'ODDIS' in company.__class__.__name__:
                    final_data.oddis_articles = company.article
                    final_data.oddis_prices = company.price
                    final_data.oddis_links = company.url

                if 'ODDIS' in company.__class__.__name__:
                    final_data.modno_articles = company.article
                    final_data.modno_prices = company.price
                    final_data.modno_links = company.url

                if 'INSTANCE' in company.__class__.__name__:
                    final_data.instance_articles = company.article
                    final_data.instance_prices = company.price
                    final_data.instance_links = company.url

            if any((final_data.nataly_articles, final_data.gomany_articles, final_data.td_valeriay_articles,
                    final_data.oddis_articles, final_data.modno_articles, final_data.instance_articles)):
                final_list.append(astuple(final_data))

        self.repo.run(final_list, category)
