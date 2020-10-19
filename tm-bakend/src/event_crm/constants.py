from enum import Enum


class EventTypes(Enum):
    NLP_PRAKTIC = 'курс НЛП практик'
    MASTER_CLASS = 'мастер класс'
    TRENING = 'тренинг'
    GAME = 'трансформационная игра'
    ON_LINE = 'Он-лайн мероприятие'

    @classmethod
    def CHOISES(cls):
        return (
            (cls.NLP_PRAKTIC.value, 'nlp_practic'),
            (cls.MASTER_CLASS.value, 'master_class'),
            (cls.TRENING.value, 'trening'),
            (cls.GAME.value, 'game'),
            (cls.ON_LINE.value, 'on-line event'),
        )
