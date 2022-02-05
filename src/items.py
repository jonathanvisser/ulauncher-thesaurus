from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

def generate_result_item(search):
    return ExtensionResultItem(
        icon=search['icon'],
        name=search['name'],
        description=search['description'],
        on_enter=OpenUrlAction(search['name'])
    )


def generate_result_items(results):
    return [
        generate_result_item(search)
    for search in results]