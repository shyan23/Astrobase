import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from Backend.DB.Config import get_db_connection

conn = get_db_connection()
cur = conn.cursor()

Star_system = "Omega Nexus"


#SQL code for finding all  the Star system

sql_query_star_system = """
    select system_name from star_system
    """
    
try:
    cur.execute(sql_query_star_system)
except Exception as e:
    print(f"Problem executing SQL query from star system table: {e}")





sql_query = """
    SELECT planet_name, ra_coord AS right_ascension, dec_coord AS declination
    FROM planet p
    JOIN coordinates c ON p.object_id = c.object_id
    WHERE p.origin_system = %s
"""

try:
    cur.execute(sql_query, (Star_system,))
except Exception as e:
    print(f"Problem executing SQL query from planet and coordinate table: {e}")

try:
    result = cur.fetchall()
except Exception as e:
    print(f"Problem fetching data from planet and coordinate table: {e}")





planet_names = [row[0] for row in result]
ra_values = [row[1] for row in result]
dec_values = [row[2] for row in result]


plt.figure(figsize=(10, 6))


plt.scatter(ra_values, dec_values, color='skyblue')


for i, planet in enumerate(planet_names):
    plt.text(ra_values[i], dec_values[i], planet, fontsize=9, ha='right')


plt.xlabel('Right Ascension (RA) in Degree')
plt.ylabel('Declination (DEC) in Degree')
plt.title(f'Planet Coordinates in the {Star_system}')


plt.tight_layout()  
image_path = '/home/shyan/Desktop/Code/fastapi/Backend/image/Coordinate_plotting.png'
plt.savefig(image_path)  


plt.close()
cur.close()
conn.close()
