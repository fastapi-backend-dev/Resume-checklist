def brew_chai(flavor):
    if flavor not in ["masala", "elaichi", "green"]:
        raise ValueError("Unsupported chai flavor...")
    print(f"Brewing {flavor} chai...")


brew_chai("mint")
