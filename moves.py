from __future__ import division

MOVES_RBY = {
    '(No Move)': {
        'bp': 0,
        'type': 'Normal',
        'category': 'Physical'
    },
    'Acid': {
        'bp': 40,
        'type': 'Poison'
    },
    'Bind': {
        'bp': 15,
        'type': 'Normal'
    },
    'Blizzard': {
        'bp': 120,
        'type': 'Ice',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSpread': True
    },
    'Body Slam': {
        'bp': 85,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'BubbleBeam': {
        'bp': 65,
        'type': 'Water'
    },
    'Clamp': {
        'bp': 35,
        'type': 'Water'
    },
    'Crabhammer': {
        'bp': 90,
        'type': 'Water',
        'category': 'Physical',
        'makesContact': True,
        'alwaysCrit': True
    },
    'Dig': {
        'bp': 100,
        'type': 'Ground'
    },
    'Double Kick': {
        'bp': 30,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'isTwoHit': True
    },
    'Double-Edge': {
        'bp': 100,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True,
        'recoil': 1/3
    },
    'Drill Peck': {
        'bp': 80,
        'type': 'Flying',
        'category': 'Physical',
        'makesContact': True
    },
    'Earthquake': {
        'bp': 100,
        'type': 'Ground',
        'category': 'Physical',
        'isSpread': True
    },
    'Explosion': {
        'bp': 170,
        'type': 'Normal',
        'category': 'Physical',
        'isSpread': True
		# Extra: Kills user
    },
    'Fire Blast': {
        'bp': 120,
        'type': 'Fire',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Fire Punch': {
        'bp': 75,
        'type': 'Fire',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'isPunch': True
    },
    'Fire Spin': {
        'bp': 15,
        'type': 'Fire'
    },
    'Flamethrower': {
        'bp': 95,
        'type': 'Fire',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Hi Jump Kick': {
        'bp': 85,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'recoil': True
		# Extra: If move misses, user loses half HP rounded down
    },
    'Hydro Pump': {
        'bp': 120,
        'type': 'Water',
        'category': 'Special'
    },
    'Hyper Beam': {
        'bp': 150,
        'type': 'Normal',
        'category': 'Special'
    },
    'Ice Beam': {
        'bp': 95,
        'type': 'Ice',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Ice Punch': {
        'bp': 75,
        'type': 'Ice',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'isPunch': True
    },
    'Mega Drain': {
        'bp': 40,
        'type': 'Grass'
    },
    'Night Shade': {
        'bp': 100,
        'type': 'Ghost',
        'category': 'Special'
    },
    'Pin Missile': {
        'bp': 14,
        'type': 'Bug',
        'category': 'Physical',
        'isMultiHit': True
    },
    'Psychic': {
        'bp': 90,
        'type': 'Psychic',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Quick Attack': {
        'bp': 40,
        'type': 'Normal',
        'category': 'Physical',
		'priority' : 1,
        'makesContact': True
    },
    'Razor Leaf': {
        'bp': 55,
        'type': 'Grass',
        'category': 'Special',
        'alwaysCrit': True
    },
    'Rock Slide': {
        'bp': 75,
        'type': 'Rock',
        'category': 'Physical',
        'hasSecondaryEffect': True,
        'isSpread': True
    },
    'Seismic Toss': {
        'bp': 100,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True
    },
    'Selfdestruct': {
        'bp': 130,
        'type': 'Normal',
        'category': 'Physical',
        'isSpread': True
		# Extra: Kills user
    },
    'Sky Attack': {
        'bp': 140,
        'type': 'Flying',
        'category': 'Physical',
        'hasSecondaryEffect': True
    },
    'Slash': {
        'bp': 70,
        'type': 'Normal',
        'alwaysCrit': True
    },
    'Sludge': {
        'bp': 65,
        'type': 'Poison'
    },
    'Submission': {
        'bp': 80,
        'type': 'Fighting',
		'recoil' : .25
    },
    'Surf': {
        'bp': 95,
        'type': 'Water',
        'category': 'Special',
        'isSpread': True
    },
    'Tackle': {
        'bp': 35,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True
    },
    'Thunder': {
        'bp': 120,
        'type': 'Electric',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'ThunderPunch': {
        'bp': 75,
        'type': 'Electric',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'isPunch': True
    },
    'Thunderbolt': {
        'bp': 95,
        'type': 'Electric',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Twineedle': {
        'bp': 25,
        'type': 'Bug',
        'isTwoHit': True
    },
    'Wrap': {
        'bp': 15,
        'type': 'Normal'
    }
};

MOVES_GSC = {
    'Aeroblast': {
        'bp': 100,
        'type': 'Flying',
        'category': 'Special'
    },
    'AncientPower': {
        'bp': 60,
        'type': 'Rock',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Bite': {
        'bp': 60,
        'type': 'Dark',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'isBite': True
    },
    'Crabhammer': { 'alwaysCrit': False },
    'Cross Chop': {
        'bp': 100,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True
    },
    'Crunch': {
        'bp': 80,
        'type': 'Dark',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'isBite': True
    },
    'Double-Edge': { 'bp': 120 },
    'DynamicPunch': {
        'bp': 100,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'isPunch': True
		# Extra: Always Confuses
    },
    'Explosion': { 'bp': 250 },
    'ExtremeSpeed': {
        'bp': 80,
        'type': 'Normal',
        'category': 'Physical',
		'priority' : 2,
        'makesContact': True
    },
    'Faint Attack': {
        'bp': 60,
        'type': 'Dark',
        'category': 'Physical',
        'makesContact': True
    },
    'Flail': {
        'bp': 1,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True
    },
    'Flame Wheel': {
        'bp': 60,
        'type': 'Fire',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Frustration': {
        'bp': 102,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True
    },
    'Giga Drain': {
        'bp': 60,
        'type': 'Grass',
        'category': 'Special',
		'restoreHalfDamage' : True
    },
    'Headbutt': {
        'bp': 70,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Hidden Power Bug': {
        'bp': 70,
        'type': 'Bug',
        'category': 'Special'
    },
    'Hidden Power Dark': {
        'bp': 70,
        'type': 'Dark',
        'category': 'Special'
    },
    'Hidden Power Dragon': {
        'bp': 70,
        'type': 'Dragon',
        'category': 'Special'
    },
    'Hidden Power Electric': {
        'bp': 70,
        'type': 'Electric',
        'category': 'Special'
    },
    'Hidden Power Fighting': {
        'bp': 70,
        'type': 'Fighting',
        'category': 'Special'
    },
    'Hidden Power Fire': {
        'bp': 70,
        'type': 'Fire',
        'category': 'Special'
    },
    'Hidden Power Flying': {
        'bp': 70,
        'type': 'Flying',
        'category': 'Special'
    },
    'Hidden Power Ghost': {
        'bp': 70,
        'type': 'Ghost',
        'category': 'Special'
    },
    'Hidden Power Grass': {
        'bp': 70,
        'type': 'Grass',
        'category': 'Special'
    },
    'Hidden Power Ground': {
        'bp': 70,
        'type': 'Ground',
        'category': 'Special'
    },
    'Hidden Power Ice': {
        'bp': 70,
        'type': 'Ice',
        'category': 'Special'
    },
    'Hidden Power Poison': {
        'bp': 70,
        'type': 'Poison',
        'category': 'Special'
    },
    'Hidden Power Psychic': {
        'bp': 70,
        'type': 'Psychic',
        'category': 'Special'
    },
    'Hidden Power Rock': {
        'bp': 70,
        'type': 'Rock',
        'category': 'Special'
    },
    'Hidden Power Steel': {
        'bp': 70,
        'type': 'Steel',
        'category': 'Special'
    },
    'Hidden Power Water': {
        'bp': 70,
        'type': 'Water',
        'category': 'Special'
    },
    'Icy Wind': {
        'bp': 55,
        'type': 'Ice',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSpread': True,
		'modOppStat' : {'Spe' : 2/3}
    },
    'Iron Tail': {
        'bp': 100,
        'type': 'Steel',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Mach Punch': {
        'bp': 40,
        'type': 'Fighting',
        'category': 'Physical',
		'priority' : 1,
        'makesContact': True,
        'isPunch': True
    },
    'Megahorn': {
        'bp': 120,
        'type': 'Bug',
        'category': 'Physical',
        'makesContact': True
    },
    'Pursuit': {
        'bp': 40,
        'type': 'Dark',
        'category': 'Physical',
        'makesContact': True
		# Extra: if the opponent switches out, deal double damage
    },
    'Rapid Spin': {
        'bp': 20,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True
		# Extra: Removes entry hazards
    },
    'Razor Leaf': { 'alwaysCrit': False },
    'Return': {
        'bp': 102,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True
    },
    'Reversal': {
        'bp': 1,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True
    },
    'Sacred Fire': {
        'bp': 100,
        'type': 'Fire',
        'category': 'Physical',
        'hasSecondaryEffect': True
    },
    'Selfdestruct': { 'bp': 200 },
    'Shadow Ball': {
        'bp': 80,
        'type': 'Ghost',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isBullet': True
    },
    'Sludge Bomb': {
        'bp': 90,
        'type': 'Poison',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isBullet': True
    },
    'SolarBeam': {
        'bp': 120,
        'type': 'Grass',
        'category': 'Special'
    },
    'Steel Wing': {
        'bp': 70,
        'type': 'Steel',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Thief': {
        'bp': 40,
        'type': 'Dark',
        'category': 'Physical',
        'makesContact': True
    },
    'Zap Cannon': {
        'bp': 100,
        'type': 'Electric',
        'category': 'Special',
        'hasSecondaryEffect': True
    }
}

MOVES_GSC.update(MOVES_RBY)

del MOVES_GSC['Acid'];
del MOVES_GSC['Bind'];
del MOVES_GSC['Clamp'];
del MOVES_GSC['Dig'];
del MOVES_GSC['Fire Spin'];
del MOVES_GSC['Mega Drain'];
del MOVES_GSC['Slash'];
del MOVES_GSC['Sludge'];
del MOVES_GSC['Wrap'];

MOVES_ADV = {
    'Aerial Ace': {
        'bp': 60,
        'type': 'Flying',
        'category': 'Physical',
        'makesContact': True
    },
    'Air Cutter': {
        'bp': 55,
        'type': 'Flying',
        'category': 'Special',
        'isSpread': True
    },
    'Blaze Kick': {
        'bp': 85,
        'type': 'Fire',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Bonemerang': {
        'bp': 50,
        'type': 'Ground',
        'category': 'Physical',
        'isTwoHit': True
    },
    'Bounce': {
        'bp': 85,
        'type': 'Flying',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
		# Extra: disappears first turn, reappears second turn
    },
    'Brick Break': {
        'bp': 75,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True
    },
    'Doom Desire': {
        'bp': 120,
        'type': 'Steel',
        'category': 'Special'
    },
    'Dragon Claw': {
        'bp': 80,
        'type': 'Dragon',
        'category': 'Physical',
        'makesContact': True
    },
    'Eruption': {
        'bp': 150,
        'type': 'Fire',
        'category': 'Special',
        'isSpread': True
		# Extra: Damage based on user HP
    },
    'Extrasensory': {
        'bp': 80,
        'type': 'Psychic',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Facade': {
        'bp': 70,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True
		# Extra: Double damage if burned poisoned, or paralyzed
    },
    'Fake Out': {
        'bp': 40,
        'type': 'Normal',
        'category': 'Physical',
		'priority' : 3,
        'makesContact': True,
        'hasSecondaryEffect': True
		# Extra: only works on first turn, always flinches
    },
    'Focus Punch': {
        'bp': 150,
        'type': 'Fighting',
        'category': 'Physical',
		'priority' : -3,
        'makesContact': True,
        'isPunch': True
		# Extra: Fails if user is hit before it lands, unless behind a sub
    },
    'Heat Wave': {
        'bp': 100,
        'type': 'Fire',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSpread': True
    },
    'Knock Off': {
        'bp': 20,
        'type': 'Dark',
        'category': 'Physical',
        'makesContact': True
		# Extra: deals double damage if opponent has an item, removes it
    },
    'Leaf Blade': {
        'bp': 70,
        'type': 'Grass',
        'category': 'Physical',
        'makesContact': True
    },
    'Low Kick': {
        'bp': 1,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True
    },
    'Meteor Mash': {
        'bp': 100,
        'type': 'Steel',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'isPunch': True
    },
    'Muddy Water': {
        'bp': 95,
        'type': 'Water',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSpread': True
    },
    'Overheat': {
        'bp': 140,
        'type': 'Fire',
        'category': 'Special',
		'modUserStat' : {'SpA' : .5}
    },
    'Poison Fang': {
        'bp': 50,
        'type': 'Poison',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'isBite': True
    },
    'Psycho Boost': {
        'bp': 140,
        'type': 'Psychic',
        'category': 'Special'
    },
    'Revenge': {
        'bp': 60,
        'type': 'Fighting',
        'category': 'Physical',
		'priority' : -4,
        'makesContact': True,
		'doublesIfHitFirst' : True
		# doublesIfHitFirst: Revenge, Avalanche, Payback
    },
    'Rock Blast': {
        'bp': 25,
        'type': 'Rock',
        'category': 'Physical',
        'isMultiHit': True
    },
    'Rock Tomb': {
        'bp': 50,
        'type': 'Rock',
        'category': 'Physical',
        'hasSecondaryEffect': True
    },
    'Shadow Punch': {
        'bp': 60,
        'type': 'Ghost',
        'category': 'Physical',
        'makesContact': True,
        'isPunch': True
    },
    'Shock Wave': {
        'bp': 60,
        'type': 'Electric',
        'category': 'Special'
    },
    'Signal Beam': {
        'bp': 75,
        'type': 'Bug',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Sky Uppercut': {
        'bp': 85,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'isPunch': True
    },
    'Spark': {
        'bp': 65,
        'type': 'Electric',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Superpower': {
        'bp': 120,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
		'modUserStat' : {'Atk' : 2/3, 'Def' : 2/3}
    },
    'Volt Tackle': {
        'bp': 120,
        'type': 'Electric',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'recoil': 1/3
    },
    'Water Pulse': {
        'bp': 60,
        'type': 'Water',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isPulse': True
    },
    'Water Spout': {
        'bp': 150,
        'type': 'Water',
        'category': 'Special',
        'isSpread': True
		# Extra: Damage based on User HP
    },
    'Weather Ball': {
        'bp': 50,
        'type': 'Normal',
        'category': 'Special',
        'isBullet': True
		# Extra: Changes type based on the weather
    }
}

MOVES_ADV.update(MOVES_GSC)

del MOVES_ADV['BubbleBeam'];
del MOVES_ADV['Submission'];

MOVES_DPP = {
    'Air Slash': {
        'bp': 75,
        'type': 'Flying',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Aqua Jet': {
        'bp': 40,
        'type': 'Water',
        'category': 'Physical',
        'priority' : 1,
        'makesContact': True
    },
    'Aqua Tail': {
        'bp': 90,
        'type': 'Water',
        'category': 'Physical',
        'makesContact': True
    },
    'Assurance': {
        'bp': 50,
        'type': 'Dark',
        'category': 'Physical',
        'makesContact': True
		# Extra: Power doubles if opponent has already taken damage this turn
    },
    'Aura Sphere': {
        'bp': 90,
        'type': 'Fighting',
        'category': 'Special',
        'isBullet': True,
        'isPulse': True
    },
    'Avalanche': {
        'bp': 120,
        'type': 'Ice',
        'category': 'Physical',
		'priority' : -4,
        'makesContact': True,
		'doublesIfHitFirst' : True
    },
    'Brave Bird': {
        'bp': 120,
        'type': 'Flying',
        'category': 'Physical',
        'makesContact': True,
        'recoil': 1/3
    },
    'Bug Bite': {
        'bp': 60,
        'type': 'Bug',
        'category': 'Physical',
        'makesContact': True
    },
    'Bug Buzz': {
        'bp': 90,
        'type': 'Bug',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSound': True
    },
    'Bullet Punch': {
        'bp': 40,
        'type': 'Steel',
        'category': 'Physical',
		'priority' : 1,
        'makesContact': True,
        'isPunch': True
    },
    'Charge Beam': {
        'bp': 50,
        'type': 'Electric',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Chatter': {
        'bp': 60,
        'type': 'Flying',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSound': True
		# Extra: Always Confuses
    },
    'Close Combat': {
        'bp': 120,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
		'modUserStat' : {'Def' : 2/3, 'SpD' : 2/3}
    },
    'Cross Poison': {
        'bp': 70,
        'type': 'Poison',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Dark Pulse': {
        'bp': 80,
        'type': 'Dark',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isPulse': True
    },
    'Discharge': {
        'bp': 80,
        'type': 'Electric',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSpread': True
    },
    'Double Hit': {
        'bp': 35,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True,
        'isTwoHit': True
    },
    'Draco Meteor': {
        'bp': 140,
        'type': 'Dragon',
        'category': 'Special',
		'modUserStat' : {'SpA' : .5}
    },
    'Dragon Pulse': {
        'bp': 90,
        'type': 'Dragon',
        'category': 'Special',
        'isPulse': True
    },
    'Dragon Rush': {
        'bp': 100,
        'type': 'Dragon',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Drain Punch': {
        'bp': 60,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'isPunch': True,
		'restoreHalfDamage' : True
    },
    'Earth Power': {
        'bp': 90,
        'type': 'Ground',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Energy Ball': {
        'bp': 80,
        'type': 'Grass',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isBullet': True
    },
    'Fire Fang': {
        'bp': 65,
        'type': 'Fire',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'isBite': True
    },
    'Flare Blitz': {
        'bp': 120,
        'type': 'Fire',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'recoil': 1/3
    },
    'Flash Cannon': {
        'bp': 80,
        'type': 'Steel',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Fling': {
        'bp': 1,
        'type': 'Dark',
        'category': 'Physical'
    },
    'Focus Blast': {
        'bp': 120,
        'type': 'Fighting',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isBullet': True
    },
    'Force Palm': {
        'bp': 60,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Giga Impact': {
        'bp': 150,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True
    },
    'Grass Knot': {
        'bp': 1,
        'type': 'Grass',
        'category': 'Special',
        'makesContact': True
    },
    'Gunk Shot': {
        'bp': 120,
        'type': 'Poison',
        'category': 'Physical',
        'hasSecondaryEffect': True
    },
    'Gyro Ball': {
        'bp': 1,
        'type': 'Steel',
        'category': 'Physical',
        'makesContact': True,
        'isBullet': True
		# Extra: damage based on weight
    },
    'Hammer Arm': {
        'bp': 100,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'isPunch': True,
		'modUserStat' : {'Spe' : 2/3}
    },
    'Head Smash': {
        'bp': 150,
        'type': 'Rock',
        'category': 'Physical',
        'makesContact': True,
        'recoil': 1/2
    },
    'Hi Jump Kick': { 'bp': 100 },
    'Hyper Voice': {
        'bp': 90,
        'type': 'Normal',
        'category': 'Special',
        'isSound': True,
        'isSpread': True
    },
    'Ice Fang': {
        'bp': 65,
        'type': 'Ice',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'isBite': True
    },
    'Ice Shard': {
        'bp': 40,
        'type': 'Ice',
        'category': 'Physical',
		'priority' : 1
    },
    'Iron Head': {
        'bp': 80,
        'type': 'Steel',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Judgment': {
        'bp': 100,
        'type': 'Normal',
        'category': 'Special'
    },
    'Jump Kick': {
        'bp': 85,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'recoil': True
		# Extra: If move misses, user loses half HP rounded down
    },
    'Lava Plume': {
        'bp': 80,
        'type': 'Fire',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSpread': True
    },
    'Leaf Blade': { 'bp': 90 },
    'Leaf Storm': {
        'bp': 140,
        'type': 'Grass',
        'category': 'Special',
		'modUserStat' : {'SpA' : .5}
    },
    'Magma Storm': {
        'bp': 120,
        'type': 'Fire',
        'category': 'Special'
		# Extra: Traps Opponent
    },
    'Natural Gift': {
        'bp': 1,
        'type': 'Normal',
        'category': 'Physical'
    },
    'Nature Power': {
        'bp': 80,
        'type': 'Normal',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Night Slash': {
        'bp': 70,
        'type': 'Dark',
        'category': 'Physical',
        'makesContact': True
    },
    'Outrage': {
        'bp': 120,
        'type': 'Dragon',
        'category': 'Physical',
        'makesContact': True,
		'multiTurn' : True
    },
    'Payback': {
        'bp': 50,
        'type': 'Dark',
        'category': 'Physical',
        'makesContact': True,
		'doublesIfHitFirst' : True
		# Extra: Power doubles if user was attacked first(same as Revenge)
    },
    'Pluck': {
        'bp': 60,
        'type': 'Flying',
        'category': 'Physical',
        'makesContact': True
    },
    'Poison Jab': {
        'bp': 80,
        'type': 'Poison',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Power Gem': {
        'bp': 70,
        'type': 'Rock',
        'category': 'Special'
    },
    'Power Whip': {
        'bp': 120,
        'type': 'Grass',
        'category': 'Physical',
        'makesContact': True
    },
    'Psycho Cut': {
        'bp': 70,
        'type': 'Psychic',
        'category': 'Physical'
    },
    'Punishment': {
        'bp': 60,
        'type': 'Dark',
        'category': 'Physical',
        'makesContact': True
    },
    'Rock Climb': {
        'bp': 90,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Rock Smash': {
        'bp': 40,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Seed Bomb': {
        'bp': 80,
        'type': 'Grass',
        'category': 'Physical',
        'isBullet': True
    },
    'Seed Flare': {
        'bp': 120,
        'type': 'Grass',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Shadow Claw': {
        'bp': 70,
        'type': 'Ghost',
        'category': 'Physical',
        'makesContact': True
    },
    'Shadow Force': {
        'bp': 120,
        'type': 'Ghost',
        'category': 'Physical',
        'makesContact': True
    },
    'Shadow Sneak': {
        'bp': 40,
        'type': 'Ghost',
        'category': 'Physical',
		'priority' : 1,
        'makesContact': True
    },
    'Spacial Rend': {
        'bp': 100,
        'type': 'Dragon',
        'category': 'Special'
    },
    'Stone Edge': {
        'bp': 100,
        'type': 'Rock',
        'category': 'Physical'
    },
    'Sucker Punch': {
        'bp': 80,
        'type': 'Dark',
        'category': 'Physical',
		'priority' : 2,
        'makesContact': True
		# Extra: Fails if opponent uses an attack or a move with a priority of 3 or higher
    },
    'Swift': {
        'bp': 60,
        'type': 'Normal',
        'category': 'Special',
        'isSpread': True
    },
    'Thunder Fang': {
        'bp': 65,
        'type': 'Electric',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'isBite': True
    },
    'Tri Attack': {
        'bp': 80,
        'type': 'Normal',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'U-turn': {
        'bp': 70,
        'type': 'Bug',
        'category': 'Physical',
        'makesContact': True
		# Extra: User Switches out immediately after attacking
    },
    'Vacuum Wave': {
        'bp': 40,
        'type': 'Fighting',
        'category': 'Special',
		'priority' : 1
    },
    'Wake-Up Slap': {
        'bp': 60,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True
		# Extra: power doubles if opponent is asleep, but wakes it up
    },
    'Waterfall': {
        'bp': 80,
        'type': 'Water',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Wood Hammer': {
        'bp': 120,
        'type': 'Grass',
        'category': 'Physical',
        'makesContact': True,
        'recoil': 1/3
    },
    'X-Scissor': {
        'bp': 80,
        'type': 'Bug',
        'category': 'Physical',
        'makesContact': True
    },
    'Zen Headbutt': {
        'bp': 80,
        'type': 'Psychic',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    }
}

MOVES_DPP.update(MOVES_ADV)

del MOVES_DPP['Razor Leaf'];
del MOVES_DPP['Twineedle'];
del MOVES_DPP['Zap Cannon'];

MOVES_BW = {
    'Acid Spray': {
        'bp': 40,
        'type': 'Poison',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isBullet': True
    },
    'Acrobatics': {
        'bp': 55,
        'type': 'Flying',
        'category': 'Physical',
        'makesContact': True
		# Extra: Doubles damage if user is no holding an item
    },
    'Attack Order': {
        'bp': 90,
        'type': 'Bug',
        'category': 'Physical'
    },
    'Blue Flare': {
        'bp': 130,
        'type': 'Fire',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Bolt Strike': {
        'bp': 130,
        'type': 'Electric',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Bulldoze': {
        'bp': 60,
        'type': 'Ground',
        'category': 'Physical',
        'hasSecondaryEffect': True,
        'isSpread': True,
		'modOppStat' : {'Spe' : 2/3}
    },
    'Bullet Seed': {
        'bp': 25,
        'type': 'Grass',
        'category': 'Physical',
        'isMultiHit': True,
        'isBullet': True
    },
    'Circle Throw': {
        'bp': 60,
        'type': 'Fighting',
        'category': 'Physical',
		'priority' : -6,
		'phazing' : True,
        'makesContact': True
    },
    'Clear Smog': {
        'bp': 50,
        'type': 'Poison',
        'category': 'Special'
		# Extra: removes the target's stat changes
    },
    'Doom Desire': { 'bp': 140 },
    'Dragon Tail': {
        'bp': 60,
        'type': 'Dragon',
        'category': 'Physical',
		'priority' : -6,
		'phasing' : True,
        'makesContact': True
    },
    'Drain Punch': { 'bp': 75 },
    'Drill Run': {
        'bp': 80,
        'type': 'Ground',
        'category': 'Physical',
        'makesContact': True
    },
    'Dual Chop': {
        'bp': 40,
        'type': 'Dragon',
        'category': 'Physical',
        'makesContact': True,
        'isTwoHit': True
    },
    'Electro Ball': {
        'bp': 1,
        'type': 'Electric',
        'category': 'Special',
        'isBullet': True
    },
    'Feint': {
        'bp': 30,
        'type': 'Normal',
        'category': 'Physical',
		'priority' : 2
		# Extra: goes through protect
    },
    'Fiery Dance': {
        'bp': 80,
        'type': 'Fire',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Flame Charge': {
        'bp': 50,
        'type': 'Fire',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
		'modUserStat' :  {'Spe': 3/2}
    }, # [key for key in MOVES['Flame Charge']['modUserStat']] 
    'Foul Play': {
        'bp': 95,
        'type': 'Dark',
        'category': 'Physical',
        'makesContact': True
		# Extra: Deals damage based on opponents Attack Stat
    },
    'Freeze Shock': {
        'bp': 140,
        'type': 'Ice',
        'category': 'Physical',
        'hasSecondaryEffect': True
    },
    'Frost Breath': {
        'bp': 40,
        'type': 'Ice',
        'category': 'Special',
        'alwaysCrit': True
    },
    'Fusion Bolt': {
        'bp': 100,
        'type': 'Electric',
        'category': 'Physical'
    },
    'Fusion Flare': {
        'bp': 100,
        'type': 'Fire',
        'category': 'Special'
    },
    'Gear Grind': {
        'bp': 50,
        'type': 'Steel',
        'category': 'Physical',
        'isTwoHit': True
    },
    'Giga Drain': { 'bp': 75 },
    'Glaciate': {
        'bp': 65,
        'type': 'Ice',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSpread': True,
		'modOppStat' : {'Spe' : 2/3}
    },
    'Head Charge': {
        'bp': 120,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True,
        'recoil': 1/4
    },
    'Heavy Slam': {
        'bp': 1,
        'type': 'Steel',
        'category': 'Physical',
        'makesContact': True
    },
    'Hex': {
        'bp': 50,
        'type': 'Ghost',
        'category': 'Special' 
		# Extra: Double damage if opponent has a status condition 
    },
    'Hi Jump Kick': { 'bp': 130 },
    'Horn Leech': {
        'bp': 75,
        'type': 'Grass',
        'category': 'Physical',
        'makesContact': True,
		'restoreHalfDamagme' : True
    },
    'Hurricane': {
        'bp': 120,
        'type': 'Flying',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Icicle Crash': {
        'bp': 85,
        'type': 'Ice',
        'category': 'Physical',
        'hasSecondaryEffect': True
    },
    'Icicle Spear': {
        'bp': 25,
        'type': 'Ice',
        'category': 'Physical',
        'isMultiHit': True
    },
    'Incinerate': {
        'bp': 30,
        'type': 'Fire',
        'category': 'Special',
        'isSpread': True
    },
    'Jump Kick': { 'bp': 100 },
    'Low Sweep': {
        'bp': 60,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Nature Power': {
        'bp': 100,
        'type': 'Ground',
        'category': 'Physical',
        'hasSecondaryEffect': False,
        'isSpread': True
    },
    'Night Daze': {
        'bp': 85,
        'type': 'Dark',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Petal Dance': {
        'bp': 120,
        'type': 'Grass',
        'category': 'Special',
        'makesContact': True,
		'multiTurn' : True
    },
    'Psyshock': {
        'bp': 80,
        'type': 'Psychic',
        'category': 'Special',
        'dealsPhysicalDamage': True
    },
    'Psystrike': {
        'bp': 100,
        'type': 'Psychic',
        'category': 'Special',
        'dealsPhysicalDamage': True
    },
    'Razor Shell': {
        'bp': 75,
        'type': 'Water',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Relic Song': {
        'bp': 75,
        'type': 'Normal',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSound': True,
        'isSpread': True
		# Extra: Transforms Meloetta
    },
    'Retaliate': {
        'bp': 70,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True
		# Extra: Double damage if a teammate fainted on the last turn 
    },
    'Sacred Sword': {
        'bp': 90,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'ignoresDefenseBoosts': True
    },
    'Scald': {
        'bp': 80,
        'type': 'Water',
        'category': 'Special',
        'hasSecondaryEffect': True
		# Extra: Spammable
    },
    'Searing Shot': {
        'bp': 100,
        'type': 'Fire',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSpread': True
    },
    'Secret Sword': {
        'bp': 85,
        'type': 'Fighting',
        'category': 'Special',
        'dealsPhysicalDamage': True
    },
    'Sludge Wave': {
        'bp': 95,
        'type': 'Poison',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSpread': True
    },
    'Smack Down': {
        'bp': 50,
        'type': 'Rock',
        'category': 'Physical'
    },
    'Snarl': {
        'bp': 55,
        'type': 'Dark',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSound': True,
        'isSpread': True,
		'modOppStat' : {'SpA' : 2/3}
    },
    'Stored Power': {
        'bp': 20,
        'type': 'Psychic',
        'category': 'Special'
    },
    'Storm Throw': {
        'bp': 40,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'alwaysCrit': True
    },
    'Tackle': { 'bp': 50 },
    'Tail Slap': {
        'bp': 25,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True,
        'isMultiHit': True
    },
    'Thrash': {
        'bp': 120,
        'type': 'Normal',
        'category': 'Physical',
        'makesContact': True,
		'multiTurn' : True
    },
    'V-create': {
        'bp': 180,
        'type': 'Fire',
        'category': 'Physical',
        'makesContact': True,
		'modUserStat' : {'Def' : 2/3, 'SpD' : 2/3, 'Spe' : 2/3}
    },
    'Volt Switch': {
        'bp': 70,
        'type': 'Electric',
        'category': 'Special'
		# Extra: User must switch out immediately after attacking
    },
    'Wild Charge': {
        'bp': 90,
        'type': 'Electric',
        'category': 'Physical',
        'makesContact': True,
        'recoil': 1/4
    }
}

MOVES_BW.update(MOVES_DPP)

MOVES = {
    'Air Cutter': { 'bp': 60 },
    'Arm Thrust': {
        'bp': 15,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'isMultiHit': True
    },
    'Assurance': { 'bp': 60 },
    'Aura Sphere': { 'bp': 80 },
    'Blizzard': { 'bp': 110 },
    'Boomburst': {
        'bp': 140,
        'type': 'Normal',
        'category': 'Special',
        'isSound': True,
        'isSpread': True
    },
    'Chatter': { 'bp': 65 },
    'Crabhammer': { 'bp': 100 },
    'Dazzling Gleam': {
        'bp': 80,
        'type': 'Fairy',
        'category': 'Special',
        'isSpread': True
    },
    'Diamond Storm': {
        'bp': 100,
        'type': 'Rock',
        'category': 'Physical',
        'hasSecondaryEffect': True,
        'isSpread': True
    },
    'Draco Meteor': { 'bp': 130 },
    'Dragon Ascent': {
        'bp': 120,
        'type': 'Flying',
        'category': 'Physical',
        'makesContact': True
    },
    'Dragon Pulse': { 'bp': 85 },
    'Energy Ball': { 'bp': 90 },
    'Facade': { 'ignoresBurn': True },
    'Fire Blast': { 'bp': 110 },
    'Flamethrower': { 'bp': 90 },
    'Flying Press': {
        'bp': 80,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True
    },
    'Freeze-Dry': {
        'bp': 70,
        'type': 'Ice',
        'category': 'Special',
        'hasSecondaryEffect': True
		# Super effective against Water Types
    },
    'Frost Breath': { 'bp': 60 },
    'Heat Wave': { 'bp': 95 },
    'Hex': { 'bp': 65 },
    'Hidden Power Bug': { 'bp': 60 },
    'Hidden Power Dark': { 'bp': 60 },
    'Hidden Power Dragon': { 'bp': 60 },
    'Hidden Power Electric': { 'bp': 60 },
    'Hidden Power Fighting': { 'bp': 60 },
    'Hidden Power Fire': { 'bp': 60 },
    'Hidden Power Flying': { 'bp': 60 },
    'Hidden Power Ghost': { 'bp': 60 },
    'Hidden Power Grass': { 'bp': 60 },
    'Hidden Power Ground': { 'bp': 60 },
    'Hidden Power Ice': { 'bp': 60 },
    'Hidden Power Poison': { 'bp': 60 },
    'Hidden Power Psychic': { 'bp': 60 },
    'Hidden Power Rock': { 'bp': 60 },
    'Hidden Power Steel': { 'bp': 60 },
    'Hidden Power Water': { 'bp': 60 },
    'Hurricane': { 'bp': 110 },
    'Hydro Pump': { 'bp': 110 },
    'Ice Beam': { 'bp': 90 },
    'Incinerate': { 'bp': 60 },
    'Knock Off': { 'bp': 65 },
    'Land\'s Wrath': {
        'bp': 90,
        'type': 'Ground',
        'category': 'Physical',
        'isSpread': True
    },
    'Leaf Storm': { 'bp': 130 },
    'Light of Ruin': {
        'bp': 140,
        'type': 'Fairy',
        'category': 'Special',
		'recoil' : 1/3
    },
    'Low Sweep': { 'bp': 65 },
    'Magma Storm': { 'bp': 100 },
    'Meteor Mash': { 'bp': 90 },
    'Moonblast': {
        'bp': 95,
        'type': 'Fairy',
        'category': 'Special',
        'hasSecondaryEffect': True
    },
    'Muddy Water': { 'bp': 90 },
    'Nature Power': {
        'bp': 80,
        'type': 'Normal',
        'category': 'Special',
        'hasSecondaryEffect': True,
        'isSpread': False
    },
    'Oblivion Wing': {
        'bp': 80,
        'type': 'Flying',
        'category': 'Special',
		'restoreHalfDamage' : True
    },
    'Origin Pulse': {
        'bp': 110,
        'type': 'Water',
        'category': 'Special',
        'isSpread': True
    },
    'Overheat': { 'bp': 130 },
    'Phantom Force': {
        'bp': 90,
        'type': 'Ghost',
        'category': 'Physical',
        'makesContact': True
		# Extra: Disappears First Turn, reapears second turn
    },
    'Pin Missile': { 'bp': 25 },
    'Play Rough': {
        'bp': 90,
        'type': 'Fairy',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True
    },
    'Power Gem': { 'bp': 80 },
    'Power-Up Punch': {
        'bp': 40,
        'type': 'Fighting',
        'category': 'Physical',
        'makesContact': True,
        'hasSecondaryEffect': True,
        'isPunch': True
    },
    'Precipice Blades': {
        'bp': 120,
        'type': 'Ground',
        'category': 'Physical',
        'isSpread': 'True'
    },
    'Rock Tomb': { 'bp': 60 },
    'Storm Throw': { 'bp': 60 },
    'Surf': { 'bp': 90 },
    'Thief': { 'bp': 60 },
    'Thunder': { 'bp': 110 },
    'Thunderbolt': { 'bp': 90 },
    'Wake-Up Slap': { 'bp': 70 },
    'Water Shuriken': {
        'bp': 15,
        'type': 'Water',
        'category': 'Physical',
		'priority' : 1,
        'isMultiHit': True
    },
	'Draining Kiss' : {
		'bp' : 50, 
		'type' : 'Fairy',
		'category' : 'Special',
		'restoreHalfDamage' : True
	},
	'Endeavor' : {
		'type' : 'Normal',
		'category' : 'Physical',
		# Extra: sets the opposing pokemon's health equal to the user's
	},
	'Counter' : {
		'type' : 'Fighting',
		'category' : 'Physical',
		'priority' : -5
		# Extra: Deal back 2x physical damage done to user
	},
	'Mirror Coat' : {
		'type' : 'Psychic',
		'category' : 'Special',
		'priority' : -5
		# Extra: Deal back 2x special damage done to user
	},
	'Final Gambit' : {
		'type' : 'Fighting',
		'category' : 'Special',
		# Extra: inflicts damage equal to remaining HP, kills user
	},
	# end of damaging moves
	'Acid Armor' : {
		'modStat' : {'User' :('Def', 2)}
	},
	'Roar' : {
		'phazing' : True,
		'priority' : -6
	},
	'Whirlwind' : {
		'phazing' : True,
		'priority' : -6
	},
	'Trick Room' : {
		'priority' : -7
		# Extra: Field: Slower pokemon go first for 5 turns, cancels current trick room if already in use
	},
	'Acupressure' : None,
	'Agility' : {
		'modUserStat' : {'Spe' : 2}
	},
	'Amnesia' : {
		'modUserStat' : {'SpD' : 2}
	},
	'Aromatherapy' : {
		# Extra: Restores the status of teamates
	},
	'Assist' : None,
	'Attract' : None,
	'Autotomize' : {
		'modUserStat' : {'Spe' : 2, 'w' : .5}
	},
	'Baby-Doll Eyes' : None,
	'Barrier' : {
		'modUserStat' : {'Def' : 2}
	},
	'Baton Pass' : {
		# Extra: Pass stats to a teammate
	},
	'Belly Drum' : {
		# Extra: Reduce HP by half max, max attack
	},
	'Bulk Up' : {
		'modUserStat' : {'Atk' : 1.5, 'Def' : 1.5}
	},
	'Calm Mind' : {
		'modUserStat' : {'SpA' : 1.5, 'SpD' : 1.5}
	},
	'Coil' : {
		'modUserStat' : {'Atk' : 1.5, 'Def' : 1.5}
	},
	'Cosmic Power' : {
		'modUserStat' : {'Def' : 1.5, 'SpD' : 1.5}
	},
	'Cotton Guard' : {
		'modUserStat' : {'Def' : 2.5}
	},
	'Curse' : {
		'modUserStat' : {'Atk' : 1.5, 'Def' : 1.5, 'Spe' : 2/3}
		# Extra: if user is a ghost type half health, place curse on opponent
	},
	'Dark Void' : {
		# Extra: put opponent to sleep
	},
	'Defend Order' : {
		'modUserStat' : {'Def': 1.5, 'SpD' : 1.5}
	},
	'Defog' : {
		# Extra: Remove entry hazards from both sides
	},
	'Destiny Bond' : {
		# Extra: If user dies this turn, so does opponent
	},
	'Dragon Dance' : {
		'modUserStat' : {'Atk' : 1.5, 'Spe' : 1.5}
	},
	'Encore' : {
		# Extra: opponent uses same move three times in a row
	},
	'Endure' : None,
	'Entrainment' : None,
	'Feather Dance' : {
		'modUserStat' : {'Atk' : .5}
	},
	'Fling' : None,
	'Focus Energy' : {
		# increases critical hit ratio
	},
	'Foresight' : {
		# allows normal and fighting type attacks to hit ghost types
	},
	'Geomancy' : {
		'modUserStat' : {'SpA' : 2, 'SpD' : 2, 'Spe' : 2},
	},
	'Glare' : {
		# Paralyes the opponent
	},
	'Gravity' : None,
	'Growth' : {
		'modUserStat' : {'Atk' : 1.5, 'SpA' : 1.5}
		# if sun is up, double boosts
	},
	'Haze' : {
		# resets all stats on the field
	},
	'Heal Bell' : {
		# same as Aromatherapy
	},
	'Heal Order' : {
		'heal' : True
	},
	'Healing Wish' : {
		# kills user, restores next pokemon
	},
	'Hone Claws' : {
		'modUserStat' : {'Atk' : 2}
	},
	'Howl' : {
		'modUserStat' : {'Atk' : 1.5}
	},
	'Hypnosis' : {
		# Puts opponent to sleep
	},
	'Ingrain' : {
		# gives roots (used in BP)
	},
	'Iron Defense' : {
		'modUserStat' : {'Def' : 2}
	},
	'Leech Seed' : {
		# Steals 10% of opponents max HP each turn
		# Fails on grass types
	},
	'Light Screen' : {
		# gives whole team x2 SpD
	},
	'Lovely Kiss' : {
		# puts opponent to sleep
	},
	'Lunar Dance' : {
		# kills user, restores next pokemon
	},
	'Magic Coat' : {
		'priority': 4
		# reflects status moves directed at the user back at the opponent
	},
	'Magnet Rise' : {
		# User becomes immune to ground type moves for 5 turns
	},
	'Memento' : {
		'modOppStat' : {'Atk' : .5, 'SpA' : .5}
		# user faints
	},
	'Milk Drink' : {
		'heal' : True
	},
	'Moonlight' : {
		'heal' : True
		# varies with weather
	},
	'Morning Sun' : {
		'heal' : True
		# varies with weather
	},
	'Nasty Plot' : {
		'modUserStat' : {'SpA' : 2}
	},
	'Pain Split' : {
		# averages both Pokemon's HP
	},
	'Perish Song' : {
		# faints any pokemon that hears it after three turns
	},
	'Protect' : {
		'priority' : 4
		# user is immune to a move
	},
	'Psycho Shift': {
		# Gives the opponent the user's status condition
	},
	'Quiver Dance' : {
		'modUserStat' : {'SpA' : 1.5, 'SpD' : 1.5, 'Spe' : 1.5}
	},
	'Rain Dance' : {
		# changes weather to rain
	},
	'Recover' : {
		'heal' : True
	},
	'Reflect' : {
		# give all teammates 2x Def
	},
	'Refresh' : {
		# restores user's status condition
	},
	'Rest' : {
		# restores user's health to full, puts user to sleep
	},
	'Rock Polish' : {
		'modUserStat' : {'Spe' : 2}
	},
	'Roost' : {
		'heal' : True
		# removes ground type immunity temporarily
	},
	'Shell Smash' : {
		'modUserStat' : {'Atk' : 2, 'SpA' : 2, 'Spe' : 2, 'Def' : 2/3, 'SpD': 2/3}
	},
	'Shift Gear' : {
		'modUserStat' : {'Atk' : 1.5, 'Spe' : 2}
	},
	'Slack Off' : {
		'heal' : True
	},
	'Sleep Powder' : {
		# puts opponent to sleep, fails on grass types
	},
	'Sleep Talk' : {
		# only works while asleep, chooses a random attack
	},
	'Soft-Boiled' : {
		'heal' : True
	},
	'Spikes' : {
		# stacks up to three, deals 6.25, 12.5, then 25 percent of grounded mons max health upon switch in
	},
	'Spiky Shield' : {
		'priority' : 4
		# one turn immunity
	},
	'Spore' : {
		# puts opponent to sleep, fails on grass types
	},
	'Stealth Rock' : {
		# damages opponent upon entry, a really good move
	},
	'Sticky Web' : {
		# lowers grounded opponent's speed 
	},
	'Stun Spore' : {
		# paralyzes opponent, fails on grass types
	},
	'Substitute' : {
		# takes 25% of user's max health, puts user behind a sub worth the health taken, they are immune until sub is dead
	}, 
	'Switcheroo' : {
		# switches user's item with opponent's
	},
	'Swords Dance' : {
		'modUserStat' : {'Atk' : 2}
	},
	'Synthesis' : {
		'heal' : True
		# varies with weather
	},
	'Tail Glow' : { 
		'modUserStat' : {'SpA' : 2.5}
	},
	'Tailwind' : {
		# doubles user's team's speed for 4 turns
	},
	'Taunt' : {
		# opponent can only use attacking moves
	},
	'Thunder Wave' : {
		# paralyzes opponent, fails on electric and ground types
	},
	'Tickle' : {
		'modOppStat' : {'Atk' : 2/3, 'Def' : 2/3}
	},
	'Toxic' : {
		# poisons opponent, fails on poison and steel types
	}, 
	'Toxic Spikes' : {
		# stacks up to 2 times poisons all incoming pokemon on the targets side(not poison and steel) - poison types absorb them
	},
	'Trick' : {
		# switches user's item with opponent's
	},
	'Will-O-Wisp' : {
		# burns opponent, fails on fire types
	},
	'Wish' : {
		# restores half users max hp to user or a teammate on the following turn
	},
	'Work Up' : {
		'modUserStat' : {'Atk' : 1.5, 'SpA' : 1.5}
	}, 
	'Yawn' : {
		# puts opponent to sleep on the following turn
	}
}

# for value of status moves: you only need to see if the move is worth using,
# do this by looking at the current state of the pokemon and field
# if the move is not worth using or too complex to decide, put None

MOVES.update(MOVES_BW)

MOVES['Ancient Power'] = MOVES['AncientPower'];
MOVES['Dynamic Punch'] = MOVES['DynamicPunch'];
MOVES['Extreme Speed'] = MOVES['ExtremeSpeed'];
MOVES['Feint Attack'] = MOVES['Faint Attack'];
MOVES['High Jump Kick'] = MOVES['Hi Jump Kick'];
MOVES['Self-Destruct'] = MOVES['Selfdestruct'];
MOVES['Solar Beam'] = MOVES['SolarBeam'];
MOVES['Thunder Punch'] = MOVES['ThunderPunch'];
del MOVES['AncientPower'];
del MOVES['DynamicPunch'];
del MOVES['ExtremeSpeed'];
del MOVES['Faint Attack'];
del MOVES['Hi Jump Kick'];
del MOVES['Selfdestruct'];
del MOVES['SolarBeam'];
del MOVES['ThunderPunch'];


