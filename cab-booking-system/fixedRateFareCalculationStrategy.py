from fareCalculationStrategy import FareCalculationStrategy


class FixedRateFareCalculationStrategy(FareCalculationStrategy):
    def calculateFare(self, ride):
        return 100