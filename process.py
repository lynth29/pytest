#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parametrize with a List of Examples and Expected Outputs"""

import pytest

def text_contain_word(word: str, text: str):
    """Find whether the text contains a particular word."""
    return word in text

testdata = [
('There is a duck in this text',True),
('There is nothing here',False)
]

@pytest.mark.parametrize('sample, expected_output', testdata)
def test_text_contains(sample, expected_output):
    word = 'duck'
    assert text_contain_word(word, sample) == expected_output
