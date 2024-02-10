from django.db import models
import yfinance as yf


class StockSymbol(models.Model):
    TYPE_CHOICES = [
        ('bullish', 'Bullish'),
        ('futures_options', 'Futures & Options'),
        ('previous_week', 'Previous Week Performance'),
    ]
    symbol = models.CharField(max_length=10)
    stop_loss = models.FloatField()
    first_target = models.FloatField()
    second_target = models.FloatField()
    target_met = models.BooleanField(default=False)
    type = models.CharField(max_length=16, choices=TYPE_CHOICES)
    current_price = models.FloatField(null=True, blank=True)  # Add field for current price
    update_date = models.DateField(auto_now=True)  # Track last update for moving to previous week

    def __str__(self):
        return self.symbol

    def update_current_price(self):
        """Fetch current price from yfinance with '.NS' suffix for NSE stocks and update the model."""
        ticker_symbol = f"{self.symbol}.NS"  # Append '.NS' to the stock symbol
        ticker = yf.Ticker(ticker_symbol)
        hist = ticker.history(period="1d")
        if not hist.empty:
            self.current_price = hist['Close'][-1]  # Get the last close price
            self.save()
            return True
        return False

    def current_price_to_target_percentage(self):
        """Calculate the percentage of the current price to the first target."""
        if self.current_price and self.first_target:
            return (self.current_price / self.first_target) * 100
        return None

    def move_to_previous_week(self):
        """Logic to move the stock to previous week if the criteria are met."""
        # Implement your logic here, e.g., based on target_met and update_date
        # This could be a scheduled task or triggered manually
