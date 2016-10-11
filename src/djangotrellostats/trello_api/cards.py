from djangotrellostats.trello_api.connector import TrelloConnector

from trello import Card as TrelloCard


# Move the card to other list
def move_card(card, member, destination_list):
    # Communication with Trello
    trello_connector = TrelloConnector(member)
    trello_board = trello_connector.trello_client.get_board(card.board.uuid)
    trello_card = TrelloCard(parent=trello_board, card_id=card.uuid)
    trello_card.change_list(destination_list.uuid)
