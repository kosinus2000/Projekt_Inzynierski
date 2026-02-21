import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random
from functions.otsu_function import detect_anomaly_otsu_mse
from sklearn.metrics import roc_auc_score


def print_summary(mse_anomaly,mse_healthy):
    mean_healthy = np.mean(mse_healthy)
    mean_anomaly = np.mean(mse_anomaly)
    ratio = mean_anomaly / mean_healthy


    print(f"Średni błąd dla zdrowych: {mean_healthy:.5f}")
    print(f"Średni błąd dla anomalii: {mean_anomaly:.5f}")
    print(f"Stosunek błędu (zdrowa/anomalia): {ratio:.2f}")
    if mean_anomaly > mean_healthy:
        print("Wniosek: Model skutecznie odróżnia anomalie (wyższy błąd rekonstrukcji).")
    else:
        print("Wniosek: Model ma trudności z odróżnieniem klas (błędy są zbliżone).")


def print_summary_advanced(mse_anomaly, mse_healthy):
    # Statystyki opisowe
    print(
        f"Zdrowe - Średnia: {np.mean(mse_healthy):.5f}, Mediana: {np.median(mse_healthy):.5f}, Max: {np.max(mse_healthy):.5f}")
    print(
        f"Anomalie - Średnia: {np.mean(mse_anomaly):.5f}, Mediana: {np.median(mse_anomaly):.5f}, Max: {np.max(mse_anomaly):.5f}")

    # Obliczanie AUC
    y_true = np.concatenate([np.zeros(len(mse_healthy)), np.ones(len(mse_anomaly))])
    y_scores = np.concatenate([mse_healthy, mse_anomaly])
    auc = roc_auc_score(y_true, y_scores)

    print(f"Metryka AUC-ROC: {auc:.4f}")

    if auc > 0.8:
        print("Wniosek: Model ma wysoką zdolność separacji klas.")
    elif auc > 0.5:
        print("Wniosek: Model odróżnia anomalie lepiej niż rzut monetą, ale wymaga optymalizacji.")
    else:
        print("Wniosek: Model kompletnie zawodzi (anomalie mają niższy błąd niż zdrowe).")

def generate_report(anomaly_data, decoded_anomaly_data, mse_ano, mse_test_per_image):

    local_otsu_results = []
    for i in range(len(anomaly_data)):
        input_img = anomaly_data[i]
        output_img = decoded_anomaly_data[i]

        thresh, mask, err_map = detect_anomaly_otsu_mse(input_img, output_img)
        local_otsu_results.append({
                    'threshold': thresh,
                    'mask': mask,
                    'error_map': err_map
                })

    all_thresholds = [x['threshold'] for x in local_otsu_results]

    print(f'średni próg: {np.mean(all_thresholds)}')
    print(f'najmniejsza wartość progu: {np.min(all_thresholds)}')
    print(f'największa wartość progu: {np.max(all_thresholds)}')
    print(f'std: {np.std(all_thresholds)}')

    print('-------------------------------------------------------------------------')

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(7, 5))
    sns.histplot(x=all_thresholds, bins=15, kde=False)
    plt.axvline(np.mean(all_thresholds), color='red', linestyle='--', linewidth=2, label=f'Średnia: {np.mean(all_thresholds):.2f}')

    plt.title('Rozkład wartości progów Otsu dla zbioru anomalii', fontsize=14)
    plt.xlabel('Wartość progu')
    plt.ylabel('Liczba obrazów', fontsize=12)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)

    print('------------------------------------------------------------------------------------------------')


    idx = random.randint(0, len(local_otsu_results)-1)

    curr_org = anomaly_data[idx]
    curr_dec = decoded_anomaly_data[idx]


    idx_thresh = local_otsu_results[idx]['threshold']
    idx_mask = local_otsu_results[idx]['mask']
    idx_err = local_otsu_results[idx]['error_map']

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(20, 5))
    plt.subplot(1,4,1)
    plt.title("Obraz wejściowy", fontsize=14)
    plt.imshow(curr_org)
    plt.axis('off')


    plt.subplot(1,4,2)
    plt.title('Rekonstrukcja', fontsize=14)
    plt.imshow(curr_dec)
    plt.axis('off')


    plt.subplot(1,4,3)
    plt.imshow(idx_err, cmap='inferno')
    plt.title("Mapa Błędu (Różnica)", fontsize=14)
    plt.axis('off')

    plt.subplot(1,4,4)

    plt.imshow(curr_org)
    plt.imshow(idx_mask, cmap='gray')

    plt.title(f"Maska Anomalii Próg: {idx_thresh:.1f}", fontsize=14)
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    print('----------------------------------------------------------------------------------------')

    df_healthy = pd.DataFrame({'MSE': mse_test_per_image, 'Typ': 'Zdrowa'})
    df_cancer = pd.DataFrame({'MSE': mse_ano, 'Typ': 'Anomalia'})
    df_results = pd.concat([df_healthy,df_cancer], ignore_index=True)

    plt.figure(figsize=(10, 7))
    sns.set_theme(style="whitegrid")

    ax = sns.boxplot(data=df_results, x='Typ', y='MSE')

    sns.stripplot(data=df_results, x='Typ', y='MSE', color="black", alpha=0.3, jitter=0.3, size=4)

    plt.title('Błąd rekonstrukcji dla komórek testowych (zdrowych) oraz anomalii', fontsize=14)
    plt.ylabel('Błąd średniokwadratowy MSE', fontsize=12)
    plt.xlabel('')

    threshold = np.percentile(mse_test_per_image, 95)
    plt.axhline(threshold, color='red', linestyle='--', label=f'Sugerowany próg MSE={threshold:.4f}')
    plt.legend()

    plt.show()

    print('--------------------------------------------------------------------')

    print_summary_advanced( mse_ano, mse_test_per_image)