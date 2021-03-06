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

def to_num_format(number):
    return "{:,}".format(number)

app.jinja_env.filters['to_currency'] = to_currency
app.jinja_env.filters['to_num_format'] = to_num_format

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