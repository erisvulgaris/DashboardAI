from django.shortcuts import render
from .models import StockSymbol

import yfinance as yf
from django.shortcuts import render
from .models import StockSymbol


def dashboard(request):
    # Assuming all symbols are initially fetched from the bullish and futures_options categories
    bullish_symbols = StockSymbol.objects.filter(type='bullish')
    futures_options_symbols = StockSymbol.objects.filter(type='futures_options')
    previous_week_symbols = StockSymbol.objects.filter(type='previous_week')  # or based on target_met and date logic

    # Fetch current prices and calculate percentages for each queryset
    for queryset in [bullish_symbols, futures_options_symbols, previous_week_symbols]:
        for symbol in queryset:
            # Fetch current price using yfinance
            ticker = yf.Ticker(f"{symbol.symbol}.NS")
            hist = ticker.history(period="1d")
            if not hist.empty:
                current_price = hist['Close'][-1]  # Get the last close price
                symbol.current_price = current_price
                symbol.percentage = (current_price / symbol.first_target * 100) if symbol.first_target else 0
            else:
                symbol.current_price = None
                symbol.percentage = None

            # Optionally, move to previous_week_symbols if target met
            # This logic might be more complex depending on how you define "previous week"
            # and would typically involve updating the symbol's type or moving it to a different list

    return render(request, 'stocks_dashboard/dashboard.html', {
        'bullish_symbols': bullish_symbols,
        'futures_options_symbols': futures_options_symbols,
        'previous_week_symbols': previous_week_symbols,
    })


def stock_detail(request, symbol):
    return render(request, 'stocks_dashboard/stock_detail.html', {'symbol': symbol})
