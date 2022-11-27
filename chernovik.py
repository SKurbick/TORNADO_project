import tornado.ioloop
import tornado.web
import os
import pandas as pd
import uuid
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("template.html", title="My title", items=items)



class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("base.html")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/predict", MainHandler),
            (r"/", BaseHandler),
        ]
        settings = dict(
            title=u"Registrations Form",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            # static_path=os.path.join(os.path.dirname(__file__), "static"),
            # xsrf_cookies=True,
            # cookie_secret=uuid.uuid4().int,
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)


def main():
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
