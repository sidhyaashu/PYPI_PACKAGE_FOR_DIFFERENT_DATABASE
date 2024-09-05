import os
from pathlib import Path

package_name = "MultiDBConnector"

list_of_files = [
   ".github/workflows/ci.yaml",
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/mongo_db.py", 
   f"src/{package_name}/core_db.py", 
   f"src/{package_name}/pinecone_db.py", 
   f"src/{package_name}/mysql_db.py",
   f"src/{package_name}/postgresql_db.py",
   f"src/{package_name}/utils.py", 

   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/test_core_unit.py",
   "tests/unit/test_pinecone_db_unit.py",
   "tests/unit/test_mysql_db_unit.py",
   "tests/unit/test_mongo_db_unit.py",
   "tests/unit/test_postgresql_db_unit.py",

   "tests/integration/__init__.py",
   "tests/integration/test_pinecone_db_integration.py",
   "tests/integration/test_mysql_db_integration.py",
   "tests/integration/test_mongo_db_integration.py",
   "tests/integration/test_postgresql_db_integration.py",

   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "MANIFEST.in",

   "experiments/experiments_mongo_db.ipynb", 
   "experiments/experiments_pinecone_db.ipynb", 
   "experiments/experiments_mysql_db.ipynb",
   "experiments/experiments_postgresql_db.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass