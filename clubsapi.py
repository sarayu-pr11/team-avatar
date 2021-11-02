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
    "To learn how to solve computer science security problems and build cyber security knowledge -- CTF Club",
    "To prepare emerging leaders and entrepreneurs in marketing, finance, hospitality and business management in high "
    "schools and the globe -- DECA",
    "To identify a real-world problem and develop a solution to it. Equips students to become tech entrepreneurs and "
    "leaders -- Del Norte Business and Technology",
    "To discuss and destigmatize topics relating to neurodiversity, representation, ableism, resources, self-advocacy, "
    "etc -- Del Norte Neurodiversity Advocacy",
    "To raise awareness for hunger relief and support the San Diego Food Bank through fundraisers and food drives -- "
    "DNHS Food Bank Club",
    "To do shows of improv comedy for the DNHS student body and their families -- DNHS Improv Team",
    "To give students opportunities to share their voice in a safe environment through writing -- DNHS Diverse Diaries",
    "To both provide a safe space for and spread awareness of the LGBTQ+ community at Del Norte -- Gender Sexuality "
    "Alliance",
    "To help students explore the medical field and participate in community device projects -- HOSA",
    "To promote volunteering and fundraising for the communities -- Key Club",
    "To destigmatize mental illness through letter-writing, advocacy, and creating a safe space for students to "
    "de-stress -- Letters to Strangers",
    "To prepare academic trivia competitions: encourage participation, breadth and depth of academic knowledge -- "
    "Quiz Bowl",
    "To inspire passion for science and allow access to various scientific competitions for those seeking to take "
    "their learning to the next level -- Science Alliance ",
    "To play the popular game Super Smash Bros Ultimate and to have fun -- Smash Club",
    "To recite speeches and practice debates on current events; compete at tournaments -- Speech and Debate Club",
    "To use art to help the community -- Stickers for Charity",
    "To build a robot for the FRC regional competition in March; also to fund and market the robot -- Team Optix "
    "Robotics ",
    "To teach students how to crochet and knit -- Teenage Grandma Society",
    "To inspire and motivate young women to pursue STEM Careers -- Women in Science and Engineering"
]


def _find_next_id():
    return max(clubs["id"] for club in clubs) + 1


def _init_clubs():
    id = 1
    for club in club_list:
        clubs.append({"id": id, "club": club, "Maybe I'll Join": 0, "Not My Thing": 0})
        id += 1


@api_bp.route('/club')
def get_club():
    if len(clubs) == 0:
        _init_clubs()
    club = random.choice(clubs)
    return club


if __name__ == "__main__":
    print(random.choice(clubs))
