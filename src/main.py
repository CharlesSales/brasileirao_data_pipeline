from extract.matches import main as mat_ext
from extract.scorers import main as sco_ext
from extract.standings import main as sta_ext

from transform.standings import main as sta_transform
from transform.matches import main as mat_transform
from transform.scorers import main as scr_transform

from load.standings import main as sta_load
from load.scorers import main as scr_load
from load.matches import main as mat_load

def main():

    mat_ext()
    sco_ext()
    sta_ext()

    mat_transform()
    sta_transform()
    scr_transform()

    mat_load()
    sta_load()
    scr_load()

if __name__ == "__main__":
    main()