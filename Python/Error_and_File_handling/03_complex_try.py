def serve_chai(type):
    try:
        print(f"Brewing {type} chai...")
        if type.lower() == "unknown":
            raise ValueError("Chai type is unknown...")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Served {type} chai")
    finally:
        print(f"Next customer please")


serve_chai("masala")
serve_chai("unkown")
