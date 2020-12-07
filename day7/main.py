input_file = open("input.txt", "r")
bag_map = {}
rev_bag_map = {}
for line in input_file:
    line_seg = line.split(" contain ")
    dest_bags = line_seg[1].replace("bags", "bag").replace(",", "").split("bag")
    dest_bags = [x.strip() for x in dest_bags]
    dest_bags.pop()  # remove "."
    src_bag = line_seg[0][:-5]
    if src_bag not in rev_bag_map:
        rev_bag_map[src_bag] = []

    for bag in dest_bags:
        cleaned_bag = ''.join(i for i in bag if not i.isdigit()).strip()
        if cleaned_bag != "no other":
            if cleaned_bag not in bag_map:
                bag_map[cleaned_bag] = []
            bag_map[cleaned_bag].append(src_bag)

            num_bags = bag.split(" ")[0]
            rev_bag_map[src_bag].append((cleaned_bag, num_bags))


visited = set()
visited.add("shiny gold")


def p1_dfs(cur_bag, vis):
    if cur_bag not in bag_map:
        return
    for upper_bag in bag_map[cur_bag]:
        if upper_bag not in vis:
            vis.add(upper_bag)
            p1_dfs(upper_bag, vis)


def p2_dfs(cur_bag):
    ret_val = 1
    for lower_bag, bag_count in rev_bag_map[cur_bag]:
        ret_val += int(bag_count) * p2_dfs(lower_bag)
    return ret_val


p1_dfs("shiny gold", visited)
print(len(visited)-1)

print(p2_dfs("shiny gold")-1)
