#!/usr/bin/env python3

import finance as fin
import json
import unittest.mock as mock
from decimal import Decimal
from unittest.mock import Mock, patch

def replacement_func():
    return [{ 'LastTradePrice': '123.45', 'StockSymbol': 'AAPL'}]

class TestClass():
    def __init__(self, input_quote):
        self.ticker = input_quote
        self.quote = self.test_mock_function_call(input_quote)

    @patch('finance.getQuotes')
    def test_mock_function_call(self, ticker='', mock_func=None):
        mock_func.return_value = replacement_func()
        print(ticker)
        some_value = fin.getQuote(ticker)
        print(some_value)
        return some_value

def main():
    test_object = TestClass('XOM')
    print(test_object.test_mock_function_call('AAPL'))
    assert test_object.quote == Decimal('123.45')
    assert isinstance(test_object.quote, Decimal)

if __name__ == '__main__':
    main()