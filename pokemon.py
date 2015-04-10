from collections import OrderedDict
from pokedex import POKEDEX
from moves import MOVES
import math

pokemon_data_file = "pokemon_data.txt"
ignored = ['Shiny', 'IV', 'Happiness']
STATS_DICT =  OrderedDict([('HP', None), ('Atk', 0), ('Def', 1), ('SpA' , 2), ('SpD' , 3), ('Spe' , 4)])
NATURES = {
	"Hardy" : [1, 1, 1, 1, 1],
	"Lonely" : [1.1, .9, 1, 1, 1],
	"Brave" : [1.1, 1, 1, 1, .9],
	"Adamant" : [1.1, 1, .9, 1, 1],
	"Naughty" : [1.1, 1, 1, .9, 1],
	"Bold" : [.9, 1.1, 1, 1, 1],
	"Docile" : [1, 1, 1, 1, 1],
	"Relaxed" : [1, 1.1, 1, 1, .9],
	"Impish" : [1, 1.1, .9, 1, 1],
	"Lax" : [1, 1.1, 1, .9, 1],
	"Timid" : [.9, 1, 1, 1, 1.1],
	"Hasty" : [1, .9, 1, 1, 1.1],
	"Serious" : [1, 1, 1, 1, 1],
	"Jolly" : [1, 1, .9, 1, 1.1],
	"Naive" : [1, 1, 1, .9, 1.1],
	"Modest" : [.9, 1, 1.1, 1, 1],
	"Mild" : [1, .9, 1.1, 1, 1],
	"Quiet" : [1, 1, 1.1, 1, .9],
	"Bashful" : [1, 1, 1, 1, 1],
	"Rash" : [1, 1, 1.1, .9, 1],
	"Calm" : [.9, 1, 1, 1.1, 1],
	"Gentle" : [1, .9, 1, 1.1, 1], 
	"Sassy" : [1, 1, 1, 1.1, .9],
	"Careful" : [1, 1, .9, 1.1, 1],
	"Quirky" : [1, 1, 1, 1, 1]
}
TYPES = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

class Move(object):
	def __init__(self, move_data, move_name):
		self.name = move_name
		self.data = move_data
		if 'category' not in self.data:
			self.category = 'status'
		else:
			self.category = self.data['category']
			self.bp = self.data['bp']
			self.type = self.data['type']
		
		self.hits = 1
		
		
class Pokemon(object):
	def __init__(self, name, item, ability, nature, evs, moves):
		self.name = name
		self.item = item
		self.ability = ability
		self.nature = nature
		self.level = 100
		self.evs = dict(zip(STATS_DICT, [int(evs[key]) for key in evs]))
		self.moves = [Move(MOVES[move_name], move_name) for move_name in moves]
		self.stats = dict(zip(STATS_DICT, [None]*6))
		
		data = POKEDEX[self.name]
		self.type = [data[key] for key in data if key == 't1' or key == 't2']
		self.base_stats = data['bs']
		self.raw_stats = {}
		self.weight = data['w']
		
		self.boosts = {'Atk' : 0, 'Def' : 0, 'SpA' : 0, 'SpD': 0, 'Spe' : 0}
		self.status = 'Healthy'
		self.toxic_counter = 0
		self.calculate_stats()
		self.current_HP = self.raw_stats['HP']
		
	def calculate_stats(self):
		for stat in self.base_stats:
			if stat == 'HP':
				try:
					self.raw_stats[stat] = int(31 + 2*self.base_stats[stat] + self.evs[stat]/4 + 10 + 100)
				except KeyError: # in case of no EVS
					self.raw_stats[stat] = int(31 + 2*self.base_stats[stat] + 10 + 100)
			elif stat != 'sl':
				try:
					self.raw_stats[stat] = int((31 + 2*self.base_stats[stat] + self.evs[stat]/4 + 5) * NATURES[self.nature][STATS_DICT[stat]])
				except KeyError:
					self.raw_stats[stat] = int((31 + 2*self.base_stats[stat] +  5) * NATURES[self.nature][STATS_DICT[stat]])
		print self.name, self.raw_stats
			
	def modify_stats(self, field):
		for _stat in self.raw_stats:
			if _stat is not 'HP':
				stat = self.raw_stats[_stat]
				boost = self.boosts[_stat]
				self.stats[_stat] = stat * (2 + mod) // 2 if mod > 0 else stat * 2 // (2 - mod) if mod < 0 else stat 
				if _stat is 'Spe':
					if self.item is "Choice Scarf":
						speed = math.floor(self.stats['Spe'] * 1.5)
					elif self.item is "Macho Brace" or self.item is "Iron Ball":
						speed = self.stats['Spe'] // 2
					if (self.ability is "Chlorophyll" and field['weather'] is "Sun") or \
					(self.ability is "Sand Rush" and field['weather'] is "Sand") or \
					(self.ability is "Swift Swim" and field['weather'] is "Rain"):
						speed *= 2
					self.stats['Spe'] = speed
		
		# get the base stats from the file
		
	def get_move_data(self):
		pass
		
	
	
class PokemonTeam(object):
	def __init__(self, team_data=None):
		self.team = []
		if team_data:
			for i in range(1, 7):
				mon_data = team_data[8*(i-1):(8*i)]
				self.add_pokemon(mon_data)
	
	def __call__(self):
		return self.team
		
	def add_pokemon(self, mon_data):
		try:
			name = mon_data[0].split()[0]
			item = " ".join(mon_data[0].split()[2:])
			ability = " ".join(mon_data[1].split()[1:])
			nature = mon_data[3].split()[0]
			ev_data = [d for d in mon_data[2].split() if d != '/'] 
			evs = dict([reversed(ev_data[i:i+2]) for i in range(1, len(ev_data), 2)])
			moves = [" ".join(line[1:]).replace("[", "").replace("]", "") for line in [mon_data[i].split() for i in range(4,8)]]
			self.team.append(Pokemon(name, item, ability, nature, evs, moves))
		except IndexError:
			pass
			# alternative method
			
	@classmethod
	def from_data(cls, team_data):
		data = [line for line in team_data.splitlines() if (line != '' and all([ignored[i] not in line for i in range(len(ignored))]))]
		return cls(data)
			
	

	

def damage_calc(damage, player, opponent):
	pass
	