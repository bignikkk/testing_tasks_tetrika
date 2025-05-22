import pytest
from scrapy.http import HtmlResponse, Request
from animals.spiders.animal_spider import AnimalsSpider


@pytest.fixture
def html_response():
    """
    Возвращает мок-ответ с HTML, содержащим трех животных.
    """

    html = """
    <html>
        <body>
            <div class="mw-category-group">
                <ul>
                    <li><a>Аист</a></li>
                    <li><a>Барсук</a></li>
                    <li><a>Бобр</a></li>
                </ul>
            </div>
        </body>
    </html>
    """
    request = Request(url="https://example.com")
    return HtmlResponse(
        url="https://example.com", body=html,
        encoding='utf-8', request=request
    )


def test_parse_counts_letters(html_response):
    """
    Проверяет, что паук корректно считает количество животных по первой букве.
    """

    spider = AnimalsSpider()
    list(spider.parse(html_response))

    assert spider.letter_counts["А"] == 1
    assert spider.letter_counts["Б"] == 2
