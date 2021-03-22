# get data using scraping library
# select more accurate features to improve model accuracy

from basketball_reference_scraper.players import get_stats

s = get_stats('James Harden', stat_type='PER_GAME', playoffs=False, career=False)


