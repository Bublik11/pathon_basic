class User(object):

    def __init__(self, name: str, best_score=0, is_playing=False):
        self.name = name
        self.best_score = best_score
        self.is_playing = is_playing

    def update_best_score(self, update_score: int):
        self.best_score = update_score

    def play(self):
        self.is_playing = True

    def play_stop(self):
        self.is_playing = False

    def print_info(self):
        print(f"| Игрок: {self.name} | Лучший счет: {self.best_score} | "
              f"Играет сейчас: {'да' if self.is_playing else 'нет'} |")
