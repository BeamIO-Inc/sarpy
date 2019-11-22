import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.getcwd(), '.env'))
os.environ['FLASK_APP'] = 'run.py'
os.environ['ATK_CONFIG'] = os.path.join(os.getcwd(), 'config.py')

import run

run.main()
