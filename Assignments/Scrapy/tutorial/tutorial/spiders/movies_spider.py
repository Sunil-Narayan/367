import scrapy
import re


class MoviesSpider(scrapy.Spider):
    name = "movies"

    def start_requests(self):
        urls = [
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=1&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=51&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=101&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=151&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=201&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=251&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=301&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=351&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=401&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=451&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=501&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=551&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=601&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=651&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=701&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=751&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=801&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=851&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=901&ref_=adv_prv',
        'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&start=951&ref_=adv_prv']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.lister-item-content'):
            g = quote.css('p.sort-num_votes-visible').get()
            yield {
                'Movie': quote.css('h3.lister-item-header a::text').get(),
                'Director': quote.css('p a::text').get(),
                'Genre': quote.css('span.genre::text').get()[1:-12].split(","),
                'Gross (millions USD)': re.findall(r'\$.*M', g)[0][1:-1],
                'Rating': quote.css('div.ratings-bar strong').get()[8:11],
            }