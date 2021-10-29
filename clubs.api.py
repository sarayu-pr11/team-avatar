import random

from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

clubs = []
club_list = [
    "To cultivate a desire for learning through team based trivia competitions -- Academic League",
    "To spread kindness and serve the school and community -- Acts of Random Kindness",
    "To create workshops to inspire young girls to pursue STEM -- All Girls STEM Society",
    "To have fun and find people to talk to about anime, games and manga -- Anime Club",
    "To get other people involved in Chess and Compete in chess Tournaments -- Bishops and Knights",
    "To provide a safe space for black students and allies -- Black Student Union",
    "To act as a form for students interested in neuroscience and provide opportunities to nurse neuroscience -- "
    "Brain Club",
    "To educate students on the pro-choice movement and encourage women empowerment through advocating for women's "
    "reproductive rights -- Club Choice",
    "Learn how to solve computer science security problems and build cyber security knowledge -- CTF Club",
    "To prepare emerging leaders and entrepreneurs in marketing, finance, hospitality and business management in high "
    "schools and the globe -- DECA",
    "To prepare emerging leaders and entrepreneurs in marketing, finance, hospitality and business management in high "
    "schools and the globe -- Del Norte Biology Club",
    "To identify a real-world problem and develop a solution to it. Equips students to become tech entrepreneurs and "
    "leaders -- Del Norte Business and Technology",
    ""
]


def _find_next_id():
    return max(jokes["id"] for joke in jokes) + 1


def _init_jokes():
    id = 1
    for joke in joke_list:
        jokes.append({"id": id, "joke": joke, "haha": 0, "boohoo": 0})
        id += 1


@api_bp.route('/joke')
def get_joke():
    if len(jokes) == 0:
        _init_jokes()
    return jsonify(random.choice(jokes))


@api_bp.route('/jokes')
def get_jokes():
    if len(jokes) == 0:
        _init_jokes()
    return jsonify(jokes)


if __name__ == "__main__":
    print(random.choice(joke_list))