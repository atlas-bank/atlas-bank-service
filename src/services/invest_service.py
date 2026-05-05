import os

from models.account import Account
from models.invest import Invest
from models.user import User
from repositories.invest_repository import InvestRepository


class InvestService:
    def __init__(self):
        self.repository = InvestRepository()
        self.br_api_token = os.getenv("BR_API_TOKEN")

    def create_invest_account(self, account: Account, user: User):
        invest_account = Invest(account=account, user=user)
        self.repository.save(invest_account)

    def send_invest_account_create_email(self, invest_account: Invest):
        pass

    def buy_fixed_income(self, invest_account: Invest, amount: float, percentage: float, name: str):
        pass

    def buy_stock(self, invest_account: Invest, amount: float, stock_code: str, quantity: int):


        pass
