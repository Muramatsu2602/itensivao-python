def marketCapClass(market_cap):
    if market_cap <= 50.:
        val = 'Nano Cap'
    elif ((market_cap > 50.) & (market_cap <= 300.)):
        val = 'Micro Cap'
    elif ((market_cap > 300.) & (market_cap <= 2000.)):
        val = 'Small Cap'
    elif ((market_cap > 2000.) & (market_cap <= 10000.)):
        val = 'Mid Cap'
    elif ((market_cap > 10000.) & (market_cap <= 200000.)):
        val = 'Large Cap'
    elif market_cap > 200000.:
        val = 'Mega Cap'
    else:
        val = 'Erro: Veja se você não preencheu algum argumento de forma equivocada.'
    return val
