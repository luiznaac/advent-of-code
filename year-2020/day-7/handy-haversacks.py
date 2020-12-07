import utils.utils as utils


def parse_bag_rules():
    rules = utils.open_file('bag-rules.txt')

    bag_rules = {}

    for rule in rules:
        rule_parts = rule.split('contain')
        bag_key = rule_parts.pop(0).replace(' bags ', '')
        bags_contained = rule_parts.pop(0).split(',')

        this_bag = {}

        for bag in bags_contained:
            bag_parts = bag.strip('. ').split(' ', 1)
            bag_quantity = bag_parts[0]
            bag_color = bag_parts[1].replace(' bags', '').replace(' bag', '')

            this_bag[bag_color] = bag_quantity

        bag_rules[bag_key] = this_bag

    return bag_rules


# PART ONE #
verified_bags = []


def find_bags_with_bag(bag, bag_rules):
    bags_with_bag = []

    for bag_rule in bag_rules:
        if bag in bag_rules[bag_rule]:
            bags_with_bag.append(bag_rule)

    for bag_with_bag in bags_with_bag:
        if bag_with_bag not in verified_bags:
            verified_bags.append(bag_with_bag)
            bags_with_bag += find_bags_with_bag(bag_with_bag, bag_rules)

    return bags_with_bag


bag_rules = parse_bag_rules()
bags_found = find_bags_with_bag('shiny gold', bag_rules)
bags_found = list(dict.fromkeys(bags_found))
print(len(bags_found))


# PART TWO #
def count_bags_inside_bag(bag, bag_rules):
    bags_inside_bag = bag_rules[bag]
    count = 0

    if len(bags_inside_bag) == 1 and 'other' in bags_inside_bag:
        return 0

    for bag_inside in bags_inside_bag:
        if bag_inside != 'other':
            num_of_bags = int(bags_inside_bag[bag_inside])
            count += num_of_bags + num_of_bags * count_bags_inside_bag(bag_inside, bag_rules)

    return count


print(count_bags_inside_bag('shiny gold', bag_rules))
