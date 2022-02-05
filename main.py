from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

from src.big_huge_thesaurus_search import BHTSearch
from src.items import generate_result_items


class DemoExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        query = event.get_argument() or str()
        # params = strip_list(query.split(' '))  
        params = query
        api_key = extension.preferences['api_key']
        search = BHTSearch(params,api_key)
        results = search.search()

        items = []
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='Item %s' % params,
                                         description='Item description %s' % params,
                                         on_enter=HideWindowAction()))

        return RenderResultListAction(generate_result_items(results))

if __name__ == '__main__':
    DemoExtension().run()