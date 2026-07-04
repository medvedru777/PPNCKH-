import os
import glob
import json
import math

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

try:
    import pandas as pd
except ImportError:
    pd = None


FEATURES = [
    "header_coff_timestamp",
    "header_optional_sizeof_code",
    "header_optional_sizeof_headers",
    "sections_count",
    "api_calls_count",
]


def _extract_features_from_record(record):
    imports = record.get("imports", {})
    return {
        "label": record.get("label", -1),
        "header_coff_timestamp": record.get("header", {}).get("coff", {}).get("timestamp", 0),
        "header_optional_sizeof_code": record.get("header", {}).get("optional", {}).get("sizeof_code", 0),
        "header_optional_sizeof_headers": record.get("header", {}).get("optional", {}).get("sizeof_headers", 0),
        "sections_count": len(record.get("section", {}).get("sections", [])),
        "api_calls_count": sum(len(funcs) for funcs in imports.values()) if isinstance(imports, dict) else 0,
    }


def _load_from_raw_jsonl():
    malware_data = []
    benign_data = []

    for input_file in glob.glob("data/processed/ember/ember2018/train_features_*.jsonl"):
        with open(input_file, "r", encoding="utf-8") as handle:
            for line in handle:
                try:
                    features = _extract_features_from_record(json.loads(line))
                except json.JSONDecodeError:
                    continue

                label = features["label"]
                if label == 1 and len(malware_data) < 500:
                    malware_data.append(features)
                elif label == 0 and len(benign_data) < 500:
                    benign_data.append(features)

                if len(malware_data) == 500 and len(benign_data) == 500:
                    return malware_data + benign_data

    return malware_data + benign_data


def _load_dataset(file_path):
    if pd is None:
        print("Pandas unavailable; reconstructing canonical feature subset from raw EMBER JSONL.")
        return _load_from_raw_jsonl()

    try:
        return pd.read_parquet(file_path)
    except ImportError:
        print("Parquet engine unavailable; reconstructing canonical feature subset from raw EMBER JSONL.")
        return _load_from_raw_jsonl()


def _variance(values):
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    return sum((value - mean) ** 2 for value in values) / (len(values) - 1)


def _calculate_variances(df):
    if pd is not None and hasattr(df, "columns"):
        return {feature: float(df[feature].var()) for feature in FEATURES}

    return {
        feature: _variance([float(record[feature]) for record in df])
        for feature in FEATURES
    }


def _save_with_pillow(variances, save_path):
    from PIL import Image, ImageDraw, ImageFont

    width, height = 1800, 1200
    margin_left, margin_right = 520, 180
    margin_top, margin_bottom = 150, 170
    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype("arial.ttf", 42)
        label_font = ImageFont.truetype("arial.ttf", 30)
        tick_font = ImageFont.truetype("arial.ttf", 25)
    except OSError:
        title_font = label_font = tick_font = ImageFont.load_default()

    values = [max(value, 1e-12) for _, value in variances]
    log_min = math.floor(math.log10(min(values)))
    log_max = math.ceil(math.log10(max(values)))

    def x_for(value):
        return margin_left + (math.log10(max(value, 1e-12)) - log_min) / (log_max - log_min) * plot_width

    draw.text((width / 2, 55), "Feature Variance Comparison Across Selected PE Features", fill="#111111", font=title_font, anchor="ma")

    for power in range(log_min, log_max + 1):
        x = x_for(10 ** power)
        draw.line((x, margin_top, x, height - margin_bottom), fill="#d0d0d0", width=2)
        draw.text((x, height - margin_bottom + 22), f"1e{power}", fill="#333333", font=tick_font, anchor="ma")

    row_gap = plot_height / len(variances)
    bar_height = row_gap * 0.52
    for i, (feature, value) in enumerate(variances):
        y = margin_top + row_gap * i + row_gap / 2
        label = feature.replace("_", " ")
        draw.text((margin_left - 24, y), label, fill="#111111", font=label_font, anchor="rm")
        x = x_for(value)
        draw.rounded_rectangle((margin_left, y - bar_height / 2, x, y + bar_height / 2), radius=8, fill="#4477aa")
        draw.text((min(x + 20, width - margin_right + 120), y), f"{value:.2e}", fill="#111111", font=tick_font, anchor="lm")

    draw.line((margin_left, margin_top, margin_left, height - margin_bottom), fill="#222222", width=3)
    draw.line((margin_left, height - margin_bottom, width - margin_right, height - margin_bottom), fill="#222222", width=3)
    draw.text((margin_left + plot_width / 2, height - 55), "Variance (log scale)", fill="#111111", font=label_font, anchor="ma")

    image.save(save_path)


def _save_plot(variances, save_path):
    if plt is None:
        _save_with_pillow(variances, save_path)
        return

    labels = [feature.replace("_", "\n") for feature, _ in variances]
    values = [value for _, value in variances]

    # With five features, an explicit log-scale comparison is more informative than a boxplot.
    plt.figure(figsize=(10, 6))
    bars = plt.barh(labels, values, color="#4477aa")
    plt.xscale("log")
    plt.xlabel("Variance (log scale)", fontsize=12)
    plt.title("Feature Variance Comparison Across Selected PE Features", fontsize=14)
    plt.grid(axis="x", linestyle="--", alpha=0.45)

    for bar, value in zip(bars, values):
        plt.text(
            value * 1.08,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.2e}",
            va="center",
            fontsize=9,
        )

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)

def main():
    # Load dataset
    file_path = "data/raw/ember_1k_real.parquet"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found")
        return

    df = _load_dataset(file_path)

    # Calculate variance for each feature
    variances = sorted(_calculate_variances(df).items(), key=lambda item: item[1])
    print("NUM FEATURES:", len(variances))
    for feature, value in sorted(variances, key=lambda item: item[1], reverse=True):
        print(f"{feature}: {value:.6e}")
    
    # Save the figure
    os.makedirs("figures", exist_ok=True)
    save_path = "figures/feature_variance_boxplot.png"
    _save_plot(variances, save_path)
    print(f"Successfully saved feature variance comparison chart to {save_path}")

if __name__ == "__main__":
    main()
