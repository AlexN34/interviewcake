class Change:
    def __init__(self):
        self.memo = {}

    # recursive
    def making_change(self, amount_left, denominations, current_index=0):
        memo_key = str((amount_left, current_index))
        if memo_key in self.memo:
            return self.memo[memo_key]

        if amount_left == 0:
            # made the desired amount! found a way.
            print("found a way!")
            return 1
        if amount_left < 0: 
            # overshot
            return 0

        if current_index == len(denominations):
            return 0 # tried everything

        print("checking ways to make %i with %s" % (
            amount_left,
            denominations[current_index:],
        ))

        current_coin = denominations[current_index]
        combination_count = 0
        while amount_left >= 0:
            combination_count += self.making_change(
                amount_left,
                denominations,
                current_index + 1
            )
            amount_left -= current_coin

        # save for next iteration
        self.memo[memo_key] = combination_count
        return combination_count

    def making_change_bottom_up(self, amount, denominations):
        way_list = [0] * (amount + 1)
        way_list[0] = 1
        for denomination in denominations:
            for i in range(denomination, amount + 1):
                if i - denomination >= 0:
                    way_list[i] = way_list[i] + way_list[i - denomination]
        return way_list[amount]
#     for denomination in denominations:
#         possible_uses_of_denomination_without_overshoot = range(0, _calc_overshoot(amount, denomination))
#         for number_of_uses in possible_uses_of_denomination_without_overshoot:
#             answer += making_change(amount - (denomination * number_of_uses), denominations)
#     return answer

        ...

#     for denomination in denominations:
#         possible_uses_of_denomination_without_overshoot = range(0, _calc_overshoot(amount, denomination))
#         for number_of_uses in possible_uses_of_denomination_without_overshoot:
#             answer += making_change(amount - (denomination * number_of_uses), denominations)
#     return answer

# def _calc_overshoot(amount, denomination):
#     count = 0
#     while amount > 0:
#         amount -= denomination
#         if amount > 0:
#             count += 1
#     return count


# run your function through some test cases here
# remember: debugging is half the battle!
ch = Change()
print(ch.making_change(4, [1,2,3]))
print(ch.making_change_bottom_up(4, [1,2,3]))
