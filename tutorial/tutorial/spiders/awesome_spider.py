import scrapy


class AwesomeSpider(scrapy.Spider):
    name = "awesome"

    async def start(self):
        # GET request
        yield scrapy.Request(
            "https://httpbin.dev/get", meta={"playwright": True}, callback=self.parse
        )
        # POST request
        yield scrapy.FormRequest(
            url="https://httpbin.dev/post",
            formdata={"foo": "bar"},
            meta={"playwright": True},
            callback=self.parse,
        )

    def parse(self, response, **kwargs):
        # 'response' contains the page as seen by the browser
        return {"response": response}
