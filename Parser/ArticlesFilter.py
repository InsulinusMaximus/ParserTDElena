import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Filter')


def article_filtering(parsing_result, category_result, article_data):

    # Checking which article came: if the keys,
    # then this is the article of TD Elena, and they come in the form of a one-dimensional write_list,
    # and in the case of values, they come in the form of a multidimensional write_list,
    # where the values are tuples
    article_list = list(article_data)
    if isinstance(article_list[0], tuple):
        article_list = [i for item in article_list for i in item]

    for card_data in parsing_result:
        if card_data.article in article_list:
            category_result.append(card_data)

    for data in category_result:
        if data.article in article_list:
            article_list.remove(data.article)

    logger.info(f'Not found {article_list}')
    logger.info(f'Filtered {len(category_result)} elements')
