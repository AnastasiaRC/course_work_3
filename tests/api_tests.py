import pytest
import json
from dao.dao import PostsDAO
from run import app

posts = PostsDAO('./data/posts.json', './data/comments.json')


def test_api_all_posts():
    test_posts = []
    with open('./data/posts.json', 'r', encoding='utf-8') as f:
        test_posts = json.load(f)
    assert len(test_posts) == len(posts.load_posts_json())


keys_right = {
    'poster_name',
    'poster_avatar',
    'pic',
    'content',
    'views_count',
    'likes_count',
    'pk'
}


def test_all_posts():
    response = app.test_client().get('/api/posts/', follow_redirects=True)
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == list
    assert set(api_response[0].keys()) == keys_right


def test_api_post():
    response = app.test_client().get('/api/posts/', follow_redirects=True)
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == dict
    assert set(api_response[0].keys()) == keys_right
