import telebot
import json
from inheritors.mhl import mhl_parse
from inheritors.mhl import mhl_regular_season_parser
from inheritors.khl import khl_parse
from inheritors.khl import khl_regular_season_parser
# from inheritors.shl import shl_parse
from inheritors.nhl import nhl_regular_season_parser

bot = telebot.TeleBot('5254316199:AAG0259Rkkzmb179uY6tGW3fSQ8jLy5iBhA')


def read_json(path, chat):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for info in data:
            bot.send_message(chat, f"<b>{info['date']}</b>", parse_mode='html')
            for records_info in info['records']:
                bot.send_message(chat, f"{records_info['team']} vs {records_info['team-opposite']} ({records_info['time']})")

def read_regular_season_json(path, chat):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            bot.send_message(chat, f"<b>{item['conference']}</b>", parse_mode='html')
            for team in item['records']:
                bot.send_photo(chat, f"{team['logo']}")
                bot.send_message(chat, f"{team['team-position']},  {team['team-name']} \n"
                                       f"GP: {team['GP']} \n"
                                       f"W: {team['W']} \n"
                                       f"ROW: {team['ROW']} \n"
                                       f"OT: {team['OT']} \n"
                                       f"L: {team['L']} \n"
                                       f"GF: {team['GF']} \n"
                                       f"PTS: {team['PTS']}")

def read_nhl_regular_season_json(path, chat):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        # print(data)
        for item in data:
            # print(item)
            bot.send_message(chat, f"<b>{item['conference']} {item['division']}</b>", parse_mode='html')
            for team in item['records']:
                # print(team)
                bot.send_message(chat, f"{team['team-position']} | <b>{team['team-name']}</b> \n"
                                       f"GP: {team['GP']} \n"
                                       f"W: {team['W']} \n"
                                       f"ROW: {team['ROW']} \n"
                                       f"OT: {team['OT']} \n"
                                       f"L: {team['L']} \n"
                                       f"GF: {team['GF']} \n"
                                       f"PTS: {team['PTS']}", parse_mode='html')

def call_parser(parser_name, chat):
    if parser_name == 'mhl playoffs':
        return _mhl_playoffs(parser_name, chat)
    if parser_name == 'mhl regular season':
        return _mhl_regular_season(parser_name, chat)
    if parser_name == 'khl playoffs':
        return _khl_playoffs(parser_name, chat)
    if parser_name == 'khl regular season':
        return _khl_regular_season(parser_name, chat)
    if parser_name == 'shl playoffs':
        return _shl_playoffs(parser_name, chat)
    # if parser_name == 'shl regular season':
    #     return _shl_regular_season(parser_name, chat)
    if parser_name == 'nhl playoffs':
        return _nhl_playoffs(parser_name, chat)
    if parser_name == 'nhl regular season':
        return _nhl_regular_season(parser_name, chat)

def _mhl_playoffs(parser_name, chat):
    print(parser_name)
    mhl_parse.main()
    read_json('json_files/mhl_playoffs_data.json', chat)

def _mhl_regular_season(parser_name, chat):
    print(parser_name)
    mhl_regular_season_parser.main()
    read_regular_season_json('json_files/mhl_regular_season_data.json', chat)

def _khl_playoffs(parser_name, chat):
    print(parser_name)
    khl_parse.main()
    read_json('json_files/khl_playoffs_data.json', chat)
def _khl_regular_season(parser_name, chat):
    print(parser_name)
    khl_regular_season_parser.main()
    read_regular_season_json('json_files/khl_regular_season_data.json', chat)

def _shl_playoffs(parser_name, chat):
    print(parser_name)
    bot.send_message(chat, "sorry, we haven't information")

# def _shl_regular_season(parser_name, chat):
#     print(parser_name)
#     if shl_parse.main() == False:
#         bot.send_message(chat, "sorry, we haven't information" )
#     else:
#         read_json('json_files/shl_matches_data.json', chat)

def _nhl_playoffs(parser_name, chat):
    print(parser_name)


def _nhl_regular_season(parser_name, chat):
    print(parser_name)
    nhl_regular_season_parser.main()
    read_nhl_regular_season_json('json_files/nhl_regular_season_data.json', chat)