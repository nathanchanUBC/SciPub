import subprocess

subprocess.run(["python", "scripts/clean_data.py"])
subprocess.run(["python", "scripts/conf.py"])
subprocess.run(["python", "scripts/journ.py"])
subprocess.run(["python", "scripts/tags.py"])
subprocess.run(["python", "scripts/deptPerYr.py"])
subprocess.run(["python", "scripts/network_graph.py"])
subprocess.run(["python", "scripts/ubcAuthor.py"])