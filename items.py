range = xrange

ITEMS = [
    'Berry Juice',
    'Black Belt',
    'Black Glasses',
    'Charcoal',
    'Dragon Fang',
    'Hard Stone',
    'King\'s Rock',
    'Leftovers',
    'Light Ball',
    'Magnet',
    'Metal Coat',
    'Metal Powder',
    'Miracle Seed',
    'Mystic Water',
    'Never-Melt Ice',
    'Poison Barb',
    'Sharp Beak',
    'Silver Powder',
    'Soft Sand',
    'Spell Tag',
    'Stick',
    'Thick Club',
    'Twisted Spoon',
	'Choice Band',
    'Deep Sea Scale',
    'Deep Sea Tooth',
    'Oran Berry',
    'Silk Scarf',
    'Sitrus Berry',
    'Soul Dew',
	'Adamant Orb',
    'Apicot Berry',
    'Babiri Berry',
    'Belue Berry',
    'Black Sludge',
    'Charti Berry',
    'Chesto Berry',
    'Chilan Berry',
    'Choice Scarf',
    'Choice Specs',
    'Chople Berry',
    'Coba Berry',
    'Colbur Berry',
    'Custap Berry',
    'Draco Plate',
    'Dread Plate',
    'Durin Berry',
    'Earth Plate',
    'Enigma Berry',
    'Expert Belt',
    'Fist Plate',
    'Flame Orb',
    'Flame Plate',
    'Ganlon Berry',
    'Griseous Orb',
    'Haban Berry',
    'Icicle Plate',
    'Insect Plate',
    'Iron Ball',
    'Iron Plate',
    'Jaboca Berry',
    'Kasib Berry',
    'Kebia Berry',
    'Lagging Tail',
    'Lansat Berry',
    'Leppa Berry',
    'Liechi Berry',
    'Life Orb',
    'Lum Berry',
    'Lustrous Orb',
    'Macho Brace',
    'Meadow Plate',
    'Micle Berry',
    'Mind Plate',
    'Muscle Band',
    'Occa Berry',
    'Odd Incense',
    'Passho Berry',
    'Payapa Berry',
    'Petaya Berry',
    'Rawst Berry',
    'Razor Fang',
    'Rindo Berry',
    'Rock Incense',
    'Rose Incense',
    'Rowap Berry',
    'Salac Berry',
    'Sea Incense',
    'Shuca Berry',
    'Sky Plate',
    'Splash Plate',
    'Spooky Plate',
    'Starf Berry',
    'Stone Plate',
    'Tanga Berry',
    'Toxic Orb',
    'Toxic Plate',
    'Wacan Berry',
    'Watmel Berry',
    'Wave Incense',
    'Wise Glasses',
    'Yache Berry',
    'Zap Plate',
	'Air Balloon',
    'Eviolite',
    'Normal Gem',
	'Assault Vest',
    'Kee Berry',
    'Maranga Berry',
    'Pixie Plate',
    'Roseli Berry',
    'Safety Goggles',
	'Focus Sash',
]

MEGA_STONES = [
	'Abomasite',
	'Absolite',
	'Aerodactylite',
	'Aggronite',
	'Alakazite',
	'Altarianite',
	'Ampharoiste',
	'Audinite',
	'Banettite',
	'Beedrillite',
	'Blastoisinite',
	'Blazikenite',
	'Cameruptite',
	'Charizardite X',
	'Charizardite Y',
	'Diancite',
	'Galladite',
	'Garchompite',
	'Gardevoirite',
	'Gengarite',
	'Glalitite',
	'Gyaradosite',
	'Heracronite',
	'Houndoominite',
	'Kangaskhanite',
	'Latiasite',
	'Latiosite',
	'Lopunnite',
	'Lucarionite',
	'Manectite',
	'Mawilite',
	'Medichamite',
	'Metagrossite',
	'Mewtwonite X',
	'Mewtwonite Y',
	'Pidgeotite',
	'Pinsirite',
	'Sablenite',
	'Salamencite',
	'Sceptilite',
	'Scizorite',
	'Sharpedonite',
	'Slowbronite',
	'Steelixite',
	'Swampertite',
	'Tyranitarite',
	'Venusaurite'
]

ITEMS = ITEMS + MEGA_STONES
def get_item_boost_type(item):
	items = {}
	for i in range(len(ITEMS)):
		items.setdefault(ITEMS[i], None)
	items['Draco Plate'] = items['Dragon Fang'] = 'Dragon'
	items['Dread Plate'] = items['Black Glasses'] = 'Dark'
	items['Earth Plate'] = items['Soft Sand'] = 'Ground'
	items['Fist Plate'] = items['Black Belt'] = 'Fighting'
	items['Flame Plate'] = items['Charcoal'] = 'Fire'
	items['Icicle Plate'] = items['Never-Melt Ice'] = 'Ice'
	items['Insect Plate'] = items['Silver Powder'] = 'Bug'
	items['Iron Plate'] = items['Metal Coat'] = 'Steel'
	items['Meadow Plate'] = items['Rose Incense'] = items['Miracle Seed'] = 'Grass'
	items['Mind Plate'] = items['Odd Incense'] = items['Twisted Spoon'] = 'Psychic'
	items['Pixie Plate'] = 'Fairy'
	items['Sky Plate'] = items['Sharp Beak'] = 'Flying'
	items['Splash Plate'] = items['Sea Incense'] = items['Wave Incense'] = items['Mystic Water'] = 'Water'
	items['Spooky Plate'] = items['Spell Tag'] = 'Ghost'
	items['Stone Plate'] = items['Rock Incense'] = items['Hard Stone'] = 'Rock'
	items['Toxic Plate'] = items['Poison Barb'] = 'Poison'
	items['Zap Plate'] = items['Magnet'] = 'Electric'
	items['Silk Scarf'] = 'Normal'
	return items[item]

	
