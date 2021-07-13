#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test one Function at a time"""

from sentiment import extract_sentiment
from process import text_contain_word
import pytest

testdata = ["I think today will be a great day",
"I do no think this will turn out well"]

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):
    sentiment = extract_sentiment(sample)
    assert sentiment > 0

testdata2 = [
('There is a duck in this text',True),
('There is nothing here',False)
]

@pytest.mark.parametrize('sample, expected_output', testdata2)
def test_text_contains(sample, expected_output):
    word = 'duck'
    assert text_contain_word(word, sample) == expected_output
