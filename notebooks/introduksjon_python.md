
# Introduksjon til Jupyter Notebook (forelesing)

Vi starter dagen med å skrive funksjoner som konverterer mellom grader,
radianer og gon.

    import numpy as np

    # Om man ønsker å runde ned til signifikante tall kan man bruke round()
    import math

    def deg2rad(deg): return deg*(np.pi/180)

    def rad2deg(rad): return rad*(180/np.pi)

    def gon2deg(gon): return gon/0.9

    def deg2gon(deg): return deg * 0.9

    def gon2rad(gon): return (gon*np.pi)/200

    def rad2gon(rad): return (200*rad)/np.pi


## Regne gjennomsnitt fra csv filer


    import pandas as pd
    import numpy as np

    # Kunne gjort dette i funksjon, men så ikke poenget
    df = pd.read_csv('dataset/coordinates_trygve_mobil.csv')
    arr = df.to_numpy()
    arr_mean = np.mean(arr, axis=0)
    arr_std = np.std(arr, axis=0)

    display(df)
    print(f'Gjennomsnittet for dataset: {arr_mean}')
    print(f'Standardavviket for dataset er: {arr_std}')


|     | Longitude | Latitude  |
|-----|-----------|-----------|
| 0   | 10.775348 | 59.665860 |
| 1   | 10.775348 | 59.665860 |
| 2   | 10.775348 | 59.665860 |
| 3   | 10.775347 | 59.665860 |
| 4   | 10.775347 | 59.665860 |
| ... | ...       | ...       |
| 79  | 10.775301 | 59.665858 |
| 80  | 10.775301 | 59.665858 |
| 81  | 10.775301 | 59.665858 |
| 82  | 10.775301 | 59.665858 |
| 83  | 10.775301 | 59.665858 |

84 rows × 2 columns


