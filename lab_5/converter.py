from tkinter import *
import tkinter.ttk as ttk
from collections import namedtuple
import urllib.request
import xml.dom.minidom
from datetime import datetime
import sys

import matplotlib
import matplotlib.pyplot as plt


CURRENCY_DAILY_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
CURRENCY_DYNAMIC_BASE_URL = 'http://www.cbr.ru/scripts/XML_dynamic.asp'
RUS_CURRENCY_NAME = 'Российский рубль'


class CurrencyRate:
    def __init__(self):
        self.currency_rate = self.get_currency_rate()
        self.periods_dict = {
            'Январь 2020': 'date_req1=01/01/2020&date_req2=31/01/2020',
            'Февраль 2020': 'date_req1=01/02/2020&date_req2=29/02/2020',
            'Март 2020': 'date_req1=01/03/2020&date_req2=31/03/2020',
            'Апрель 2020': 'date_req1=01/04/2020&date_req2=30/04/2020',
            'Mай 2020': 'date_req1=01/05/2020&date_req2=31/05/2020',
            'Июнь 2020': 'date_req1=01/06/2020&date_req2=30/06/2020',
            'Июль 2020': 'date_req1=01/07/2020&date_req2=31/07/2020',
            'Август 2020': 'date_req1=01/08/2020&date_req2=31/08/2020',
            'Сентябрь 2020': 'date_req1=01/09/2020&date_req2=30/09/2020',
            'Октябрь 2020': 'date_req1=01/10/2020&date_req2=31/10/2020',
            'Ноябрь 2020': 'date_req1=01/11/2020&date_req2=30/11/2020',
            'Декабрь 2020': 'date_req1=01/12/2020&date_req2=31/12/2020',
        }

    @staticmethod
    def get_currency_rate() -> dict:
        response = urllib.request.urlopen(CURRENCY_DAILY_URL)
        dom = xml.dom.minidom.parse(response)
        node_collection = dom.getElementsByTagName('Valute')

        result = {}

        for node in node_collection:
            currency_id = node.attributes['ID'].value
            child_nodes = node.childNodes
            currency_char_code = child_nodes[1].firstChild.nodeValue
            currency_nominal = float(child_nodes[2].firstChild.nodeValue)
            currency_name = child_nodes[3].firstChild.nodeValue
            currency_rate_raw = float(child_nodes[4].firstChild.nodeValue.replace(',', '.'))
            currency_rate = currency_rate_raw / currency_nominal
            nt = namedtuple(currency_char_code, ['id', 'rate'])

            result[currency_name] = nt(currency_id, currency_rate)

        nt = namedtuple('RUB', ['id', 'rate'])
        result[RUS_CURRENCY_NAME] = nt(None, 1.)

        return result

    def get_currency_in_dynamic(self, currency_name: str, period: str) -> namedtuple:
        currency_id = self.currency_rate[currency_name].id
        date_range = self.periods_dict[period]
        response = urllib.request.urlopen(f'{CURRENCY_DYNAMIC_BASE_URL}?{date_range}&VAL_NM_RQ={currency_id}')
        print(f'status code {response.status}', file=sys.stderr)
        dom = xml.dom.minidom.parse(response)
        node_collection = dom.getElementsByTagName('Record')
        nt = namedtuple('records', ['days', 'rates'])
        result = nt([], [])
        for node in node_collection:
            day = datetime.strptime(node.attributes['Date'].value, '%d.%m.%Y').day
            nominal = float(node.childNodes[0].firstChild.nodeValue)
            rate_raw = float(node.childNodes[1].firstChild.nodeValue.replace(',', '.'))
            rate = rate_raw / nominal
            result.days.append(day)
            result.rates.append(rate)

        return result

    def convert(self, currency_name_from: str, currency_name_to: str, number: float) -> float:
        result = number * self.currency_rate[currency_name_from].rate / self.currency_rate[currency_name_to].rate
        return result


def app(cr_object: CurrencyRate):
    currency_name_collection = list(cr_object.currency_rate.keys())

    def convert():
        currency_name_from = combo.get()
        currency_name_to = combo_2.get()
        number = float(input_num.get())
        result = cr_object.convert(currency_name_from, currency_name_to, number)
        output_num.configure(text=result)

    def plot_graph():
        fig = plt.figure()
        canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=tab_2)

        period = combo_3.get()
        currency_name = combo_4.get()

        print(f'запрос за {period} для валюты {currency_name}', file=sys.stderr)

        data = cr_object.get_currency_in_dynamic(currency_name, period)

        plot_widget = canvas.get_tk_widget()
        fig.clear()
        plt.plot(data.days, data.rates)
        plt.grid()
        plot_widget.grid(column=1, row=3, padx=5, pady=10)

    window = Tk()
    window.title('Конвертер валют')
    window.geometry("900x700")

    tab_control = ttk.Notebook(window)
    tab_1 = ttk.Frame(tab_control)
    tab_2 = ttk.Frame(tab_control)
    tab_control.add(tab_1, text='Курсы валют')
    tab_control.add(tab_2, text='График')

    # первая вкладка (Курсы валют)
    combo = ttk.Combobox(tab_1, width=30)
    combo['values'] = currency_name_collection
    combo.grid(column=0, row=0, padx=5, pady=5)
    combo_2 = ttk.Combobox(tab_1, width=30)
    combo_2['values'] = currency_name_collection
    combo_2.grid(column=1, row=0, padx=5, pady=5)

    input_num = Entry(tab_1)
    input_num.grid(column=0, row=1, padx=5, pady=5)

    output_num = Label(tab_1, text='')
    output_num.grid(column=1, row=1, padx=5, pady=5)

    btn = Button(tab_1, text='Конвертировать', command=convert)
    btn.grid(column=2, row=0, padx=5, pady=10)

    # вторая вкладка (График)
    matplotlib.use('TkAgg')

    combo_3 = ttk.Combobox(tab_2, width=30)
    combo_3['values'] = list(cr_object.periods_dict.keys())
    combo_3.grid(column=0, row=0, padx=5, pady=10)
    combo_4 = ttk.Combobox(tab_2, width=30)
    combo_4['values'] = currency_name_collection
    combo_4.grid(column=0, row=1, padx=5, pady=10)

    btn_2 = Button(tab_2, text='График', command=plot_graph)
    btn_2.grid(column=0, row=2, padx=5, pady=10)

    tab_control.pack(expand=1, fill='both')
    window.mainloop()


if __name__ == '__main__':
    cr = CurrencyRate()
    app(cr)
