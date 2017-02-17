import json
import utils

# returns a dictionary mapping movie ID to movie details from tmdb.json, reflecting the TMDB source data model
def extract(db_path):
    print "Extracting: ",
    try:
        db = open(db_path)
        print utils.get_green_print("Success.")
    except IOError:
        print utils.get_red_print("Failure.")
        print utils.get_red_print("ERROR: ") + "No such file or directory: " + db_path
        exit(1)

    if db:
        return json.loads(db.read());