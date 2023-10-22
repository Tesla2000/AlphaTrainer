from collections import defaultdict

from sklearn.tree import DecisionTreeClassifier

from GameLogic.choose_move import choose_move
from PySplendor.Game import Game
from alpha_trainer.exceptions.GameFinishedException import GameFinishedException
from alpha_trainer.exceptions.NoPossibleMoveException import NoPossibleMoveException


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
        state = game.get_state()
        try:
            move, move_index = choose_move(
                game, state, game.all_moves, model, model_decision_weight
            )
        except NoPossibleMoveException:
            winner_id = id(game.players[-1])
            x += states[winner_id]
            y += len(states[winner_id]) * [1]
            break
        states[id(current_player)].append(state + [move_index])
        move.perform(game)
        try:
            game.next_turn()
        except GameFinishedException as e:
            winner_id = id(e.args[0])
            x += states[winner_id]
            y += len(states[winner_id]) * [1]
            break
