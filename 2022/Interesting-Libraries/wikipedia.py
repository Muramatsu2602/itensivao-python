# first, pip install wikipedia

import wikipedia
result = wikipedia.summary("Debugging", sentences=2)

print(result)
