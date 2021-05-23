apple = "apple.sqlite"

import database as db

db.initialize(apple)

nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

# For inserting nodes
for node in nodes:
    db.atomic(apple, db.add_node({}, node))

# Adjacent matrix mapping
connection_nodes = [
    [0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 1],
]

# Connecting nodes to each other based on adjacent matrix
for idx, i in enumerate(connection_nodes):
    for jdx, j in enumerate(i):
        if j == 1:
            db.atomic(apple, db.connect_nodes(nodes[idx], nodes[jdx]))


print(db.traverse(apple, "A", "B"))

# Error
# Traceback (most recent call last):
#   File "app.py", line 33, in <module>
#     print(db.traverse(apple, "A", "B"))
#   File "/home/achal/Projects/graph_db/simple-graph/python/database.py", line 150, in traverse
#     return atomic(db_file, _traverse)
#   File "/home/achal/Projects/graph_db/simple-graph/python/database.py", line 29, in atomic
#     results = cursor_exec_fn(cursor)
#   File "/home/achal/Projects/graph_db/simple-graph/python/database.py", line 142, in _traverse
#     for row in cursor.execute(neighbors_fn(), (json.dumps(src,))):
# sqlite3.OperationalError: circular reference: traverse