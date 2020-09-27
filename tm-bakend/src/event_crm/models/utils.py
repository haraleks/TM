from enum import Enum


class PaymemntsTypes(Enum):
    CASH = 'cash'
    BANK_CARD = 'bank_card'

    @classmethod
    def CHOISES(cls):
        return (
            (cls.CASH.value, 'наличные'),
            (cls.BANK_CARD.value, 'карта банка'),
        )
