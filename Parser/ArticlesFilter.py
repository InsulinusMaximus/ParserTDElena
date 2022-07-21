import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Filter')


def article_filtering(parsing_result, category_result, articles_data):
    for card_data in parsing_result:
        if card_data.article in articles_data:
            category_result.append(card_data)

    logger.info(f'Filtered {len(category_result)} elements')
