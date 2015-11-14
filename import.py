import argparse
from importer.kosovo_importer import KosovoImporter
from importer.montenegro_importer import MontenegroImporter
from importer.serbia_importer import SerbiaImporter

from app import create_app

import sys

reload(sys)
sys.setdefaultencoding('utf8')

# Create the flask app.
app = create_app()

def execute(region_csv):
    regions = region_csv.split(",")

    # We are using the Flask application's mongo interface.
    # Because of this we need to make sure we are operating on the Flask applicaiton's context.
    # Read more about this here: http://flask.pocoo.org/docs/0.10/appcontext/
    with app.app_context():
        for region in regions:
            if region.lower() in ["all", "kosovo"]:
                KosovoImporter().execute()

            if region.lower() in ["all", "montenegro"]:
                MontenegroImporter().execute()

            if region.lower() in ["all", "serbia"]:
                SerbiaImporter().execute()


if __name__ == '__main__':

    # Initialize arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--regions", help="The regions we want to import data from.")
    args = parser.parse_args()

    # Read the arguments and run the function
    municipalities_sr = args.regions
    execute(args.regions)