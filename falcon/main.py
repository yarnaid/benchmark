import falcon
import json


class ItemResource():
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_OK
        resp.body = json.dumps({'version': 0, 'service': 'falcon'})


app = falcon.API()

items = ItemResource()

app.add_route('/item', items)
