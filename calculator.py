# Embedded file name: C:\PsBot\calculator.py
from __future__ import division
import math
import operator
from collections import OrderedDict
from items import MEGA_STONES, get_item_boost_type
range = xrange

def prod(factors):
    return reduce(operator.mul, factors, 1)


TYPES = ['Normal',
 'Fire',
 'Water',
 'Electric',
 'Grass',
 'Ice',
 'Fighting',
 'Poison',
 'Ground',
 'Flying',
 'Psychic',
 'Bug',
 'Rock',
 'Ghost',
 'Dragon',
 'Dark',
 'Steel',
 'Fairy']
OPP_TYPE = OrderedDict([ reversed(t) for t in enumerate(TYPES) ])
TYPE_CHART = {'Normal': [1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            0.5,
            0,
            1,
            1,
            0.5,
            1],
 'Fire': [1,
          0.5,
          0.5,
          1,
          2,
          2,
          1,
          1,
          1,
          1,
          1,
          2,
          0.5,
          1,
          0.5,
          1,
          2,
          1],
 'Water': [1,
           2,
           0.5,
           1,
           0.5,
           1,
           1,
           1,
           2,
           1,
           1,
           1,
           2,
           1,
           0.5,
           1,
           1,
           1],
 'Electric': [1,
              1,
              2,
              0.5,
              0.5,
              1,
              1,
              1,
              0,
              2,
              1,
              1,
              1,
              1,
              0.5,
              1,
              1,
              1],
 'Grass': [1,
           0.5,
           2,
           1,
           0.5,
           1,
           1,
           0.5,
           2,
           0.5,
           1,
           0.5,
           2,
           1,
           0.5,
           1,
           0.5,
           1],
 'Ice': [1,
         0.5,
         0.5,
         1,
         2,
         0.5,
         1,
         1,
         2,
         2,
         1,
         1,
         1,
         1,
         2,
         1,
         0.5,
         1],
 'Fighting': [2,
              1,
              1,
              1,
              1,
              2,
              1,
              0.5,
              1,
              0.5,
              0.5,
              0.5,
              2,
              0,
              1,
              2,
              2,
              0.5],
 'Poison': [1,
            1,
            1,
            1,
            2,
            1,
            1,
            0.5,
            0.5,
            1,
            1,
            1,
            0.5,
            0.5,
            1,
            1,
            0,
            2],
 'Ground': [1,
            2,
            1,
            2,
            0.5,
            1,
            1,
            2,
            1,
            0,
            1,
            0.5,
            2,
            1,
            1,
            1,
            2,
            1],
 'Flying': [1,
            1,
            1,
            0.5,
            2,
            1,
            2,
            1,
            1,
            1,
            1,
            2,
            0.5,
            1,
            1,
            1,
            0.5,
            1],
 'Psychic': [1,
             1,
             1,
             1,
             1,
             1,
             2,
             2,
             1,
             1,
             0.5,
             1,
             1,
             1,
             1,
             0,
             0.5,
             1],
 'Bug': [1,
         0.5,
         1,
         1,
         2,
         1,
         0.5,
         0.5,
         1,
         0.5,
         2,
         1,
         1,
         0.5,
         1,
         2,
         0.5,
         0.5],
 'Rock': [1,
          2,
          1,
          1,
          1,
          2,
          0.5,
          1,
          0.5,
          2,
          1,
          2,
          1,
          1,
          1,
          1,
          0.5,
          1],
 'Ghost': [0,
           1,
           1,
           1,
           1,
           1,
           1,
           1,
           1,
           1,
           2,
           1,
           1,
           2,
           1,
           0.5,
           1,
           1],
 'Dragon': [1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            1,
            0.5,
            0],
 'Dark': [1,
          1,
          1,
          1,
          1,
          1,
          0.5,
          1,
          1,
          1,
          2,
          1,
          1,
          2,
          1,
          0.5,
          1,
          0.5],
 'Steel': [1,
           0.5,
           0.5,
           0.5,
           1,
           2,
           1,
           1,
           1,
           1,
           1,
           1,
           2,
           1,
           1,
           1,
           0.5,
           2],
 'Fairy': [1,
           0.5,
           1,
           1,
           1,
           1,
           2,
           0.5,
           1,
           1,
           1,
           1,
           1,
           1,
           2,
           2,
           0.5,
           1]}

def _calculate_damage(attacker, defender, move, field):
    """
    Functions
    """

    def chain_mods(mods):
        m = 4096
        for mod in mods:
            if mod != 4096:
                m = m * mod + 2048 >> 12

        return m

    def get_move_effectiveness(move, types, is_ghost_revealed, is_gravity):
        eff = []
        for type in types:
            if is_ghost_revealed and type is 'Ghost' and (move.type is 'Normal' or move.type is 'Fighting'):
                eff.append(1)
                continue
            elif is_gravity and type is 'Flying' and move.type is 'Ground':
                eff.append(1)
            elif move.name is 'Freeze-Dry' and type is 'Water':
                eff.append(2)
                continue
            elif move.name is 'Flying Press':
                eff.append(TYPE_CHART['Fighting'][OPP_TYPE[type]] * TYPE_CHART['Flying'][OPP_TYPE[type]])
            else:
                eff.append(TYPE_CHART[move.type][OPP_TYPE[type]])

        return prod(eff)

    def count_boosts(boosts):
        return sum([ stat for stat in STATS if boosts[stat] > 0 ])

    def round(num):
        if num % 1 > 0.5:
            return math.ceil(num)
        return math.floor(num)

    weather = field['weather']
    def_ability = defender.ability
    if attacker.ability in ('Mold Breaker', 'Teravolt', 'Turboblaze'):
        def_ability = ''
    is_critical = 'is_crit' in move.data and def_ability not in ('Battle Armor', 'Shell Armor')
    if attacker.ability is 'Aerilate' and move.type is 'Normal':
        move.type = 'Flying'
    elif attacker.ability is 'Pixilate' and move.type is 'Normal':
        move.type = 'Fairy'
    elif attacker.ability is 'Refrigerate' and move.type is 'Normal':
        move.type = 'Ice'
    elif attacker.ability is 'Normalize':
        move.type = 'Normal'
    type_effectiveness = get_move_effectiveness(move, defender.type, attacker.ability is 'Scrappy' or 'Foresight' in field, 'Gravity' in field)
    if type_effectiveness == 0:
        return [0]
    if def_ability is 'Wonder Guard' and type_effectiveness <= 1 or move.type is 'Grass' and def_ability is 'Sap Sipper' or move.type is 'Fire' and def_ability is 'Flash Fire' or move.type is 'Water' and def_ability in ('Dry Skin', 'Storm Drain', 'Water Absorb') or move.type is 'Electric' and def_ability in ('Lighting Rod', 'Motor Drive', 'Volt Absorb') or move.type is 'Ground' and 'Gravity' not in field and def_ability is 'Levitate' or 'isBullet' in move.data and def_ability is 'Bulletproof' or 'isSound' in move.data and def_ability is 'Soundproof':
        return [0]
    if move.type is 'Ground' and 'isGravity' not in field and defender.item is 'Air Balloon':
        return [0]
    if move.name is 'Seismic Toss' or move.name is 'Night Shade':
        lv = attacker.level
        if attacker.ability is 'Parental Bond':
            lv *= 2
        return [lv]
    turn_order = 'FIRST' if attacker.stats['Spe'] > defender.stats['Spe'] else 'LAST'
    if move.name is 'Payback':
        base_power = 100 if turn_order is 'LAST' else 50
    elif move.name is 'Electro Ball':
        r = attacker.stats['Spe'] // defender.stats['Spe']
        base_power = 150 if r >= 4 else (120 if r >= 3 else (80 if r >= 2 else 60))
    elif move.name is 'Gyro Ball':
        base_power = min(150, 25 * defender.stats['Spe'] // attacker.stats['Spe'])
    elif move.name is 'Punishment':
        base_power = min(200, 60 + 20 * count_boosts(attacker.boosts))
    elif move.name is 'Low Kick' or move.name is 'Grass Knot':
        w = defender.weight
        base_power = 120 if w >= 200 else (100 if w >= 100 else (80 if w >= 50 else (60 if w >= 25 else (40 if w >= 10 else 20))))
    elif move.name is 'Hex':
        base_power = move.bp * (2 if defender.status is not 'Healthy' else 1)
    elif move.name is 'Heavy Slam' or move.name is 'Heat Crash':
        wr = attacker.weight // defender.weight
        base_power = 120 if wr >= 5 else (100 if wr >= 4 else (80 if wr >= 3 else (60 if wr >= 2 else 40)))
    elif move.name is 'Stored Power':
        base_power = 20 + 20 * count_boosts(attacker.boosts)
    elif move.name is 'Acrobatics':
        base_power = 110 if attacker.item is '' else 55
    elif move.name is 'Wake-up Slap':
        base_power = move.bp * (2 if defender.status is 'Asleep' else 1)
    elif move.name is 'Weather Ball':
        base_power = 100 if field.weather is not '' else 50
    elif move.name is 'Eruption' or move.name is 'Water Spout':
        base_power = max(1, 150 * attacker.current_HP // attacker.stats['HP'])
    else:
        base_power = move.bp
    bp_mods = []
    if attacker.ability is 'Technician' and base_power <= 60 or attacker.ability is 'Flare Boost' and attacker.status is 'Burned' and move.category is 'Special' or attacker.ability is 'Toxic Boost' and (attacker.status is 'Poisoned' or attacker.status is 'Badly Poisoned') and move.category is 'Special':
        bp_mods.append(6144)
    elif attacker.ability is 'Analytic' and turn_order is not 'FIRST':
        bp_mods.append(5325)
    elif attacker.ability is 'Sand Force' and field.weather is 'Sand' and move.type in ('Rock', 'Ground', 'Steel'):
        bp_mods.append(5325)
    elif attacker.ability is 'Reckless' and 'hasRecoil' in move.data or attacker.ability is 'Iron Fist' and 'isPunch' in move.data:
        bp_mods.append(4915)
    if def_ability is 'Heatproof' and move.type is 'Fire':
        bp_mods.append(2048)
    elif def_ability is 'Dry Skin' and move.type is 'Fire':
        bp_mods.append(5120)
    if attacker.ability is 'Sheer Force' and 'hasSecondaryEffect' in move.data:
        bp_mods.append(5325)
    if get_item_boost_type(attacker.item) is move.type:
        bp_mods.append(4915)
    elif attacker.item is 'Muscle Band' and move.category is 'Physical' or attacker.item is 'Wise Glasses' and move.category is 'Special':
        bp_mods.append(4505)
    if move.name is 'Facade' and attacker.status in ('Burned', 'Paralyzed', 'Poisoned', 'Badly Poisoned') or move.name is 'Brine' and defender.currentHP <= defender.stats['HP'] / 2 or move.name is 'Venoshock' and defender.status in ('Poisoned', 'Badly Poisoned'):
        bp_mods.append(8192)
    elif move.name is 'Solar Beam' and weather in ('Rain', 'Heavy Rain', 'Sand', 'Hail'):
        bp_mods.append(2048)
    elif move.name is 'Knock Off' and defender.item not in MEGA_STONES:
        bp_mods.append(6144)
    elif attacker.ability in ('Aerilate', 'Pixilate', 'Refrigerate'):
        bp_mods.append(5325)
    elif attacker.ability is 'Mega Launcher' and 'isPulse' in move.data or attacker.ability is 'Strong Jaw' and 'isBite' in move.data:
        bp_mods.append(6144)
    elif attacker.ability is 'Tough Claws' and 'makesContact' in move.data:
        bp_mods.append(5447)
    base_power = max(1, round(base_power * chain_mods(bp_mods) / 4096))
    attack_source = defender if move.name is 'Foul Play' else attacker
    attack_stat = 'Atk' if move.category is 'Physical' else 'SpA'
    if attack_source.boosts[attack_stat] == 0 or is_critical and attack_source.boosts[attack_stat] < 0:
        attack = attack_source.raw_stats[attack_stat]
    else:
        attack = attack_source.stats[attack_stat]
    if attacker.ability is 'Hustle' and move.category is 'Physical':
        attack = round(attack * 3 / 2)
    atk_mods = []
    if def_ability is 'Thick Fat' and (move.type is 'Fire' or move.type is 'Ice'):
        atk_mods.append(2048)
    if attacker.ability is 'Guts' and attacker.status is not 'Healthy' and move.category is 'Physical' or attacker.ability is 'Overgrow' and attacker.current_HP <= attacker.stats['HP'] / 3 and move.type is 'Grass' or attacker.ability is 'Torrent' and attacker.current_HP <= attacker.stats['HP'] / 3 and move.type is 'Water' or attacker.ability is 'Blaze' and attacker.current_HP <= attacker.stats['HP'] / 3 and move.type is 'Fire':
        atk_mods.append(6144)
    elif attacker.ability is 'Flash Fire (activated)' and move.type is 'Fire':
        atk_mods.append(6144)
    elif attacker.ability is 'Solar Power' and weather is 'Sun' and move.category is 'Special' or attacker.ability is 'Flower Gift' and weather is 'Sun' and move.category is 'Physical':
        atk_mods.append(6144)
    elif attacker.ability is 'Defeatist' and attacker.current_HP <= attacker.stats['HP'] / 2 or attacker.ability is 'Slow Start' and move.category is 'Physical':
        atk_mods.append(2048)
    elif (attacker.ability is 'Huge Power' or attacker.ability is 'Pure Power') and move.category is 'Physical':
        atk_mods.append(8192)
    if attacker.item is 'Thick Club' and (attacker.name is 'Cubone' or attacker.name is 'Marowak') and move.category is 'Physical' or attacker.item is 'Deep Sea Tooth' and attacker.name is 'Clamperl' and move.category is 'Special' or attacker.item is 'Light Ball' and attacker.name is 'Pikachu':
        atk_mods.append(8192)
    elif attacker.item is 'Soul Dew' and (attacker.name is 'Latios' or attacker.name is 'Latias') and move.category is 'Special' or attacker.item is 'Choice Band' and move.category is 'Physical' or attacker.item is 'Choice Specs' and move.category is 'Special':
        atk_mods.append(6144)
    attack = max(1, round(attack * chain_mods(atk_mods) / 4096))
    hits_physical = move.category is 'Physical' or 'dealsPhysicalDamage' in move.data
    defense_stat = 'Def' if hits_physical else 'SpD'
    if defender.boosts[defense_stat] == 0 or is_critical and defender.boosts[defense_stat] > 0 or 'ignoresDefenseBoosts' in move.data or attacker.ability is 'Unaware':
        defense = defender.raw_stats[defense_stat]
    else:
        defense = defender.stats[defense_stat]
    if weather == 'Sand' and 'Rock' in defender.type and not hits_physical:
        defense = round(defense * 3 / 2)
    def_mods = []
    if def_ability is 'Marvel Scale' and defender.status is not 'Healthy' and hits_physical:
        def_mods.append(6144)
    elif def_ability is 'Flower Gift' and weather is 'Sun' and not hits_physical:
        def_mods.append(6144)
    if defender.item is 'Deep Sea Scale' and defender.name is 'Clamperl' and not hits_physical or defender.item is 'Metal Powder' and defender.name is 'Ditto' or defender.item is 'Soul Dew' and (defender.name is 'Latios' or defender.name is 'Latias') and not hits_physical or defender.item is 'Assault Vest' and not hits_physical or defender.item is 'Eviolite':
        def_mods.append(6144)
    defense = max(1, round(defense * chain_mods(def_mods) / 4096))
    base_damage = (2 * attacker.level // 5 + 2) * base_power * attack // defense // 50 + 2
    if weather is 'Sun' and move.type is 'Fire' or weather is 'Rain' and move.type is 'Water':
        base_damage = round(base_damage * 6144 / 4096)
    elif weather is 'Sun' and move.type is 'Water' or weather is 'Rain' and move.type is 'Fire' or weather is 'Strong Winds' and 'Flying' in defender.type and TYPE_CHART[move.type][OPP_TYPE['Flying']] == 2:
        base_damage = round(base_damage * 2048 / 4096)
    elif weather is 'Harsh Sunshine' and move.type is 'Water' or weather is 'Heavy Rain' and move.type is 'Fire':
        return [0]
    if 'Gravity' in field or 'Flying' in attacker.type and attacker.item is not 'Air Balloon' and attacker.ability is not 'Levitate':
        if field['terrain'] == 'Electric' and move.type is 'Electric' or field['terrain'] == 'Grassy' and move.type is 'Grass':
            base_damage = round(base_damage * 6144 / 4096)
        elif field['terrain'] == 'Misty' and move.type is 'Dragon':
            base_damage = round(base_damage * 2048 / 4096)
    if is_critical:
        base_damage = math.floor(base_damage * 1.5)
    stab_mod = 4096
    if move.type in attacker.type:
        if attacker.ability is 'Adaptability':
            stab_mod = 8192
        else:
            stab_mod = 6144
    elif attacker.ability is 'Protean':
        stab_mod = 6144
    apply_burn = attacker.status is 'Burned' and move.category is 'Physical' and attacker.ability is not 'Guts' and 'ignoresBurn' not in move.data
    final_mods = []
    if 'Reflect' in field and move.category is 'Physical' and not is_critical:
        final_mods.append(2703)
    elif 'Light Screen' in field and move.category is 'Special' and not is_critical:
        final_mods.append(2703)
    if def_ability is 'Multiscale' and defender.current_HP == defender.stats['HP']:
        final_mods.append(2048)
    if attacker.ability is 'Tinted Lens' and type_effectiveness < 1:
        final_mods.append(8192)
    elif attacker.ability is 'Sniper' and is_critical:
        final_mods.append(6144)
    if (def_ability is 'Solid Rock' or def_ability is 'Filter') and type_effectiveness > 1:
        final_mods.append(3072)
    elif attacker.item is 'Expert Belt' and type_effectiveness > 1:
        final_mods.append(4915)
    elif attacker.item is 'Life Orb':
        final_mods.append(5324)
    if def_ability is 'Fur Coat' and hits_physical:
        final_mods.append(2048)
    final_mod = chain_mods(final_mods)
    damage = []
    for i in range(16):
        d = base_damage * (85 + i) // 100
        d = round(d * stab_mod / 4096)
        d = math.floor(d * type_effectiveness)
        if apply_burn:
            d //= 2
        d = max(1, d)
        d = round(d * final_mod / 4096)
        if attacker.ability is 'Parental Bond' and move.hits:
            d = math.floor(d * 3 / 2)
        damage.append(d)

    return damage


def get_ko_chance(attacker, defender, move, field, isBadDreams = False):
    damage = _calculate_damage(attacker, defender, move, field)
    if 'isMultiHit' in move.data:
        hits = [2,
         3,
         4,
         5]
    elif 'isTwoHit' in move.data:
        hits = [2]
    else:
        hits = 1
    if damage[0] >= defender.current_HP:
        return (1, 100)
    hazards = 0
    if 'SR' in field and defender.ability is not 'Magic Guard':
        effectiveness = prod((TYPE_CHART['Rock'][OPP_TYPE[type]] for type in defender.type))
        hazards += effectiveness * defender.stats['HP'] // 8
    if 'Spikes' in field and 'Flying' not in defender.types and defender.ability not in ('Magic Guard', 'Levitate') and defender.item is not 'Air Balloon':
        hazards += defender.stats['HP'] // (10 - 2 * field['Spikes'])
    eot = 0
    if field['weather'] is 'Sun' and (defender.ability is 'Dry Skin' or defender.ability is 'Solar Power'):
        eot -= defender.stats['HP'] // 8
    elif field['weather'] is 'Rain':
        if defender.ability is 'Dry Skin':
            eot += defender.stats['HP'] // 8
        elif defender.ability is 'Rain Dish':
            eot += defender.stats['HP'] // 16
    elif field['weather'] is 'Sand':
        if defender.type not in ('Rock', 'Ground', 'Steel') and defender.ability not in ('Magic Guard', 'Overcoat', 'Sand Force', 'Sand Rush') and defender.item is not 'Safety Goggles':
            eot -= defender.stats['HP'] // 16
    elif field['weather'] is 'Hail':
        if defender.ability is 'Ice Body':
            eot += defender.stats['HP'] // 16
        elif defender.ability not in ('Magic Guard', 'Overcoat', 'Snow Cloak') and defender.item is not 'Safety Goggles':
            eot -= defender.stats['HP'] // 16
    if defender.item is 'Leftovers':
        eot += defender.stats['HP'] // 16
    elif defender.item is 'Black Sludge':
        if 'Poison' in defender.type:
            eot += self.stats['HP'] // 16
        elif defender.ability is not 'Magic Guard' and defender.ability is not 'Klutz':
            eot -= self.stats['HP'] // 16
    if field['terrain'] is 'Grassy' and ('Gravity' in field or 'Flying' not in defender.type and defender.item is not 'Air Balloon' and defender.ability is not 'Levitate'):
        eot += defender.stats['HP'] // 16
    toxic_counter = 0
    if defender.status is 'Badly Poisoned':
        if defender.ability is 'Poison Heal':
            eot += defender.stats['HP'] // 16
        elif defender.ability is not 'Magic Guard':
            toxic_counter = defender.toxic_counter
    elif defender.status is 'Burned':
        if defender.ability is 'Heatproof':
            eot -= defender.stats['HP'] // 16
        elif defender.ability is not 'Magic Guard':
            eot -= defender.stats['HP'] // 8
    elif defender.status is 'Asleep' and is_bad_dreams and defender.ability is not 'Magic Guard':
        eot -= defender.stats['HP'] // 8
    multi_hit_damage = []
    if hits != 1:
        for hit in hits:
            multi_hit_damage.append(squash_multi_hit(damage, hit))

    c = ko_chance(damage, defender.current_HP - hazards, 0, 1, defender.current_HP, toxic_counter)
    if c == 1:
        return (1, 100)
    if c > 0:
        return (1, round(c * 1000) / 10)
    for i in range(2, 5):
        c = ko_chance(damage, defender.current_HP - hazards, eot, i, defender.current_HP, toxic_counter)
        if c == 1:
            return (i, 100)
        if c > 0:
            return (i, round(c * 1000) / 10)

    for i in range(5, 10):
        if predict_total(damage[0], eot, i, toxic_counter, defender.current_HP) >= defender.current_HP - hazards:
            return (i, 100)
        if predict_total(damage[len(damage) - 1], eot, i, toxic_counter, defender.current_HP) >= defender.current_HP - hazards:
            return i

    return 0


def ko_chance(damage, curr_hp, eot, hits, max_curr_hp, toxic_counter):
    n = len(damage)
    min_damage = damage[0]
    max_damage = damage[n - 1]
    if hits == 1:
        if max_damage < curr_hp:
            return 0
        for i in range(n):
            if damage[i] >= curr_hp:
                return (n - i) / n

    if predict_total(max_damage, eot, hits, toxic_counter, max_curr_hp) < curr_hp:
        return 0
    if predict_total(min_damage, eot, hits, toxic_counter, max_curr_hp) >= curr_hp:
        return 1
    toxic_damage = 0
    if toxic_counter > 0:
        toxic_damage = toxic_counter * max_curr_hp // 16
        toxic_counter += 1
    sum = 0
    for i in range(n):
        c = ko_chance(damage, curr_hp - damage[i] + eot - toxic_damage, eot, hits - 1, max_curr_hp, toxic_counter)
        if c == 1:
            sum += n - i
        else:
            sum += c

    return sum / n


def predict_total(damage, eot, hits, toxic_counter, max_curr_hp):
    toxic_damage = 0
    if toxic_counter > 0:
        for i in range(hits):
            toxic_damage += (toxic_counter + i) * max_hp // 16

    total = damage * hits - eot * (hits - 1) + toxic_damage
    return total


def squash_multi_hit(d, hits):
    if len(d) == 1:
        return [d[0] * hits]
    if len(d) == 16:
        if hits == 2:
            return [2 * d[0],
             d[2] + d[3],
             d[4] + d[4],
             d[4] + d[5],
             d[5] + d[6],
             d[6] + d[6],
             d[6] + d[7],
             d[7] + d[7],
             d[8] + d[8],
             d[8] + d[9],
             d[9] + d[9],
             d[9] + d[10],
             d[10] + d[11],
             d[11] + d[11],
             d[12] + d[13],
             2 * d[15]]
        if hits == 3:
            return [3 * d[0],
             d[3] + d[3] + d[4],
             d[4] + d[4] + d[5],
             d[5] + d[5] + d[6],
             d[5] + d[6] + d[6],
             d[6] + d[6] + d[7],
             d[6] + d[7] + d[7],
             d[7] + d[7] + d[8],
             d[7] + d[8] + d[8],
             d[8] + d[8] + d[9],
             d[8] + d[9] + d[9],
             d[9] + d[9] + d[10],
             d[9] + d[10] + d[10],
             d[10] + d[11] + d[11],
             d[11] + d[12] + d[12],
             3 * d[15]]
        if hits == 4:
            return [4 * d[0],
             4 * d[4],
             d[4] + d[5] + d[5] + d[5],
             d[5] + d[5] + d[6] + d[6],
             4 * d[6],
             d[6] + d[6] + d[7] + d[7],
             4 * d[7],
             d[7] + d[7] + d[7] + d[8],
             d[7] + d[8] + d[8] + d[8],
             4 * d[8],
             d[8] + d[8] + d[9] + d[9],
             4 * d[9],
             d[9] + d[9] + d[10] + d[10],
             d[10] + d[10] + d[10] + d[11],
             4 * d[11],
             4 * d[15]]
        if hits == 5:
            return [5 * d[0],
             d[4] + d[4] + d[4] + d[5] + d[5],
             d[5] + d[5] + d[5] + d[5] + d[6],
             d[5] + d[6] + d[6] + d[6] + d[6],
             d[6] + d[6] + d[6] + d[6] + d[7],
             d[6] + d[6] + d[7] + d[7] + d[7],
             5 * d[7],
             d[7] + d[7] + d[7] + d[8] + d[8],
             d[7] + d[7] + d[8] + d[8] + d[8],
             5 * d[8],
             d[8] + d[8] + d[8] + d[9] + d[9],
             d[8] + d[9] + d[9] + d[9] + d[9],
             d[9] + d[9] + d[9] + d[9] + d[10],
             d[9] + d[10] + d[10] + d[10] + d[10],
             d[10] + d[10] + d[11] + d[11] + d[11],
             5 * d[15]]
    elif len(d) == 39:
        if hits == 2:
            return [2 * d[0],
             2 * d[7],
             2 * d[10],
             2 * d[12],
             2 * d[14],
             d[15] + d[16],
             2 * d[17],
             d[18] + d[19],
             d[19] + d[20],
             2 * d[21],
             d[22] + d[23],
             2 * d[24],
             2 * d[26],
             2 * d[28],
             2 * d[31],
             2 * d[38]]
        if hits == 3:
            return [3 * d[0],
             3 * d[9],
             3 * d[12],
             3 * d[13],
             3 * d[15],
             3 * d[16],
             3 * d[17],
             3 * d[18],
             3 * d[20],
             3 * d[21],
             3 * d[22],
             3 * d[23],
             3 * d[25],
             3 * d[26],
             3 * d[29],
             3 * d[38]]
        if hits == 4:
            return [4 * d[0],
             2 * d[10] + 2 * d[11],
             4 * d[13],
             4 * d[14],
             2 * d[15] + 2 * d[16],
             2 * d[16] + 2 * d[17],
             2 * d[17] + 2 * d[18],
             2 * d[18] + 2 * d[19],
             2 * d[19] + 2 * d[20],
             2 * d[20] + 2 * d[21],
             2 * d[21] + 2 * d[22],
             2 * d[22] + 2 * d[23],
             4 * d[24],
             4 * d[25],
             2 * d[27] + 2 * d[28],
             4 * d[38]]
        if hits == 5:
            return [5 * d[0],
             5 * d[11],
             5 * d[13],
             5 * d[15],
             5 * d[16],
             5 * d[17],
             5 * d[18],
             5 * d[19],
             5 * d[19],
             5 * d[20],
             5 * d[21],
             5 * d[22],
             5 * d[23],
             5 * d[25],
             5 * d[27],
             5 * d[38]]
    return d