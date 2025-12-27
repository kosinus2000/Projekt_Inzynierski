from functions.poisson_sampling import poisson_sampling
from utils.classes.cancer_nucleus import CancerNucleusTest


@staticmethod
def points_generator(poisson: bool = False, normal: bool = False, clusterised: bool = False, number_of_points: int = 0):
    if poisson:
        if not CancerNucleusTest._lista_punktów:
            CancerNucleusTest._lista_punktów = poisson_sampling(128, 128)

        if CancerNucleusTest._licznik < len(CancerNucleusTest._lista_punktów): #
            srodek = CancerNucleusTest._lista_punktów[CancerNucleusTest._licznik]
            CancerNucleusTest._licznik += 1
        else:
            raise Exception("Brak punktów środka jądra do przydzielenia")

        return srodek