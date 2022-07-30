import requests
import json

OPENDOTA_URL = 'https://api.opendota.com/api'
DEFAULT_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': '_ga=GA1.2.1568616352.1658875198', 'referer': 'https://github.com/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}


class Matches():
    def get_matches(self, match_id=None):
        """
        Match data
        """
        data = {'match_id': match_id, }
        response = requests.get(f"{OPENDOTA_URL}/matches/{match_id}", header=DEFAULT_HEADERS, data=data)
        return response.json()


class PlayersByRank():
    def get_playersByRank(self):
        """
        Players ordered by rank/medal tier
        """
        data = {}
        response = requests.get(f"{OPENDOTA_URL}/playersByRank", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Players():
    def get_players(self, account_id=None):
        """
        Player data
        """
        data = {'account_id': account_id, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_players_wl(self, account_id=None, limit=None, offset=None, win=None, patch=None, game_mode=None,
                       lobby_type=None, region=None, date=None, lane_role=None, hero_id=None, is_radiant=None,
                       included_account_id=None, excluded_account_id=None, with_hero_id=None, against_hero_id=None,
                       significant=None, having=None, sort=None):
        """
        Win/Loss count
        """
        data = {'account_id': account_id, 'limit': limit, 'offset': offset, 'win': win, 'patch': patch,
                'game_mode': game_mode, 'lobby_type': lobby_type, 'region': region, 'date': date,
                'lane_role': lane_role, 'hero_id': hero_id, 'is_radiant': is_radiant,
                'included_account_id': included_account_id, 'excluded_account_id': excluded_account_id,
                'with_hero_id': with_hero_id, 'against_hero_id': against_hero_id, 'significant': significant,
                'having': having, 'sort': sort, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/wl", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_players_recentMatches(self, account_id=None):
        """
        Recent matches played
        """
        data = {'account_id': account_id, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/recentMatches", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_players_matches(self, account_id=None, limit=None, offset=None, win=None, patch=None, game_mode=None,
                            lobby_type=None, region=None, date=None, lane_role=None, hero_id=None, is_radiant=None,
                            included_account_id=None, excluded_account_id=None, with_hero_id=None, against_hero_id=None,
                            significant=None, having=None, sort=None, project=None):
        """
        Matches played
        """
        data = {'account_id': account_id, 'limit': limit, 'offset': offset, 'win': win, 'patch': patch,
                'game_mode': game_mode, 'lobby_type': lobby_type, 'region': region, 'date': date,
                'lane_role': lane_role, 'hero_id': hero_id, 'is_radiant': is_radiant,
                'included_account_id': included_account_id, 'excluded_account_id': excluded_account_id,
                'with_hero_id': with_hero_id, 'against_hero_id': against_hero_id, 'significant': significant,
                'having': having, 'sort': sort, 'project': project, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/matches", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_players_heroes(self, account_id=None, limit=None, offset=None, win=None, patch=None, game_mode=None,
                           lobby_type=None, region=None, date=None, lane_role=None, hero_id=None, is_radiant=None,
                           included_account_id=None, excluded_account_id=None, with_hero_id=None, against_hero_id=None,
                           significant=None, having=None, sort=None):
        """
        Heroes played
        """
        data = {'account_id': account_id, 'limit': limit, 'offset': offset, 'win': win, 'patch': patch,
                'game_mode': game_mode, 'lobby_type': lobby_type, 'region': region, 'date': date,
                'lane_role': lane_role, 'hero_id': hero_id, 'is_radiant': is_radiant,
                'included_account_id': included_account_id, 'excluded_account_id': excluded_account_id,
                'with_hero_id': with_hero_id, 'against_hero_id': against_hero_id, 'significant': significant,
                'having': having, 'sort': sort, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/heroes", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_players_peers(self, account_id=None, limit=None, offset=None, win=None, patch=None, game_mode=None,
                          lobby_type=None, region=None, date=None, lane_role=None, hero_id=None, is_radiant=None,
                          included_account_id=None, excluded_account_id=None, with_hero_id=None, against_hero_id=None,
                          significant=None, having=None, sort=None):
        """
        Players played with
        """
        data = {'account_id': account_id, 'limit': limit, 'offset': offset, 'win': win, 'patch': patch,
                'game_mode': game_mode, 'lobby_type': lobby_type, 'region': region, 'date': date,
                'lane_role': lane_role, 'hero_id': hero_id, 'is_radiant': is_radiant,
                'included_account_id': included_account_id, 'excluded_account_id': excluded_account_id,
                'with_hero_id': with_hero_id, 'against_hero_id': against_hero_id, 'significant': significant,
                'having': having, 'sort': sort, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/peers", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_players_pros(self, account_id=None, limit=None, offset=None, win=None, patch=None, game_mode=None,
                         lobby_type=None, region=None, date=None, lane_role=None, hero_id=None, is_radiant=None,
                         included_account_id=None, excluded_account_id=None, with_hero_id=None, against_hero_id=None,
                         significant=None, having=None, sort=None):
        """
        Pro players played with
        """
        data = {'account_id': account_id, 'limit': limit, 'offset': offset, 'win': win, 'patch': patch,
                'game_mode': game_mode, 'lobby_type': lobby_type, 'region': region, 'date': date,
                'lane_role': lane_role, 'hero_id': hero_id, 'is_radiant': is_radiant,
                'included_account_id': included_account_id, 'excluded_account_id': excluded_account_id,
                'with_hero_id': with_hero_id, 'against_hero_id': against_hero_id, 'significant': significant,
                'having': having, 'sort': sort, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/pros", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_players_totals(self, account_id=None, limit=None, offset=None, win=None, patch=None, game_mode=None,
                           lobby_type=None, region=None, date=None, lane_role=None, hero_id=None, is_radiant=None,
                           included_account_id=None, excluded_account_id=None, with_hero_id=None, against_hero_id=None,
                           significant=None, having=None, sort=None):
        """
        Totals in stats
        """
        data = {'account_id': account_id, 'limit': limit, 'offset': offset, 'win': win, 'patch': patch,
                'game_mode': game_mode, 'lobby_type': lobby_type, 'region': region, 'date': date,
                'lane_role': lane_role, 'hero_id': hero_id, 'is_radiant': is_radiant,
                'included_account_id': included_account_id, 'excluded_account_id': excluded_account_id,
                'with_hero_id': with_hero_id, 'against_hero_id': against_hero_id, 'significant': significant,
                'having': having, 'sort': sort, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/totals", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_players_counts(self, account_id=None, limit=None, offset=None, win=None, patch=None, game_mode=None,
                           lobby_type=None, region=None, date=None, lane_role=None, hero_id=None, is_radiant=None,
                           included_account_id=None, excluded_account_id=None, with_hero_id=None, against_hero_id=None,
                           significant=None, having=None, sort=None):
        """
        Counts in categories
        """
        data = {'account_id': account_id, 'limit': limit, 'offset': offset, 'win': win, 'patch': patch,
                'game_mode': game_mode, 'lobby_type': lobby_type, 'region': region, 'date': date,
                'lane_role': lane_role, 'hero_id': hero_id, 'is_radiant': is_radiant,
                'included_account_id': included_account_id, 'excluded_account_id': excluded_account_id,
                'with_hero_id': with_hero_id, 'against_hero_id': against_hero_id, 'significant': significant,
                'having': having, 'sort': sort, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/counts", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_players_histograms(self, account_id=None, limit=None, offset=None, win=None, patch=None, game_mode=None,
                               lobby_type=None, region=None, date=None, lane_role=None, hero_id=None, is_radiant=None,
                               included_account_id=None, excluded_account_id=None, with_hero_id=None,
                               against_hero_id=None, significant=None, having=None, sort=None, field=None):
        """
        Distribution of matches in a single stat
        """
        data = {'account_id': account_id, 'limit': limit, 'offset': offset, 'win': win, 'patch': patch,
                'game_mode': game_mode, 'lobby_type': lobby_type, 'region': region, 'date': date,
                'lane_role': lane_role, 'hero_id': hero_id, 'is_radiant': is_radiant,
                'included_account_id': included_account_id, 'excluded_account_id': excluded_account_id,
                'with_hero_id': with_hero_id, 'against_hero_id': against_hero_id, 'significant': significant,
                'having': having, 'sort': sort, 'field': field, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/histograms/{field}", header=DEFAULT_HEADERS,
                                data=data)
        return response.json()

    def get_players_wardmap(self, account_id=None, limit=None, offset=None, win=None, patch=None, game_mode=None,
                            lobby_type=None, region=None, date=None, lane_role=None, hero_id=None, is_radiant=None,
                            included_account_id=None, excluded_account_id=None, with_hero_id=None, against_hero_id=None,
                            significant=None, having=None, sort=None):
        """
        Wards placed in matches played
        """
        data = {'account_id': account_id, 'limit': limit, 'offset': offset, 'win': win, 'patch': patch,
                'game_mode': game_mode, 'lobby_type': lobby_type, 'region': region, 'date': date,
                'lane_role': lane_role, 'hero_id': hero_id, 'is_radiant': is_radiant,
                'included_account_id': included_account_id, 'excluded_account_id': excluded_account_id,
                'with_hero_id': with_hero_id, 'against_hero_id': against_hero_id, 'significant': significant,
                'having': having, 'sort': sort, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/wardmap", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_players_wordcloud(self, account_id=None, limit=None, offset=None, win=None, patch=None, game_mode=None,
                              lobby_type=None, region=None, date=None, lane_role=None, hero_id=None, is_radiant=None,
                              included_account_id=None, excluded_account_id=None, with_hero_id=None,
                              against_hero_id=None, significant=None, having=None, sort=None):
        """
        Words said/read in matches played
        """
        data = {'account_id': account_id, 'limit': limit, 'offset': offset, 'win': win, 'patch': patch,
                'game_mode': game_mode, 'lobby_type': lobby_type, 'region': region, 'date': date,
                'lane_role': lane_role, 'hero_id': hero_id, 'is_radiant': is_radiant,
                'included_account_id': included_account_id, 'excluded_account_id': excluded_account_id,
                'with_hero_id': with_hero_id, 'against_hero_id': against_hero_id, 'significant': significant,
                'having': having, 'sort': sort, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/wordcloud", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_players_ratings(self, account_id=None):
        """
        Player rating history
        """
        data = {'account_id': account_id, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/ratings", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_players_rankings(self, account_id=None):
        """
        Player hero rankings
        """
        data = {'account_id': account_id, }
        response = requests.get(f"{OPENDOTA_URL}/players/{account_id}/rankings", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def post_players_refresh(self, account_id=None):
        """
        Refresh player match history
        """
        data = {'account_id': account_id, }
        response = requests.post(f"{OPENDOTA_URL}/players/{account_id}/refresh", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Pro_players():
    def get_proPlayers(self):
        """
        Get list of pro players
        """
        data = {}
        response = requests.get(f"{OPENDOTA_URL}/proPlayers", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Pro_matches():
    def get_proMatches(self, less_than_match_id=None):
        """
        Get list of pro matches
        """
        data = {'less_than_match_id': less_than_match_id, }
        response = requests.get(f"{OPENDOTA_URL}/proMatches", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Public_matches():
    def get_publicMatches(self, mmr_ascending=None, mmr_descending=None, less_than_match_id=None):
        """
        Get list of randomly sampled public matches
        """
        data = {'mmr_ascending': mmr_ascending, 'mmr_descending': mmr_descending,
                'less_than_match_id': less_than_match_id, }
        response = requests.get(f"{OPENDOTA_URL}/publicMatches", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Parsed_matches():
    def get_parsedMatches(self, less_than_match_id=None):
        """
        Get list of parsed match IDs
        """
        data = {'less_than_match_id': less_than_match_id, }
        response = requests.get(f"{OPENDOTA_URL}/parsedMatches", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Explorer():
    def get_explorer(self, sql=None):
        """
        Submit arbitrary SQL queries to the database
        """
        data = {'sql': sql, }
        response = requests.get(f"{OPENDOTA_URL}/explorer", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Metadata():
    def get_metadata(self):
        """
        Site metadata
        """
        data = {}
        response = requests.get(f"{OPENDOTA_URL}/metadata", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Distributions():
    def get_distributions(self):
        """
        Distributions of MMR data by bracket and country
        """
        data = {}
        response = requests.get(f"{OPENDOTA_URL}/distributions", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Search():
    def get_search(self, q=None):
        """
        Search players by personaname.
        """
        data = {'q': q, }
        response = requests.get(f"{OPENDOTA_URL}/search", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Rankings():
    def get_rankings(self, hero_id=None):
        """
        Top players by hero
        """
        data = {'hero_id': hero_id, }
        response = requests.get(f"{OPENDOTA_URL}/rankings", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Benchmarks():
    def get_benchmarks(self, hero_id=None):
        """
        Benchmarks of average stat values for a hero
        """
        data = {'hero_id': hero_id, }
        response = requests.get(f"{OPENDOTA_URL}/benchmarks", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Status():
    def get_status(self):
        """
        Get current service statistics
        """
        data = {}
        response = requests.get(f"{OPENDOTA_URL}/status", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Health():
    def get_health(self):
        """
        Get service health data
        """
        data = {}
        response = requests.get(f"{OPENDOTA_URL}/health", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Request():
    def get_request(self, jobId=None):
        """
        Get parse request state
        """
        data = {'jobId': jobId, }
        response = requests.get(f"{OPENDOTA_URL}/request/{jobId}", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def post_request(self, match_id=None):
        """
        Submit a new parse request
        """
        data = {'match_id': match_id, }
        response = requests.post(f"{OPENDOTA_URL}/request/{match_id}", header=DEFAULT_HEADERS, data=data)
        return response.json()


class FindMatches():
    def get_findMatches(self, teamA=None, teamB=None):
        """
        Finds recent matches by heroes played
        """
        data = {'teamA': teamA, 'teamB': teamB, }
        response = requests.get(f"{OPENDOTA_URL}/findMatches", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Heroes():
    def get_heroes(self):
        """
        Get hero data
        """
        data = {}
        response = requests.get(f"{OPENDOTA_URL}/heroes", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_heroes_matches(self, hero_id=None):
        """
        Get recent matches with a hero
        """
        data = {'hero_id': hero_id, }
        response = requests.get(f"{OPENDOTA_URL}/heroes/{hero_id}/matches", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_heroes_matchups(self, hero_id=None):
        """
        Get results against other heroes for a hero
        """
        data = {'hero_id': hero_id, }
        response = requests.get(f"{OPENDOTA_URL}/heroes/{hero_id}/matchups", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_heroes_durations(self, hero_id=None):
        """
        Get hero performance over a range of match durations
        """
        data = {'hero_id': hero_id, }
        response = requests.get(f"{OPENDOTA_URL}/heroes/{hero_id}/durations", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_heroes_players(self, hero_id=None):
        """
        Get players who have played this hero
        """
        data = {'hero_id': hero_id, }
        response = requests.get(f"{OPENDOTA_URL}/heroes/{hero_id}/players", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_heroes_itemPopularity(self, hero_id=None):
        """
        Get item popularity of hero categoried by start, early, mid and late game, analyzed from professional games
        """
        data = {'hero_id': hero_id, }
        response = requests.get(f"{OPENDOTA_URL}/heroes/{hero_id}/itemPopularity", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Hero_stats():
    def get_heroStats(self):
        """
        Get stats about hero performance in recent matches
        """
        data = {}
        response = requests.get(f"{OPENDOTA_URL}/heroStats", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Leagues():
    def get_leagues(self):
        """
        Get league data
        """
        data = {}
        response = requests.get(f"{OPENDOTA_URL}/leagues", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_leagues(self, league_id=None):
        """
        Get data for a league
        """
        data = {'league_id': league_id, }
        response = requests.get(f"{OPENDOTA_URL}/leagues/{league_id}", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_leagues_matches(self, league_id=None):
        """
        Get matches for a team
        """
        data = {'league_id': league_id, }
        response = requests.get(f"{OPENDOTA_URL}/leagues/{league_id}/matches", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_leagues_teams(self, league_id=None):
        """
        Get teams for a league
        """
        data = {'league_id': league_id, }
        response = requests.get(f"{OPENDOTA_URL}/leagues/{league_id}/teams", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Teams():
    def get_teams(self, page=None):
        """
        Get team data
        """
        data = {'page': page, }
        response = requests.get(f"{OPENDOTA_URL}/teams", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_teams(self, team_id=None):
        """
        Get data for a team
        """
        data = {'team_id': team_id, }
        response = requests.get(f"{OPENDOTA_URL}/teams/{team_id}", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_teams_matches(self, team_id=None):
        """
        Get matches for a team
        """
        data = {'team_id': team_id, }
        response = requests.get(f"{OPENDOTA_URL}/teams/{team_id}/matches", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_teams_players(self, team_id=None):
        """
        Get players who have played for a team
        """
        data = {'team_id': team_id, }
        response = requests.get(f"{OPENDOTA_URL}/teams/{team_id}/players", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_teams_heroes(self, team_id=None):
        """
        Get heroes for a team
        """
        data = {'team_id': team_id, }
        response = requests.get(f"{OPENDOTA_URL}/teams/{team_id}/heroes", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Replays():
    def get_replays(self, match_id=None):
        """
        Get data to construct a replay URL with
        """
        data = {'match_id': match_id, }
        response = requests.get(f"{OPENDOTA_URL}/replays", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Records():
    def get_records(self, field=None):
        """
        Get top performances in a stat
        """
        data = {'field': field, }
        response = requests.get(f"{OPENDOTA_URL}/records/{field}", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Live():
    def get_live(self):
        """
        Get top currently ongoing live games
        """
        data = {}
        response = requests.get(f"{OPENDOTA_URL}/live", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Scenarios():
    def get_scenarios_itemTimings(self, item=None, hero_id=None):
        """
        Win rates for certain item timings on a hero for items that cost at least 1400 gold
        """
        data = {'item': item, 'hero_id': hero_id, }
        response = requests.get(f"{OPENDOTA_URL}/scenarios/itemTimings", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_scenarios_laneRoles(self, lane_role=None, hero_id=None):
        """
        Win rates for heroes in certain lane roles
        """
        data = {'lane_role': lane_role, 'hero_id': hero_id, }
        response = requests.get(f"{OPENDOTA_URL}/scenarios/laneRoles", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_scenarios_misc(self, scenario=None):
        """
        Miscellaneous team scenarios
        """
        data = {'scenario': scenario, }
        response = requests.get(f"{OPENDOTA_URL}/scenarios/misc", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Schema():
    def get_schema(self):
        """
        Get database schema
        """
        data = {}
        response = requests.get(f"{OPENDOTA_URL}/schema", header=DEFAULT_HEADERS, data=data)
        return response.json()


class Constants():
    def get_constants(self, resource=None):
        """
        Get static game data mirrored from the dotaconstants repository.
        """
        data = {'resource': resource, }
        response = requests.get(f"{OPENDOTA_URL}/constants/{resource}", header=DEFAULT_HEADERS, data=data)
        return response.json()

    def get_constants(self):
        """
        Gets an array of available resources.
        """
        data = {}
        response = requests.get(f"{OPENDOTA_URL}/constants", header=DEFAULT_HEADERS, data=data)
        return response.json()
