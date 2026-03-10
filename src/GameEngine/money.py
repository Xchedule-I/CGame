from __future__ import annotations

from typing import Dict, Union


class Money:
    """
    amount : total amount by the player acquired
    currency  : showcase the currency
    per_day_profit : profit of the day made by player.
    """
    amount: int
    currency: str = "$ "
    per_day_profit : int = 0

    def __init__(self, amount: int) -> None:
        self.amount = amount

    @classmethod
    def inc(cls, amount: int) -> None:
        cls.amount += amount

    @classmethod
    def dec(cls, amount: int) -> bool:
        """
        Allow Money debt but only certain debt level
        :param amount:
        :return:
        """
        if cls.amount < 2500 or cls.amount + amount < 2500: return False
        cls.amount -= amount
        return True

    @classmethod
    def get_money(cls) -> int:
        """ Returns money amount"""
        return cls.amount

    @classmethod
    def set_money(cls, amount: int) -> None:
        """
        Allowed this function for dev & Testing purposes only.
        :param amount:
        :return:
        """
        cls.amount = amount

    @classmethod
    def to_dict(cls) -> Dict[str, Union[str, int]]:
        """
        Serializes Money objects for GameState.json saving
        :return:
        """
        return {"amount": cls.amount,
                "currency": cls.currency}
