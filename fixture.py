#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fixtures: Use the Same Data to Test Different Functions"""

import pytest
from sentiment import extract_sentiment
from process import text_contain_word

@pytest.fixture
def example_data():
    return 'Today I found a duck and I am happy'

def test_extract_sentiment(example_data):
    sentiment = extract_sentiment(example_data)
    assert sentiment > 0

def test_text_contains(example_data):
    word = 'duck'
    assert text_contain_word(word, example_data) == True
