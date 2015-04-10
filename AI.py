from pokemon import *
from calculator import get_ko_chance

class AI(object):
	def __init__(self, team_data): # def __init__(self, team_data, source)
		self.team = PokemonTeam.from_data(team_data)
		self.opp_team = PokemonTeam.from_data(open("opp.txt", 'r').read()) # get the names of each opponent pokemon
		self.field = {'weather' : None, 'terrain' : None} # hazards.. etc
		
	def update(self, source):
		pokemon.modify_stats(self.field) # this needs to be called at some point
		# update information
		
	def calculate_value(self):
		for pokemon in self.team():
			for move in pokemon.moves:
				if 'bp' in move.data:
					for opponent in self.opp_team():
						ko_chance = get_ko_chance(pokemon, opponent, move, self.field) 
						print pokemon.name, move.name, "VS", opponent.name, ko_chance
	
	