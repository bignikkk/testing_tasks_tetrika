import scrapy
from collections import defaultdict
import csv

from animals.settings import ALLOWED_DOMAINS, START_URLS


class AnimalsSpider(scrapy.Spider):
    """Паук для парсинга сайта Wikipedia."""

    name = "animals"
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS
    letter_counts = defaultdict(int)

    def parse(self, response):
        """Парсит страницу и считает животных по первой букве."""

        category_links = response.css(
            "div.mw-category-group ul li a::text").getall()
        for item in category_links:
            first_letter = item[0].upper()
            if 'А' <= first_letter <= 'Я':
                self.letter_counts[first_letter] += 1

        next_page = response.css(
            "a:contains('Следующая страница')::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        else:
            self.save_csv()

    def save_csv(self):
        """Сохраняет результаты подсчёта в файл beasts.csv."""

        with open(
            "beasts.csv", mode="w", newline='', encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            for letter in sorted(self.letter_counts.keys()):
                writer.writerow([letter, self.letter_counts[letter]])
