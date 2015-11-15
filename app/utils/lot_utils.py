class LotUtils(object):
    def __init__(self):
        pass

    def get_lot_size(self, total):
        if total > 100000000000:
            return 1000000000

        if total > 10000000000:
            return 100000000

        if total > 1000000000:
            return 10000000

        if total > 100000000:
            return 1000000

        if total > 10000000:
            return 100000

        # 1 million
        if total > 1000000:
            return 10000

        if total > 100000:
            return 1000

        if total > 10000:
            return 100

        if total > 1000:
            return 10

        return 1

    def get_median_lot_size(self, project_cost, value_ks, value_me, value_sr):
        multipliers = [project_cost / value_ks, project_cost / value_me, project_cost / value_sr]
        list.sort(multipliers)

        median_multiplier = multipliers[1]
        median_lot_size = self.get_lot_size(median_multiplier)

        return median_lot_size


    def get_total_lots(self, project_cost, value, median_lot_size):
        total_lots = project_cost / (median_lot_size * value)

        return int(round(total_lots))