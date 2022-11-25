#  3. Реалізуйте класс Transaction. Його конструктор повинен приймати такі параметри:
# - amount - суму на яку було здійснено транзакцію
# - date - дату переказу
# - currency - валюту в якій було зроблено переказ (за замовчуванням USD)
# - usd_conversion_rate - курс цієї валюти до долара (за замовчуванням 1.0)
# - description - опис транзакції (за дефолтом None)
# Усі параметри повинні бути записані в захищені (_attr) однойменні атрибути.
# Доступ до них повинен бути забезпечений лише на читання та за допомогою механізму property. При чому якщо
# description дорівнює None, то відповідне property має повертати рядок "No description provided". Додатково
# реалізуйте властивість usd, що має повертати суму переказу у доларах (сума * курс)


class Transaction(object):

    def __init__(self, amount, date, currency='USD', usd_conversion_rate=1.0, description=None):
        self._amount = amount
        self._date = date
        self._currency = currency
        self._usd_conversation_rate = usd_conversion_rate
        self._description = description

    @property
    def amount(self):
        # print('Amount getter')
        return self._amount

    @amount.setter
    def amount(self, value):
        # print('Amount setter')
        self._amount = float(value)

    @property
    def date(self):
        return self._date

    @property
    def currency(self):
        return self._currency

    @property
    def usd_conversation_rate(self):
        return self._usd_conversation_rate

    @property
    def description(self):
        if not self._description:
            return 'No description provided'
        else:
            return self._description

    @property
    def usd(self):
        if self.currency == 'USD':
            return self.amount
        else:
            return self.amount * self.usd_conversation_rate


trn = Transaction(1500, '22-12-2000', 'UAH', 37.9, 'Crazy rate!')
print(trn.amount)
print(trn.date)
print(trn.currency)
print(trn.usd_conversation_rate)
print(trn.description)
trn.amount = 1000
print(trn.usd)

trn = Transaction(1500, '25-12-2000')
print(trn.amount)
print(trn.date)
print(trn.currency)
print(trn.usd_conversation_rate)
print(trn.description)
trn.amount = 1000
print(trn.usd)
