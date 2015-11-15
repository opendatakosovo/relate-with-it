import argparse

from app import create_app

# Create the flask app.
app = create_app()

# Register custom jinja2 filters. TODO: find a better place to do this
def to_currency(cost, currency):
    symbol = currency
    if currency == 'EUR':
        symbol = u'\u20AC'

    return "%s%s{:,.2f}".format(cost) % (symbol,  u'\u00A0')

def get_lot_size(total):
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

def get_lot_amount(total):
    lot_size = get_lot_size(total)
    lot_amount = total / lot_size
    return int(lot_amount)


def get_median_lot_size(project_cost, value_ks, value_me, value_sr):
    multipliers = [project_cost / value_ks, project_cost / value_me, project_cost / value_sr]
    list.sort(multipliers)

    median_multiplier = multipliers[1]
    median_lot_size = get_lot_size(median_multiplier)

    return median_lot_size


def get_total_lots(project_cost, value, value_ks, value_me, value_sr):
    median_lot_size = get_median_lot_size(project_cost, value_ks, value_me, value_sr)
    total_lots = project_cost / (median_lot_size * value)

    return int(round(total_lots))


app.jinja_env.filters['to_currency'] = to_currency
app.jinja_env.filters['get_lot_size'] = get_lot_size
app.jinja_env.filters['get_lot_amount'] = get_lot_amount

app.jinja_env.globals.update(get_median_lot_size=get_median_lot_size)
app.jinja_env.globals.update(get_total_lots=get_total_lots)

# Run the app
if __name__ == '__main__':

    # Define the arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0', help='Host to bind to: [%(default)s].')
    parser.add_argument('--port', type=int, default=app.config['SERVER_PORT'], help='Port to listen to: [%(default)s].')
    parser.add_argument('--debug', action='store_true', default=False, help='Debug mode: [%(default)s].')

    # Parse arguemnts and run the app.
    args = parser.parse_args()
    app.run(debug=args.debug, host=args.host, port=args.port)