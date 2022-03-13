# user access this fie to run project
"""modulefunction file is import in api file and api import in main file to run the project """
import api
if __name__ == "__main__":
    api.app.run(host="0.0.0.0", port=5004, debug=True)