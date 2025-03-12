import os
from flask import Flask, jsonify, request
import json
import random
import requests
import pytest

""" @pytest.fixture
def base_url():
    base_url = 'http://127.0.0.1:5000'
    return base_url """

def test_shuffle_endpoint():
    list = [1, 2, 3, 4]
    response = requests.get('http://localhost:5000/shuffle', json={'list_of_ints': list})
    shuffled_list = response.json()['shuffled_list']

    assert set(list) == set(shuffled_list)
    assert list != shuffled_list