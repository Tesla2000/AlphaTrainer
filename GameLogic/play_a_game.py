from collections import defaultdict

from sklearn.tree import DecisionTreeClassifier

from PySplendor.Game import Game


def play_a_game(
    x: list,
    y: list,
    model: DecisionTreeClassifier = None,
    model_decision_weight: float = 1,
):
    game = Game()
    states = defaultdict(list)
    while True:
        current_player = game.current_player
        game = game.get_best_state(10)
        if game.is_terminal():
            for player in game.players:
                result = game.get_result(player).value
                player_id = player.id
                x += states[player_id]
                y += len(states[player_id]) * [result]
            print(len(states[game.current_player.id]))
            break
        states[current_player.id].append(game.get_state())
        game.next_turn()
