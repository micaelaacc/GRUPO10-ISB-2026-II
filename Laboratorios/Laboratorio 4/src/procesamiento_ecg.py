from pathlib import Path
import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
IMAGES = BASE / "images"
IMAGES.mkdir(exist_ok=True)

FILES = {
    "lecturabasalD2.h5": ("Basal", "D2", "basal_D2.png"),
    "lecturabasalD3.h5": ("Basal", "D3", "basal_D3.png"),
    "lecturahiperventilacionD1.h5": ("Hiperventilación", "D1", "hiperventilacion_D1.png"),
    "lecturahiperventilacionD2.h5": ("Hiperventilación", "D2", "hiperventilacion_D2.png"),
    "lecturahiperventilacionD3.h5": ("Hiperventilación", "D3", "hiperventilacion_D3.png"),
    "lecturahipoventilacionD1.h5": ("Hipoventilación", "D1", "hipoventilacion_D1.png"),
    "lecturahipoventilacionD2.h5": ("Hipoventilación", "D2", "hipoventilacion_D2.png"),
    "lecturahipoventilacionD3.h5": ("Hipoventilación", "D3", "hipoventilacion_D3.png"),
}

def read_opensignals_h5(path):
    with h5py.File(path, "r") as h5:
        device = next(iter(h5.keys()))
        group = h5[device]
        fs = int(group.attrs["sampling rate"])
        channel = np.asarray(group["raw"]["channel_2"]).squeeze().astype(float)
    return channel, fs

def estimate_hr(x, fs):
    # Banda que resalta el QRS. La estimación es descriptiva, no clínica.
    b, a = signal.butter(2, [5/(fs/2), 25/(fs/2)], btype="band")
    qrs = signal.filtfilt(b, a, x)
    envelope = np.abs(signal.hilbert(qrs))
    n = max(1, int(0.05 * fs))
    smooth = np.convolve(envelope, np.ones(n)/n, mode="same")

    med = np.median(smooth)
    mad = np.median(np.abs(smooth - med))
    threshold = med + 2 * mad

    peaks, _ = signal.find_peaks(
        smooth,
        distance=int(0.45 * fs),
        height=threshold,
        prominence=np.std(smooth) * 0.4,
    )
    peaks = peaks[(peaks > 0.3*fs) & (peaks < len(x)-0.3*fs)]
    rr = np.diff(peaks) / fs
    rr = rr[(rr > 0.4) & (rr < 1.5)]
    return 60 / np.median(rr) if len(rr) >= 2 else np.nan

results = []

for filename, (condition, lead, output_name) in FILES.items():
    x, fs = read_opensignals_h5(DATA / filename)
    duration = len(x) / fs
    hr = estimate_hr(x, fs)
    results.append((condition, lead, duration, hr))

    t = np.arange(len(x)) / fs
    start = 0.5
    end = min(start + 10, t[-1])
    mask = (t >= start) & (t <= end)
    segment = x[mask] - np.median(x[mask])

    fig, ax = plt.subplots(figsize=(10, 3.6))
    ax.plot(t[mask] - start, segment, linewidth=1)
    ax.set_title(f"ECG - {condition} - {lead}")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Amplitud relativa (cuentas ADC)")
    ax.grid(True, alpha=0.25)
    ax.margins(x=0)
    fig.tight_layout()
    fig.savefig(IMAGES / output_name, dpi=180, bbox_inches="tight")
    plt.close(fig)

print("Condición\tDerivación\tDuración (s)\tFC estimada (lpm)")
for condition, lead, duration, hr in results:
    print(f"{condition}\t{lead}\t{duration:.2f}\t{hr:.1f}")
